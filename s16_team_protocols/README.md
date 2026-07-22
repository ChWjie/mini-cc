# s16_team_protocols: 团队请求响应协议

## 问题

s15 已经能创建 Teammate 并通过 MessageBus 传递普通消息，但消息之间没有可验证的关联。Lead 无法可靠判断某条回复对应哪个关闭请求或计划审批，Teammate 完成一轮后也缺少稳定的等待与唤醒协议。

## 本章目标

在团队消息之上增加带 `request_id` 的请求响应协议和状态机，让 Lead 与 Teammate 能够完成计划提交、审批、拒绝和优雅关闭，并让协议消息经过统一入口路由。

## 数据流

```text
Lead 创建 request_id
        |
        v
MessageBus: request -> Teammate Inbox
        |                    |
        |              dispatch_message
        |                    |
Lead Inbox <- response + request_id
        |
consume_lead_inbox()
        |
match_response() -> pending_requests 状态更新
```

## 新增代码

- `ProtocolState`：保存请求 ID、类型、发送方、目标、状态、载荷和创建时间。
- `pending_requests`：跟踪尚未完成的协议请求。
- `new_request_id()`：生成请求标识。
- `match_response()`：校验响应类型，并按 ID 更新对应请求。
- `consume_lead_inbox()`：统一消费 Lead Inbox，先路由协议响应，再返回消息。
- `request_shutdown`：Lead 请求 Teammate 优雅停止。
- `request_plan`：Lead 要求 Teammate 提交执行计划。
- `submit_plan`：Teammate 将计划作为审批请求发送给 Lead。
- `review_plan`：Lead 审批或拒绝计划并返回反馈。
- Teammate 在完成一轮后进入 Inbox 等待，而不是按固定轮数立即退出。

## 相对上一章变化

s15 的 MessageBus 仍负责传输，s16 在其上增加语义协议。普通消息继续作为上下文输入，带响应类型和 `request_id` 的消息会进入状态机。

教学实现的计划审批属于协议约定，尚未在代码层阻断未获审批的写入工具。并发邮箱也仍然没有生产级文件锁。

## 运行与验收

```bash
python s16_team_protocols/code.py
```

建议让 Lead 创建 Teammate、请求计划、审批计划，最后发送关闭请求。预期每个响应都能关联原请求，状态从 `pending` 更新为 `approved` 或 `rejected`。

章节已通过语法检查，MessageBus 和协议响应关联已通过离线冒烟测试。
