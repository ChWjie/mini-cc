# s20_comprehensive: 综合 Coding Agent

## 问题

s01-s19 分别解释了 Agent 的各个局部机制，但中间章节为了保持教学重点，会暂时省略其他复杂模块。课程最后需要一个统一入口，展示这些能力如何围绕同一个 Agent Loop 组合工作。

## 本章目标

构建最终综合版本，将工具、权限、Hook、Todo、Subagent、Skills、上下文压缩、记忆索引、错误恢复、任务图、后台任务、Cron、Agent Teams、协议、自主任务、Worktree 和动态 MCP 工具整合进一个终端 Agent。

## 总体数据流

```text
用户 / Cron / Inbox / 后台结果
              |
              v
       prepare_context()
              |
       assemble_system_prompt()
              |
         模型 tool_use
              |
      PreToolUse Hooks
              |
     dynamic handlers pool
       /      |       \
   同步工具  后台任务  团队/调度
       \      |       /
          tool_result
              |
              +------> Agent Loop
```

## 整合模块

### Agent 核心

- Anthropic Messages 兼容模型调用。
- 动态系统提示词和统一 `messages` 历史。
- 工具 Schema 与处理器分离的分发结构。
- `tool_use -> tool_result -> 下一轮模型调用` 闭环。

### 开发工具与权限

- Shell、读取、写入、编辑和 Glob。
- `safe_path()` 工作区边界。
- UserPromptSubmit、PreToolUse、PostToolUse 和 Stop Hooks。
- 危险命令拦截、操作日志和大输出提示。

### 规划与上下文

- Todo 更新与多轮遗漏提醒。
- Skill 扫描和 `load_skill` 按需加载。
- 工具结果预算、历史裁剪、微压缩、摘要压缩和 Transcript。
- `.memory/MEMORY.md` 索引注入；完整记忆提取流程保留在 s09 供独立学习。
- 429/529 重试、备用模型、上下文超限恢复和输出续写。

### 任务与异步执行

- 持久化任务、依赖、owner、Worktree 绑定和状态流转。
- 慢工具后台线程与 `<task_notification>`。
- Cron 校验、持久化、调度线程和自动注入。

### 多 Agent 编排

- 轻量 Subagent。
- Lead 与 Teammate 独立上下文。
- JSONL MessageBus、计划审批、关闭协议和 `request_id`。
- 空闲 Agent 扫描任务板并自动领取任务。
- Git Worktree 隔离与安全清理。

### MCP 扩展

- 动态连接教学版 `docs` 和 `deploy` Server。
- `mcp__server__tool` 工具命名空间。
- 每轮重新组装内置与 MCP 工具池。

## 相对上一章变化

s19 重点展示动态 MCP 工具，本章把前面章节的代表性机制重新放到一个主循环中。这里不是简单复制每一章全部代码，而是选择能够协同工作的实现版本，明确统一的上下文准备、模型调用、权限、工具分发和异步事件入口。

## 运行

```bash
python s20_comprehensive/code.py
```

建议从简单任务开始，逐步验证组合能力：

```text
先列出可用技能并加载 code-review，然后创建“检查代码”和“更新文档”两个任务。
```

```text
连接 docs MCP server，使用新工具查找 agent 文档。
```

```text
为两个任务创建独立 worktree，并派遣两个 teammate 分别处理。
```

## 验收结果

- s20 通过 Python 语法编译检查。
- Todo 校验与更新通过。
- 持久化任务创建和依赖判断通过。
- Cron 合法与非法表达式校验通过。
- MCP 动态工具发现与调用通过。
- 工作区路径逃逸拦截通过。
- 没有在验证过程中发起真实模型请求。

## 教学边界

- MCP Server 是模拟实现，不包含真实传输协议。
- MessageBus 没有生产级文件锁。
- 线程任务缺少进程重启恢复和分布式协调。
- 权限规则不能替代操作系统沙箱。
- 自动化测试覆盖仍需继续补充。
- 完整记忆提取与合并逻辑在 s09 中展示，s20 使用记忆索引注入。
