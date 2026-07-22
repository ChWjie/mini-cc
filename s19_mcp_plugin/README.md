# s19_mcp_plugin: 动态 MCP 工具池

## 问题

s18 的所有工具都硬编码在 Agent 文件中。每增加一个外部系统，都需要修改工具 Schema、处理器和分发逻辑。Coding Agent 需要一种运行时发现和挂载外部工具的扩展机制。

## 本章目标

用一个最小 `MCPClient` 教学实现展示 MCP 工具发现、命名空间和动态工具池。Agent 连接 Server 后，发现的工具会与内置工具一起提供给模型。

## 数据流

```text
connect_mcp("docs")
        |
        v
MCPClient.register(tool defs, handlers)
        |
        v
assemble_tool_pool()
        |
        +-> builtin tools
        +-> mcp__docs__search
        +-> mcp__docs__get_version
        |
        v
Agent Loop 下一轮模型请求
```

## 新增代码

- `MCPClient`：保存工具定义与处理器，并提供统一调用入口。
- `normalize_mcp_name()`：把 Server 和工具名称转换为安全标识。
- `connect_mcp()`：连接教学 Server 并注册发现的工具。
- `assemble_tool_pool()`：动态合并内置工具 Schema、处理器和 MCP 工具。
- `mcp__<server>__<tool>`：避免不同 Server 之间的工具名称冲突。
- `docs` 模拟 Server：提供 `search` 和 `get_version`。
- `deploy` 模拟 Server：提供 `trigger` 和 `status`。
- Agent 调用 `connect_mcp` 后会重新组装工具池，使新工具从下一轮开始可见。

## 相对上一章变化

任务、团队、协议和 Worktree 工具仍是内置工具，MCP 工具作为后绑定扩展进入同一分发器。系统提示词不缓存连接状态，以免新增工具后仍使用旧工具目录。

本章的 MCPClient 是教学模拟，并未实现 MCP 标准的 stdio、SSE 或 Streamable HTTP 传输，也没有真实的初始化握手和 JSON-RPC 生命周期。

## 运行与验收

```bash
python s19_mcp_plugin/code.py
```

建议输入：

```text
连接 docs MCP server，然后调用新发现的 search 工具查找 agent loop。
```

章节已通过语法检查，Server 连接、工具发现、命名空间和处理器调用已通过离线冒烟测试。
