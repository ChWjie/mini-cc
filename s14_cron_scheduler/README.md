# s14_cron_scheduler: 定时任务调度

## 问题

s13 可以把任务放到后台执行，但所有工作仍需用户或模型当场触发。周期检查、定时汇报和延迟执行需要一个独立调度器，在指定时间把新工作重新送回 Agent Loop。

## 本章目标

实现五段 Cron 表达式的基础校验和匹配，支持注册、查看、取消、持久化与触发定时任务，并通过队列处理线程在 Agent 空闲时自动投递到期任务。

## 数据流

```text
schedule_cron -> scheduled_jobs -> durable JSON
                       |
               scheduler thread
                       |
                   cron_queue
                       |
              queue processor thread
                       |
                 Agent Loop
                       |
             [Scheduled] prompt
```

## 新增代码

- `CronJob`：保存 ID、Cron 表达式、提示词、周期性和持久化选项。
- `validate_cron()`：校验五段表达式和字段范围。
- `cron_matches()`：匹配分钟、小时、日期、月份和星期。
- `schedule_job()`、`cancel_job()`、`save_durable_jobs()` 和 `load_durable_jobs()`。
- `.scheduled_tasks.json`：保存需要跨进程恢复的任务定义。
- `cron_scheduler_loop()`：每秒轮询并将到期任务放入 `cron_queue`。
- `_last_fired`：阻止同一任务在同一分钟重复触发。
- `queue_processor_loop()`：在 Agent 空闲时自动消费触发队列。
- 三个模型工具：`schedule_cron`、`list_crons`、`cancel_cron`。

当前表达式支持整数、`*`、`*/n`、逗号列表和连续范围，例如：

```text
*/5 * * * *
0 9 * * 1-5
30 8 1,15 * *
```

## 相对上一章变化

本章继承后台任务和任务系统，在其上增加独立调度线程、触发队列与 Agent 执行锁。教学实现使用本机时间和进程内线程，尚未加入时区配置、分布式锁、错过任务补偿和任务执行历史。

## 运行与验收

```bash
python s14_cron_scheduler/code.py
```

建议输入：

```text
创建一个每 5 分钟执行一次的持久化任务，内容是检查项目状态，然后列出所有定时任务。
```

预期可以创建和列出 Cron Job，到期时调度线程只触发一次，并由队列处理器自动送入 Agent。章节已通过 Python 语法编译检查；真实到期调用需要有效模型配置。
