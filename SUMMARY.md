# Project Summary: mini-cc

## Overview

mini-cc is a 20-lesson Python course for building a small terminal coding agent from first principles. Each lesson provides an independently runnable `code.py` and a companion `README.md`. The progression starts with a minimal agent loop and ends with an integrated agent that combines tools, context management, task orchestration, multi-agent collaboration, Git Worktrees, and dynamic MCP tools.

## Status

- Completed: s01-s20 (20/20 lessons, 100%)
- Final milestone: s20 Comprehensive Agent
- Syntax validation: all lesson modules pass Python compilation
- Offline smoke validation: team protocols, autonomous task discovery, Git Worktrees, MCP discovery, and s20 integration components pass
- Online model calls require a local `.env` with a valid API key

The lesson directories are focused teaching snapshots. Some intermediate lessons intentionally omit an earlier complex subsystem to keep the current topic readable. s20 recombines the representative mechanisms into one loop.

## Technology Stack

- Language: Python 3.10+
- LLM client: Anthropic Python SDK
- Provider support: Anthropic API and compatible endpoints through `ANTHROPIC_BASE_URL`
- Configuration: python-dotenv
- Serialization: JSON, JSONL, and PyYAML
- Concurrency: Python threads, queues, and locks
- Isolation: Git Worktree
- Extension model: teaching MCP client with dynamic tool discovery
- Testing dependency: pytest, with broader automated coverage planned

## Lessons

| Section | Topic | Status |
| --- | --- | --- |
| s01 | Agent Loop | Complete |
| s02 | Tool Use | Complete |
| s03 | Permission | Complete |
| s04 | Hooks | Complete |
| s05 | Todo Write | Complete |
| s06 | Subagent | Complete |
| s07 | Skill Loading | Complete |
| s08 | Context Compact | Complete |
| s09 | Memory | Complete |
| s10 | System Prompt | Complete |
| s11 | Error Recovery | Complete |
| s12 | Task System | Complete |
| s13 | Background Tasks | Complete |
| s14 | Cron Scheduler | Complete |
| s15 | Agent Teams | Complete |
| s16 | Team Protocols | Complete |
| s17 | Autonomous Agents | Complete |
| s18 | Worktree Isolation | Complete |
| s19 | MCP Plugin | Complete |
| s20 | Comprehensive Integration | Complete |

## Runtime Data

Local secrets and generated state are ignored by Git, including `.env`, `.memory/`, `.tasks/`, `.transcripts/`, `.task_outputs/`, `.worktrees/`, `.mailboxes/`, and `.scheduled_tasks.json`.

See the root `README.md` for architecture, setup, detailed capabilities, validation, limitations, and post-course engineering work.
