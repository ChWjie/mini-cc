# Project Summary: mini-cc

## Overview

mini-cc is a hands-on Python course for building a small terminal coding agent from first principles. The repository contains 20 lesson directories. Each lesson has an independently readable `code.py` implementation and a companion `README.md` explaining the mechanism introduced in that stage.

## Current Status

- Completed: s01-s14 (14/20 lessons, 70%)
- Latest milestone: s14 Cron Scheduler
- Planned: s15-s20
- The root `README.md` contains setup instructions, architecture, detailed progress, and the roadmap.

Later lessons are focused teaching snapshots. They preserve the main agent structure but may omit an earlier advanced subsystem when that keeps the current lesson easier to understand. The complete integration is planned for s20.

## Technology Stack

- Language: Python 3.10+
- LLM client: Anthropic Python SDK
- Provider support: Anthropic API and Anthropic-compatible endpoints through `ANTHROPIC_BASE_URL`
- Configuration: python-dotenv
- Serialization: JSON and PyYAML
- Testing: pytest is included; broader automated coverage is still planned

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
| s15 | Agent Teams | Planned |
| s16 | Team Protocols | Planned |
| s17 | Autonomous Agents | Planned |
| s18 | Worktree Isolation | Planned |
| s19 | MCP Plugin | Planned |
| s20 | Comprehensive Integration | Planned |

## Runtime Data

Local secrets and generated state are ignored by Git, including `.env`, `.memory/`, `.tasks/`, `.transcripts/`, `.task_outputs/`, `.worktrees/`, and `.scheduled_tasks.json`.
