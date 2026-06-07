# Daily Git Push Guide

Use this guide every day after finishing your Python lesson.

The goal is not only to upload code. The goal is to understand what changed,
commit it clearly, and build a visible daily learning history on GitHub.

## One-Time Setup

Run these commands only once after creating the GitHub repository.

```bash
git init
git config user.name "Mertjava"
git config user.email "YOUR_GITHUB_EMAIL"
git remote add origin https://github.com/Mertjava/python-devops-journey.git
git branch -M main
```

Use your GitHub no-reply email if you want privacy.

## Daily Push Flow

Run this before committing:

```bash
python3 check_course.py
python3 scripts/daily_git_check.py
```

Then stage, commit, and push:

```bash
git status
git add .
git status
git commit -m "Complete day 2 lists lesson"
git push -u origin main
```

After the first push, daily push is shorter:

```bash
git add .
git commit -m "Complete day 3 loops lesson"
git push
```

## What To Check Before Pushing

Before every push, ask:

- Did I finish today's lesson task?
- Did I run the file?
- Did I test at least two cases?
- Did I avoid pushing secrets?
- Did I understand every file I changed?
- Is my commit message clear?

## Good Commit Messages

Use messages that explain the learning progress:

```text
Complete day 2 lists lesson
Practice day 3 loops and guessing game
Add dictionary examples for day 4
Finish JSON save and load exercise
Add final project config validation
```

Avoid vague messages:

```text
update
fix
new stuff
asdf
```

## How To Explain What You Pushed

After each push, write one short entry in:

```text
docs/DAILY_PUSH_LOG.md
```

Use this format:

```text
Date:
Lesson:
Commit message:
Files changed:
What I learned:
Tests I ran:
Next task:
```


## Experience Notes

Longer learning notes are stored here:

```text
docs/experience/
```

First Git/GitHub setup note:

```text
docs/experience/git_github_first_push_experience.md
```


## For Future Codex Sessions

If a new Codex chat starts, read this first:

```text
docs/START_HERE_FOR_CODEX.md
```

Then read:

```text
docs/DAILY_PUSH_LOG.md
docs/experience/git_github_first_push_experience.md
```

The user wants to type Git commands himself. Guide him step by step and explain why each command is needed.

## Important Safety Rule

Never push:

- passwords
- AWS access keys
- database passwords
- `.env` files
- private company code
- private company database details

