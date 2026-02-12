# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Test repository for exercising the [radetsky/llm-code-review](https://github.com/radetsky/llm-code-review) GitHub Action. The action runs an AI code review on every pull request using OpenRouter (model: `openai/gpt-4o-mini`).

## CI

The only CI workflow is `.github/workflows/llm-core-review.yml` — it triggers on PR open/sync/reopen events. Required secret: `LLM_API_KEY`.

## Running Code

```bash
python test1.py
```

No dependencies, no virtualenv, no test framework — plain Python scripts executed directly.
