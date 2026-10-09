# Git and Change Safety

## 1. Preserve Existing Work

- Treat tracked modifications, untracked files, and staged changes as user work unless their origin and purpose are known.
- Inspect the repository status before making changes that could interact with existing work.
- Do not assume untracked files are disposable or generated.
- Do not overwrite, delete, or repurpose existing files without checking their contents and relevance.

## 2. Git Operations Require Authorization

- Do not stage, commit, push, reset, rebase, merge, cherry-pick, clean, or switch branches unless the user explicitly requests the relevant operation.
- Permission to implement a feature does not imply permission to commit or push it.
- Never use destructive Git commands to resolve a problem without explicit authorization.
- Do not rewrite history or discard changes to make the working tree appear clean.

## 3. Keep Changes Scoped

- Modify only files necessary for the authorized task.
- Before finishing an implementation task, inspect the resulting diff when permitted and practical.
- Identify unexpected changes rather than silently accepting or reverting them.
- Do not revert changes simply because they appear unrelated or unfamiliar.
- If a task would require replacing or removing existing work, explain the impact and obtain authorization first.

## 4. Repository Integrity

- Do not modify Git hooks, repository configuration, remotes, credentials, or ignore rules unless explicitly authorized.
- Do not expose credentials, access tokens, or other secrets in command output or responses.
- Report relevant pre-existing changes or unexpected repository state when they affect the task.

## 5. Completion Report

When changes are made, report the files changed and any important effects on the repository.

Do not claim that changes are committed, pushed, or otherwise saved to Git unless the corresponding operation was authorized and successfully completed.
