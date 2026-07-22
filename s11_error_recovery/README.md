# s11_error_recovery: 模型调用错误恢复

## 问题

s10 可以稳定地组装系统提示词，但一次模型请求仍可能因为限流、服务过载、上下文过长或输出 token 用尽而中断。若所有异常都直接结束 Agent Loop，长任务很难可靠完成。

## 本章目标

为模型调用增加分类恢复策略：临时错误自动重试，服务持续过载时切换备用模型，上下文超限时紧急压缩，输出被截断时提高上限或继续生成。

## 数据流

```text
Agent Loop -> with_retry() -> 模型请求
                    |
          +---------+----------+
          |         |          |
       429/529   prompt too   max_tokens
          |        long          |
       退避/降级   紧急压缩    升级上限/续写
          |         |          |
          +---------+----------+
                    |
                  重试
```

## 新增代码

- `RecoveryState`：记录升级、压缩、续写、连续 529 和当前模型状态。
- `retry_delay()`：计算带随机抖动的指数退避时间。
- `with_retry()`：处理 429 和 529 等临时错误，最多执行有限次数重试。
- `FALLBACK_MODEL_ID`：连续服务过载时使用的可选备用模型。
- `is_prompt_too_long_error()` 与 `reactive_compact()`：识别并处理上下文超限。
- `CONTINUATION_PROMPT`：输出达到上限后要求模型直接续写。
- `DEFAULT_MAX_TOKENS` 与 `ESCALATED_MAX_TOKENS`：首次截断时提升输出预算。

## 相对上一章变化

本章保留 s10 的动态提示词和基础工具，在 LLM 调用外增加恢复层。恢复次数均有上限，避免无限重试；无法恢复的异常会写入会话并结束当前轮次。

## 运行与验收

```bash
python s11_error_recovery/code.py
```

可在 `.env` 中额外配置：

```dotenv
FALLBACK_MODEL_ID=your-fallback-model-id
```

建议通过模拟异常或替换模型客户端测试 429、529、上下文超限和 `max_tokens` 四条路径。当前章节已通过 Python 语法编译检查，尚未把外部服务错误注入做成自动化测试。
