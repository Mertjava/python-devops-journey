# Start Here For Codex

This file gives future Codex sessions the context needed to continue the learning journey without starting from zero.

## Who The User Is

The user is Mert, GitHub username `Mertjava`.

He is an associate developer at Symetra. At work, he is around tools like Python, Docker, SQL, AWS, Git, Azure DevOps, and some frontend technologies. He wants to understand these tools deeply, not only copy commands.

The long-term goal is to become strong and senior-minded in these topics through serious practice.

## Communication Style

Use Turkish for conversation unless the user asks otherwise.

Use English for anything code-related:

- code comments
- commit messages
- documentation content
- file names
- variable names
- test names
- project text

Explain every terminal/Git step with this structure:

```text
1. What are we doing?
2. Why are we doing it?
3. What command should the user run?
4. What output should the user expect?
5. What does an error mean if it appears?
```

Do not rush. The user wants to learn the reason behind each command.

## Important User Preference

For Git/GitHub terminal work, guide the user instead of doing everything automatically.

The user wants to type Git commands himself to learn.

Good behavior:

- suggest the next command
- explain why it is needed
- ask the user to paste the output
- review the output
- then give the next step

Avoid doing commits or pushes automatically unless the user clearly asks for it.

## Current Project

Local folder:

```text
/Users/mertyasil/vsCodeStudy
```

GitHub repository:

```text
https://github.com/Mertjava/python-devops-journey.git
```

Branch:

```text
main
```

Git identity for this repo:

```text
user.name: Mertjava
user.email: 59204143+Mertjava@users.noreply.github.com
```

Reason for no-reply email:

- keeps the real Gmail address private
- still connects commits to the GitHub account

## Learning Plan

The user is currently focused on the 15-day Python course.

Primary tracker:

```text
DAILY_TASKS.md
```

Python lesson files:

```text
python_15_day_plan/
```

Current learning position:

```text
Day 2: Lists
```

After the 15-day Python plan, continue with:

```text
REAL_WORLD_DEVOPS_PROJECT_PLAN.md
```

That plan covers Python, Docker, SQL, AWS, Git, Azure DevOps, testing, and Codex/Copilot workflow through a larger project.

## Daily Git Documentation

Daily Git guide:

```text
docs/GIT_DAILY_PUSH_GUIDE.md
```

Daily push log:

```text
docs/DAILY_PUSH_LOG.md
```

First Git/GitHub experience note:

```text
docs/experience/git_github_first_push_experience.md
```

Before any daily commit, run:

```bash
python3 check_course.py
python3 scripts/daily_git_check.py
git status
```

Daily commit style:

```text
Complete day 2 lists lesson
Practice day 3 loops and guessing game
Add dictionary examples for day 4
```

Avoid vague commit messages like:

```text
update
fix
new stuff
```

## Safety Rules

Never push or ask the user to push:

- passwords
- AWS access keys
- database passwords
- `.env` files
- company source code
- company database details

The project has `.gitignore`, but still remind the user to think before pushing.

## How To Continue A New Session

When a future Codex session starts, read these files first:

```text
README.md
DAILY_TASKS.md
docs/START_HERE_FOR_CODEX.md
docs/GIT_DAILY_PUSH_GUIDE.md
docs/CODEX_AGENT_GUIDELINES.md
docs/DAILY_PUSH_LOG.md
```

Then ask the user what they completed today or inspect the current Git status if they ask for a check.

## Teaching Standard

The user explicitly said the education should not be weak or easy.

Teach seriously:

- explain concepts deeply but clearly
- require test cases
- require the user to explain what they learned
- connect basics to real professional workflow
- debug errors instead of skipping them
- make the user type and think, not just copy
