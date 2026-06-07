# Git and GitHub First Push Experience

Date: 2026-06-06

This note documents how we connected this local learning project to GitHub from zero. It is not only a command list. It explains why each step matters.

## 1. Repository Goal

We created a GitHub repository named:

```text
python-devops-journey
```

Why:

- keep daily Python and DevOps learning visible
- build a professional GitHub history
- practice real developer workflow
- separate this learning project from old repositories

## 2. Folder Name Lesson

The original folder name had a space:

```text
vsCode study
```

In the terminal, spaces separate command arguments. This can confuse commands.

Example:

```bash
cd /Users/mertyasil/vsCode study
```

The terminal reads that like two pieces:

```text
/Users/mertyasil/vsCode
study
```

Correct ways:

```bash
cd "/Users/mertyasil/vsCode study"
```

or:

```bash
cd /Users/mertyasil/vsCode\ study
```

We renamed the folder to:

```text
vsCodeStudy
```

Now the command is simpler:

```bash
cd /Users/mertyasil/vsCodeStudy
```

## 3. Initialize Git

Command:

```bash
git init
```

What it does:

```text
Turns the current folder into a Git repository.
```

Why:

Git needs a hidden `.git` folder to track file history. This does not upload anything to GitHub yet. It only starts local version control.

Expected result:

```text
Initialized empty Git repository...
```

## 4. Check Status

Command:

```bash
git status
```

What it does:

Shows the current Git state.

Important words:

```text
No commits yet
```

Means no permanent Git snapshot exists yet.

```text
Untracked files
```

Means Git can see the files, but they are not staged or committed yet.

## 5. Configure Git Identity

Commands:

```bash
git config user.name "Mertjava"
git config user.email "59204143+Mertjava@users.noreply.github.com"
```

What this does:

Sets the author name and email for commits in this project.

Why:

Every commit stores:

- author name
- author email
- commit message
- changed files
- date and time

We used the GitHub no-reply email because it keeps the real Gmail address private while still linking commits to the GitHub account.

Check commands:

```bash
git config user.name
git config user.email
```

Expected output:

```text
Mertjava
59204143+Mertjava@users.noreply.github.com
```

## 6. Connect Local Repo To GitHub

Command:

```bash
git remote add origin https://github.com/Mertjava/python-devops-journey.git
```

What it does:

Connects the local Git repository to the GitHub repository.

Why:

Before this step, Git can track local history but does not know where to push it online.

Check command:

```bash
git remote -v
```

Expected output:

```text
origin  https://github.com/Mertjava/python-devops-journey.git (fetch)
origin  https://github.com/Mertjava/python-devops-journey.git (push)
```

Meaning:

- `fetch` means Git can get updates from GitHub
- `push` means Git can send commits to GitHub

If you run `git remote add origin ...` twice, this error is normal:

```text
error: remote origin already exists.
```

It means the remote is already connected.

## 7. Staging With git add

Git has three important local states:

```text
Working directory -> Staging area -> Commit
```

Meaning:

- working directory: files you are editing
- staging area: files selected for the next commit
- commit: permanent snapshot in Git history

Stage one file:

```bash
git add README.md
```

Stage many files:

```bash
git add .
```

Important lesson:

We intentionally did not stage `python_15_day_plan/day01_lists.py` in the first commit because we wanted Day 1 to be a separate learning commit.

If a file is staged by mistake:

```bash
git restore --staged path/to/file.py
```

## 8. First Commit

Command:

```bash
git commit -m "Start Python DevOps learning journey"
```

What it does:

Creates the first permanent snapshot of the staged files.

Why this commit message is good:

It explains the purpose of the commit clearly.

Good commit messages:

```text
Start Python DevOps learning journey
Complete day 1 Python basics lesson
Complete day 2 lists lesson
Practice day 3 loops
```

Bad commit messages:

```text
update
fix
asdf
new stuff
```

## 9. First Push

Command:

```bash
git push -u origin main
```

What it does:

Uploads local commits to GitHub.

Why `-u origin main`:

It teaches Git that the local `main` branch should push to `origin/main`. After that, daily push can usually be:

```bash
git push
```

## 10. Separate Day 1 Commit

Command flow:

```bash
git status
git add python_15_day_plan/day01_lists.py
git status
git commit -m "Complete day 1 Python basics lesson"
git push
```

Why:

This creates a clean learning history:

```text
Commit 1: project setup
Commit 2: Day 1 lesson completed
```

That is better than one messy commit containing everything.

## 11. Daily Git Workflow

Use this every study day:

```bash
python3 check_course.py
python3 scripts/daily_git_check.py
git status
git add .
git status
git commit -m "Complete day X lesson name"
git push
```

Then update:

```text
docs/DAILY_PUSH_LOG.md
```

## 12. Safety Rules

Never push:

- passwords
- AWS keys
- database passwords
- `.env` files
- company source code
- company database connection details

Before pushing, always ask:

```text
Do I understand what I am pushing?
Could this expose private information?
Is my commit message meaningful?
Did I run at least one check?
```

## 13. What We Learned

Today we learned:

- how Git tracks a project locally
- why folder names with spaces can be annoying in terminal
- how to initialize a repository
- how to check repository status
- how to configure Git identity
- why GitHub no-reply email is useful
- how to connect local Git to GitHub with remote origin
- how staging works
- why clean commit history matters
- how to push daily progress to GitHub

This is a real developer habit, not just a Git command exercise.
