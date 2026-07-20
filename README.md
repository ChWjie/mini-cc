# mini-cc 开发进度说明

## 项目目标
mini-cc 是一个从零开始构建 AI 编程助手（类 Claude Code）的学习与实践项目，目标是通过一系列递进的章节，逐步实现 Agent 的核心能力。

## 当前开发状态
项目已经完成了前 7 个章节，当前版本已经具备更完整的规划、任务跟踪、子任务拆分与按需技能加载能力。整体进度可概括为：

- 基础 Agent 循环已完成
- 工具调用能力已完成
- 权限控制能力已完成
- Hooks 机制已接入并完善
- Todo 写入与任务提醒机制已完成
- Subagent 分工协作机制已完成
- Skill Loading 按需技能注入机制已完成
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

### 5. Todo Write
- 新增 todo_write 工具，用于在会话中维护任务清单
- 支持 pending / in_progress / completed 三种状态
- 当连续多轮未更新任务时，自动触发提醒，避免任务漂移

### 6. Subagent
- 新增 task 工具，支持为复杂子问题创建子 Agent
- 子 Agent 使用独立消息上下文，避免污染主线程上下文
- 子 Agent 仅返回摘要结果，便于父 Agent 汇总与继续推进

### 7. Skill Loading
- 新增技能扫描与注册机制，自动发现 skills 目录中的技能文件
- 系统提示词内先注入技能目录，避免一开始就加载过多上下文
- 当模型需要时，可通过 load_skill 工具按需加载完整技能内容

## 进行中 / 下一步
- 继续推进 Context Compact 与 Memory 等更高级能力
- 引入 Memory、System Prompt 和 Error Recovery 等高级能力
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

## 推送历史
- 2026-07-20：完成 s07_skill_loading 章节并更新项目说明
- 2026-07-19：完成 s06_subagent 章节并更新项目说明
- 2026-07-19：完成 s05_todo_write 章节并整理项目说明
- 2026-07-19：新增项目进度 README
- 2026-07-19：完成项目初始提交并推送到 GitHub

## 仓库信息
- GitHub 仓库：https://github.com/ChWjie/mini-cc
- 当前状态：已完成本地提交并推送到远程仓库

## 说明
这个 README 会随项目推进持续更新，用于记录当前完成度、已实现能力和后续计划。
