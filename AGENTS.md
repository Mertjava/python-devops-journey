# AGENTS.md

This file gives project-specific instructions to Codex or any coding agent working in this repository.

## Start Here

Before helping with this project, read these files:

```text
README.md
DAILY_TASKS.md
docs/START_HERE_FOR_CODEX.md
docs/CODEX_AGENT_GUIDELINES.md
docs/GIT_DAILY_PUSH_GUIDE.md
docs/DAILY_PUSH_LOG.md
```

If the task is about the long-term real-world project, also read:

```text
REAL_WORLD_DEVOPS_PROJECT_PLAN.md
```

## User Context

The user is Mert, GitHub username `Mertjava`.

Mert is an associate developer at Symetra and is learning Python, Docker, SQL, AWS, Git, Azure DevOps, testing, and agent-assisted development seriously.

The goal is not shallow tutorial completion. The goal is deep understanding and professional habits.

## Language Rules

Use Turkish for normal conversation unless the user asks otherwise.

Use English for code-related materials:

- code comments
- variable names
- function names
- file names
- commit messages
- documentation
- test names
- project text

## Teaching Rules

When explaining terminal commands, Git, Docker, AWS, SQL, or Azure DevOps, use this structure:

```text
1. What are we doing?
2. Why are we doing it?
3. What command should the user run?
4. What output should the user expect?
5. What does an error mean if it appears?
```

The user wants to understand the reason behind each command.

## Git Rules

For Git/GitHub work, guide the user instead of doing everything automatically.

The user wants to type Git commands himself.

Good agent behavior:

- suggest the next command
- explain why it is needed
- ask the user to paste the output
- review the output
- then give the next step

Do not automatically commit or push unless the user clearly asks for it.

Daily Git checks:

```bash
python3 check_course.py
python3 scripts/daily_git_check.py
git status
```

Good commit messages:

```text
Complete day 2 lists lesson
Practice day 3 loops and guessing game
Add Codex agent working guidelines
```

Avoid vague commit messages like:

```text
update
fix
new stuff
```


## After Push Documentation Rule

After every successful GitHub push, check whether the push is documented in:

```text
docs/DAILY_PUSH_LOG.md
```

If the latest push is not documented, guide Mert to add a new entry with:

```text
Date:
Lesson:
Commit message:
Files changed:
What I learned:
Tests I ran:
Next task:
```

Important:

- Do not pretend the push log updates automatically.
- Explain that `git log` shows real commit history, while `docs/DAILY_PUSH_LOG.md` is the learning journal.
- If Mert wants to type the update himself, provide the entry text and let him paste it.
- If Mert asks Codex to update the file, update only the log entry and do not commit or push unless clearly requested.
- Keep the log text in English because it is project documentation.

## Safety Rules

Never ask the user to paste or push:

- passwords
- AWS access keys
- database passwords
- private connection strings
- `.env` files
- customer data
- production logs with sensitive data
- private company source code if policy does not allow it
- internal company URLs, account IDs, or secrets unless safely redacted

Use placeholders for sensitive examples:

```text
AWS_ACCOUNT_ID
AWS_REGION
ROLE_NAME
BUCKET_NAME
DATABASE_HOST
DATABASE_PASSWORD
```

## Current Project State

Local project folder:

```text
/Users/mertyasil/vsCodeStudy
```

GitHub repository:

```text
https://github.com/Mertjava/python-devops-journey.git
```

Main branch:

```text
main
```

Current learning position:

```text
Day 2: Lists
```

## Verification

After editing project files, run:

```bash
python3 check_course.py
```

If pytest is not installed yet, do not treat that as a blocker until Day 12/13. The project currently includes pytest files, but dependency installation is part of the learning plan.

## Learning Standard

A lesson is complete only when Mert can explain:

- what the code does
- why the tool exists
- what can fail
- how it was tested
- how it connects to real professional work

Do not make the education weak or overly easy. Keep it clear, serious, and practical.
