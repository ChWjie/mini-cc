# s15_agent_teams: 多 Agent 团队与消息总线

## 问题

s14 引入了定时调度，但所有工作仍由单个 Agent 串行完成。当任务需要并行处理、角色分工或多视角协作时，单 Agent 架构成为瓶颈。需要一个机制让 Lead Agent 能够派遣队友、分配任务并通过消息通信协作完成工作。

## 本章目标

引入基于文件的 MessageBus 消息总线和 `spawn_teammate_thread` 队友派遣机制。Lead Agent 可以在后台线程中创建具有独立上下文和受限工具集的队友 Agent，队友通过 MessageBus 向 Lead 发送结果，Lead 通过 inbox 轮询接收消息并驱动新一轮对话。

## 数据流

```text
Lead Agent:
  input()/cron/inbox_wake → messages → LLM → tool_use ──→ loop
        ↑                                  ↓
        │                            spawn_teammate / send_message
        │                                  ↓
  check_inbox ← MessageBus ← teammate.send_message

Teammate Thread:
  prompt → LLM → bash/read/write/send_message → loop (max 10 turns)
                      ↓
              MessageBus.send(name, "lead", result)
```

inbox_poller 线程每秒检查 Lead 的邮箱和后台任务结果，发现消息时注入 `[Inbox]` 或 `<task_notification>` 到 history 并触发 agent_loop 执行新一轮。

## 新增代码

### MessageBus 消息总线

- `MAILBOX_DIR`（`.mailboxes/`）：每个 Agent 一个 `.jsonl` 文件作为收件箱。
- `MessageBus.send(from, to, content, msg_type)`：将消息追加到目标 Agent 的 inbox 文件。
- `MessageBus.read_inbox(agent)`：读取并删除 inbox 文件（destructive read，消费消息）。
- `MessageBus.peek(agent)`：非破坏性检查，判断是否有未读消息，用于 inbox_poller 的唤醒条件。
- 教学版本使用文件追加 + 删除，不加锁；真实 CC 使用 `proper-lockfile` 保证并发写入安全。

### 队友派遣与生命周期

- `spawn_teammate_thread(name, role, prompt)`：在守护线程中创建队友 Agent。
- 队友拥有独立的 system prompt（包含角色描述）和简化的工具集：`bash`、`read_file`、`write_file`、`send_message`。
- 队友每轮开始前检查自身 inbox（支持 Lead 向队友发送指令）。
- 教学版本限制队友最多 10 轮对话；真实 CC 使用 idle loop（等待 inbox → 工作 → 重复）直到 `shutdown_request`。
- `active_teammates`：追踪当前活跃的队友名称与状态。
- 队友结束后提取最后一条 assistant 文本作为摘要，通过 `BUS.send(name, "lead", summary, "result")` 发送给 Lead，然后从 `active_teammates` 中移除自身。

### Lead 新增工具

| 工具 | 参数 | 功能 |
| --- | --- | --- |
| `spawn_teammate` | `name`, `role`, `prompt` | 在后台线程中创建队友 Agent |
| `send_message` | `to`, `content` | 通过 MessageBus 向指定 Agent 发送消息 |
| `check_inbox` | 无 | 读取 Lead 的收件箱（destructive） |

### 事件驱动唤醒

- `events`（`queue.Queue`）：统一接收 `user`（用户输入）、`wake`（inbox/后台通知）和 `quit` 事件。
- `input_reader` 线程：读取用户终端输入。
- `inbox_poller` 线程：每秒轮询 `BUS.peek("lead")` 和 `has_pending_background()`，发现消息时向 `events` 发送 `wake`。
- 主循环根据事件类型构造 history 并调用 `agent_loop` 执行一轮。
- `[all teammates done]` 提示在所有队友完成且邮箱清空后输出一次。

## 相对上一章变化

本章保留 s14 的全部功能：Cron 调度器、后台任务、任务系统和所有前期工具。在此基础上：

- **新增 MessageBus**：文件级消息总线，支持异步 Agent 间通信。
- **新增队友派遣**：Lead 可以通过 `spawn_teammate` 创建后台工作线程。
- **新增消息工具**：`send_message` 和 `check_inbox` 支持 Lead 与队友双向通信。
- **新增事件队列**：用户输入、inbox 唤醒和后台通知统一通过 `queue.Queue` 驱动 agent_loop。

教学版本刻意省略：
- 队友工具集不包含任务系统工具（`create_task` 等）和 Cron 工具，保持队友角色简化。
- 不使用文件锁，依赖教学场景下的顺序访问。
- 队友没有 idle loop，使用固定 10 轮上限后自动结束。
- 不支持队友之间的直接通信，所有消息必须经过 Lead 中转。

## 运行与验收

```bash
python s15_agent_teams/code.py
```

建议输入：

```text
帮我创建一个队友叫 alice，角色是文档专家，让她写一个 hello.py 的 README 说明文件。
```

预期流程：
1. Lead 调用 `spawn_teammate(name="alice", role="文档专家", prompt="写一个 hello.py 的 README 说明文件")`。
2. 终端输出 `[teammate] alice spawned as 文档专家`。
3. alice 在后台线程中独立运行，调用 `write_file` 创建文件。
4. alice 完成后通过 `send_message` 向 Lead 发送结果摘要。
5. `inbox_poller` 检测到 Lead 邮箱有消息，触发 `[wake]`。
6. Lead 读取 inbox 消息并回复用户。
7. 终端输出 `[all teammates done]`。

章节已通过 Python 语法编译检查；真实模型调用需要有效 API Key。
