# s06_subagent: 子 Agent 分工协作

## 问题
上一章已经具备了任务规划能力，但在复杂问题中，单个 Agent 仍然可能变得过于庞大和混乱。比如一个大任务中包含多个子问题时，主 Agent 很难同时高效地处理所有细节。

## 本章目标
本章新增 task 工具，用于让父 Agent 将复杂子问题委派给一个子 Agent。子 Agent 使用独立消息上下文执行任务，执行完成后只返回摘要结果，避免污染主 Agent 的上下文。

## 数据流
用户输入 -> 父 Agent 判断需要拆分 -> 调用 task 工具 -> 子 Agent 使用独立 messages[] 执行 -> 返回摘要 -> 父 Agent 继续汇总与推进。

## 新增代码
本章新增了以下内容：

- SUB_SYSTEM：子 Agent 的专用系统提示词
- SUB_TOOLS：子 Agent 可使用的工具集合（不包含 task，避免递归）
- spawn_subagent()：创建子 Agent 并运行一段安全上限的执行循环
- extract_text()：从消息内容中提取最终文本摘要
- task 工具 Schema：允许父 Agent 发起子任务

## 相对上一章变化
相比 s05_todo_write，本章保留了：

- Agent Loop 的基本执行逻辑
- todo_write 任务规划能力
- Hook 与权限控制机制

新增的内容是：

- 子 Agent 的创建与隔离执行
- 子任务的委派与摘要收敛
- 递归委派的防护机制

## 运行与验收
运行方式：

```bash
python s06_subagent/code.py
```

建议输入：

```text
请帮我分析当前仓库的结构，并拆分成几个子任务来完成说明文档整理。
```

预期结果：

- 父 Agent 会调用 task 工具发起子任务
- 子 Agent 会在独立上下文中完成子任务
- 最终返回简洁摘要，供父 Agent 继续处理

实际验证：

- 章节实现已集成到当前项目版本中
- 代码已完成并可在当前环境中运行
