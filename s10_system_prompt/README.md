# s10_system_prompt: 动态系统提示词

## 问题

s09 已经能够保存和加载长期记忆，但系统提示词仍然容易被写成一整段固定文本。随着工具、工作区状态和记忆不断变化，固定提示词会出现两个问题：无关内容长期占用上下文，以及运行状态变化后提示词不能及时更新。

## 本章目标

把系统提示词拆成稳定片段，根据真实运行状态动态组装，并缓存相同上下文对应的结果。这样既能让提示词保持可维护，也为后续错误恢复、任务系统和更多运行时能力留下组合入口。

## 数据流

```text
工作区 / 可用工具 / Memory
            |
            v
     update_context()
            |
            v
 get_system_prompt(context)
       |           |
    cache hit   assemble_system_prompt()
       |           |
       +-------> system prompt -> Agent Loop
```

## 新增代码

- `PROMPT_SECTIONS`：保存 identity、tools、workspace 等稳定提示词片段。
- `assemble_system_prompt(context)`：按照当前状态选择并拼接提示词。
- `get_system_prompt(context)`：用确定性的 JSON 序列化结果作为缓存键。
- `update_context(context, messages)`：从工作区和 `.memory/MEMORY.md` 派生上下文。
- Agent Loop 在每轮工具执行后重新检查上下文并获取系统提示词。

## 相对上一章变化

本章聚焦系统提示词装配，因此保留基础文件工具与记忆索引读取，省略 s09 中完整的记忆提取、选择和压缩流水线。生产实现中，这些模块应组合使用，而不是相互替代。

## 运行与验收

```bash
python s10_system_prompt/code.py
```

建议先运行一次普通文件读取，再在 `.memory/MEMORY.md` 中加入内容后继续对话。预期可以看到提示词首次组装、上下文未变化时缓存命中，以及记忆存在时 memory 片段被加入。

本章已通过 Python 语法编译检查；真实模型交互需要有效 `.env` 配置。
