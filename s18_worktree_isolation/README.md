# s18_worktree_isolation: Git Worktree 工作区隔离

## 问题

s17 允许多个 Agent 自主领取任务，但如果它们都在同一个目录修改文件，就会互相覆盖未提交改动。并行 Coding Agent 需要独立分支和独立工作目录。

## 本章目标

使用 Git Worktree 为任务创建隔离目录和分支，将任务记录绑定到 Worktree，并在清理前检查改动，避免误删未审查成果。

## 数据流

```text
Task -> create_worktree(name, task_id)
          |
          +-> branch: wt/<name>
          +-> .worktrees/<name>/
          +-> task.worktree = <name>
          +-> events.jsonl

Teammate 领取任务 -> 在绑定 Worktree 中执行工具
```

## 新增代码

- `Task.worktree`：保存任务绑定的工作区名称。
- `validate_worktree_name()`：限制名称字符和长度，阻止路径穿越。
- `run_git()`：以参数数组执行 Git 命令并返回状态和截断输出。
- `create_worktree()`：创建 `wt/<name>` 分支和 `.worktrees/<name>` 目录。
- `bind_task_to_worktree()`：把任务与 Worktree 关联，保持任务等待领取。
- `_count_worktree_changes()`：检查未提交文件和未推送提交。
- `remove_worktree()`：默认拒绝删除存在成果的工作区。
- `keep_worktree()`：保留工作区供人工审查。
- `.worktrees/events.jsonl`：记录创建、保留和删除事件。
- Teammate 文件与 Shell 工具根据任务绑定切换执行目录。

## 相对上一章变化

s17 解决“谁来做任务”，s18 解决“在哪里做任务”。自主领取流程保持不变，但执行上下文由主仓库切换到任务绑定的 Worktree。

强制清理仍可能删除成果，因此 `discard_changes=true` 只应在明确确认后使用。教学实现不会自动合并、推送或创建 Pull Request。

## 运行与验收

```bash
python s18_worktree_isolation/code.py
```

本章必须在 Git 仓库中运行。可以创建任务后调用 `create_worktree`，检查分支和目录，再在无改动时调用 `remove_worktree`。

章节已通过语法检查，并已在临时 Git 仓库中完成真实 Worktree 创建与删除测试。
