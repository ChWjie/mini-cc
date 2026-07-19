# Project Summary: mini-cc

## Overview
mini-cc is a hands-on, progressive tutorial that teaches how to build an AI coding agent (similar to Claude Code) from scratch using Python. The project is structured as 20 incremental lessons, each adding a new capability on top of a simple agent loop.

## Technology Stack
- **Language:** Python
- **LLM SDK:** Anthropic SDK (also supports alternative providers via `ANTHROPIC_BASE_URL`)
- **Config:** python-dotenv for environment variables
- **Serialization:** PyYAML
- **Testing:** pytest

## Dependencies (from requirements.txt)
| Package         | Version   | Purpose                            |
|-----------------|-----------|------------------------------------|
| anthropic       | >=0.25.0  | Anthropic LLM API client           |
| python-dotenv   | >=1.0.0   | Load .env files for config/secrets |
| pyyaml          | >=6.0     | YAML parsing (memory, config, etc.)|
| pytest          | >=8.0     | Unit/integration testing           |

## Lesson Structure
Each lesson is a numbered directory (`s01`–`s20`) containing:
- `code.py` — the working implementation
- `README.md` — a worksheet template (problem → goal → data flow → new code → changes → verification)

## Lessons Overview
| Section | Topic               | Description                                      |
|---------|---------------------|--------------------------------------------------|
| s01     | Agent Loop          | Core while-loop: LLM → tool → result → LLM       |
| s02     | Tool Use            | Expanding toolset beyond just bash               |
| s03     | Permission          | Sandboxing & permission checks                   |
| s04     | Hooks               | Pre/post hooks for agent behavior                |
| s05     | Todo Write          | Task tracking within the agent                   |
| s06     | Subagent            | Spawning child agents for subtasks               |
| s07     | Skill Loading       | Dynamically loading reusable skills              |
| s08     | Context Compact     | Compressing conversation history                 |
| s09     | Memory              | Persistent memory across sessions                |
| s10     | System Prompt       | Advanced system prompt engineering               |
| s11     | Error Recovery      | Graceful error handling and retries              |
| s12     | Task System         | Structured task management                       |
| s13     | Background Tasks    | Running tasks in the background                  |
| s14     | Cron Scheduler      | Scheduled/recurring task execution               |
| s15     | Agent Teams         | Multi-agent collaboration                        |
| s16     | Team Protocols      | Communication protocols between agents           |
| s17     | Autonomous Agents   | Fully autonomous agent behavior                  |
| s18     | Worktree Isolation  | Git worktree isolation for parallel work         |
| s19     | MCP Plugin          | Model Context Protocol plugin system             |
| s20     | Comprehensive       | Bringing everything together                     |

## Note
- There is no root-level `README.md`. Each lesson has its own `README.md` as a structured worksheet template.
