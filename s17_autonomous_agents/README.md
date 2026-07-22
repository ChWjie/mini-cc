# s17_autonomous_agents: 自主任务领取与生命周期

## 问题

s16 的 Teammate 可以等待消息，但仍主要依赖 Lead 主动分配工作。团队任务板中即使存在已经解除依赖的待办，空闲 Agent 也不会主动发现和处理。

## 本章目标

为 Teammate 建立 WORK、IDLE、SHUTDOWN 生命周期。Agent 完成当前工作后进入空闲轮询，优先处理协议消息，也能扫描任务板、自动领取符合条件的任务并恢复执行。

## 数据流

```text
WORK -> 当前任务完成 -> IDLE
                         |
             +-----------+-----------+
             |                       |
          Inbox 消息             可领取任务
             |                       |
          WORK/关闭        claim_task(owner) -> WORK
                         |
                      超时关闭
```

## 新增代码

- `scan_unclaimed_tasks()`：查找 pending、无 owner 且依赖全部完成的任务。
- `idle_poll()`：按固定间隔检查 Inbox 和任务板。
- 空闲阶段收到 `shutdown_request` 时发送关联响应并结束。
- 自动领取成功后向上下文注入 `<auto-claimed>` 任务信息。
- Teammate 工具集增加 `list_tasks`、`claim_task` 和 `complete_task`。
- `claim_task()` 验证任务状态、依赖和 owner，避免重复领取。
- Teammate 生命周期从一次性线程扩展为 WORK、IDLE、SHUTDOWN 状态流转。

## 相对上一章变化

s16 负责通信协议，s17 将协议与任务板连接起来。Lead 可以继续主动发消息，空闲 Teammate 也可以在没有新指令时自行寻找工作。

教学版本采用轮询和固定空闲超时，没有心跳、租约续期、故障接管或分布式任务锁。

## 运行与验收

```bash
python s17_autonomous_agents/code.py
```

建议先创建一个无依赖任务和一个被其阻塞的任务，再启动 Teammate。预期 Teammate 只能发现首个任务，完成后第二个任务才会进入可领取集合。

章节已通过语法检查，任务依赖、自动发现、领取和解锁流程已通过离线冒烟测试。
