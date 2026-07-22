# s13_background_tasks: 后台任务与结果通知

## 问题

s12 的工具调用都在 Agent Loop 中同步执行。安装依赖、构建、测试等慢命令会长时间阻塞对话，Agent 也无法在等待期间继续处理其他工作。

## 本章目标

将耗时工具调用分派到后台线程，让 Agent 立即获得后台任务 ID，并在任务完成后把结果作为独立通知注入后续上下文。

## 数据流

```text
tool_use -> should_run_background()
                 |
          +------+------+
          |             |
        False          True
          |             |
       同步执行     daemon thread
                        |
                  background_results
                        |
              collect_background_results()
                        |
              <task_notification>
```

## 新增代码

- `background_tasks`：记录后台任务 ID、原工具调用、命令与状态。
- `background_results`：保存后台执行结果。
- `background_lock`：保护线程共享状态。
- `should_run_background()`：优先读取模型的显式参数，再使用慢命令特征判断。
- `start_background_task()`：创建守护线程并立即返回后台任务 ID。
- `collect_background_results()`：收集完成结果并生成 `<task_notification>`。
- `bash` 工具新增 `run_in_background` 参数。

## 相对上一章变化

本章保留 s12 的持久化任务工具，在工具分发器前增加同步或后台执行决策。后台通知使用新的文本块注入，而不会复用已经完成的 `tool_use_id`。

教学版本只使用进程内线程和内存状态。进程退出后，正在运行的后台任务与未消费结果不会恢复。

## 运行与验收

```bash
python s13_background_tasks/code.py
```

建议让 Agent 执行一个短暂的测试或构建命令，并要求 `run_in_background=true`。预期主循环立即返回 `bg_xxxx`，命令完成后出现 `<task_notification>`。章节已通过 Python 语法编译检查。
