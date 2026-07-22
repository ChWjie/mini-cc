# s12_task_system: 持久化任务依赖图

## 问题

s05 的 Todo 更适合单次会话中的轻量计划。复杂开发任务需要跨轮次保存，还需要描述任务之间的先后关系、负责人和完成状态。只有一张内存待办列表，无法支撑后续多 Agent 协作。

## 本章目标

实现一个文件持久化任务系统。每个任务拥有唯一 ID、状态、负责人和 `blockedBy` 依赖，并通过工具让 Agent 创建、查看、领取和完成任务。

## 数据流

```text
create_task -> .tasks/<task_id>.json
                       |
                       v
list/get -> can_start -> claim_task -> complete_task
                 |                         |
              检查依赖                  解锁下游任务
```

## 新增代码

- `Task` 数据类：包含 `id`、`subject`、`description`、`status`、`owner` 和 `blockedBy`。
- `.tasks/`：每个任务使用一个 JSON 文件持久化。
- `create_task()`、`save_task()`、`load_task()`、`list_tasks()` 和 `get_task()`。
- `can_start()`：检查所有依赖任务是否已经完成，缺失依赖视为阻塞。
- `claim_task()`：领取可执行任务并切换为 `in_progress`。
- `complete_task()`：完成任务，并报告刚被解锁的下游任务。
- 五个模型工具：`create_task`、`list_tasks`、`get_task`、`claim_task`、`complete_task`。

## 相对上一章变化

本章专注任务模型与持久化，因此使用简化 Agent Loop，没有复制 s11 的完整错误恢复代码。真实综合版本应将任务系统放在工具层，并与重试和上下文模块组合。

## 运行与验收

```bash
python s12_task_system/code.py
```

建议输入：

```text
创建“实现功能”和“编写测试”两个任务，让测试依赖功能实现，然后按顺序领取并完成它们。
```

预期任务写入 `.tasks/`，被依赖任务完成前不能领取下游任务，完成后会显示新解锁任务。章节已通过 Python 语法编译检查。
