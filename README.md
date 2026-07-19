# mini-cc 开发进度说明

## 项目目标
mini-cc 是一个从零开始构建 AI 编程助手（类 Claude Code）的学习与实践项目，目标是通过一系列递进的章节，逐步实现 Agent 的核心能力。

## 当前开发状态
项目目前已经完成了前 4 个基础章节，并正在向后续章节推进。整体进度可概括为：

- 基础 Agent 循环已完成
- 工具调用能力已完成
- 权限控制能力已完成
- Hooks 机制已接入并正在完善
- 后续章节正在持续扩展

## 已完成内容

### 1. 基础 Agent Loop
- 完成最核心的 Agent 执行循环
- 支持 LLM 生成响应、执行工具、回填结果再继续推理

### 2. Tool Use
- 增加工具调用能力
- 为 Agent 提供更丰富的执行接口

### 3. Permission
- 引入权限控制机制
- 避免不受限制的操作执行

### 4. Hooks
- 支持前置/后置 Hook
- 为 Agent 行为扩展提供更灵活的控制点

## 进行中 / 下一步
- 继续完善 Todo 写入能力
- 增加 Subagent 的协作机制
- 引入 Skill Loading 与 Context Compact
- 继续推进 Memory、System Prompt 和 Error Recovery 等高级能力
- 最终整合成更完整的多模块 Agent 系统

## 项目结构
- s01_agent_loop：基础 Agent 循环
- s02_tool_use：工具调用
- s03_permission：权限控制
- s04_hooks：Hook 机制
- s05_todo_write：任务跟踪
- s06_subagent：子 Agent
- s07_skill_loading：技能加载
- s08_context_compact：上下文压缩
- s09_memory：记忆能力
- s10_system_prompt：系统提示词
- s11_error_recovery：错误恢复
- s12_task_system：任务系统
- s13_background_tasks：后台任务
- s14_cron_scheduler：定时任务
- s15_agent_teams：多 Agent 协作
- s16_team_protocols：协作协议
- s17_autonomous_agents：自主执行
- s18_worktree_isolation：工作区隔离
- s19_mcp_plugin：插件扩展
- s20_comprehensive：综合集成

## 仓库信息
- GitHub 仓库：https://github.com/ChWjie/mini-cc
- 当前状态：已完成本地提交并推送到远程仓库

## 说明
这个 README 旨在随项目推进持续更新，用于记录当前完成度、已实现能力和后续计划。
