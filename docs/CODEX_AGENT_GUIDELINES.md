# Codex Agent Working Guidelines

This document explains how Mert should work with Codex/Copilot-style agents while learning and while working near professional systems.

The goal is not to let the agent replace understanding. The goal is to use the agent as a serious engineering partner.

## 1. Core Principle

Use Codex as a pair programmer, reviewer, explainer, and debugging partner.

Do not use Codex as a magic tool that writes code you do not understand.

Before accepting agent output, Mert should be able to explain:

- what changed
- why it changed
- what could break
- how it was tested
- what assumptions were made

## 2. Communication Style

Conversation can be Turkish.

Code-related output should be English:

- code comments
- variable names
- function names
- commit messages
- documentation
- test names
- terminal command explanations inside docs

When teaching terminal or Git commands, Codex should explain:

```text
1. What are we doing?
2. Why are we doing it?
3. What command should Mert run?
4. What output should Mert expect?
5. What does an error mean if it appears?
```

## 3. How To Ask Codex Good Questions

Good prompts:

```text
Explain this file like I am an associate developer.
Review this function for bugs and missing tests.
Explain the data flow from API request to database.
Give me test cases before changing the code.
What can fail in this Dockerfile?
Explain this Azure DevOps pipeline step by step.
What AWS permissions does this script need?
Help me debug this error, but do not fix it until I understand it.
```

Weak prompts:

```text
Fix everything.
Write the whole project.
Make it work.
Do it for me.
```

Better version:

```text
Here is the error and what I expected. Explain the likely cause, show me how to verify it, then suggest a minimal fix.
```

## 4. Company Code And Security Rules

When using Codex near company work, follow company policy first.

Never paste or upload:

- passwords
- AWS access keys
- database passwords
- private connection strings
- `.env` files
- customer data
- production logs with sensitive data
- private company source code if company policy does not allow it
- internal URLs, account IDs, or secrets unless they are safely redacted

Use redacted examples:

```text
postgres://USER:PASSWORD@HOST:5432/DB_NAME
```

Instead of real values.

For AWS examples, use placeholders:

```text
AWS_ACCOUNT_ID
AWS_REGION
ROLE_NAME
BUCKET_NAME
DATABASE_HOST
```

## 5. AWS Guidance Rules

When asking Codex about AWS, include:

- service name, such as RDS, S3, ECS, Lambda, IAM
- environment, such as local, dev, test, prod
- what the app is trying to do
- what error appears
- what permissions are expected

Codex should help Mert understand:

- authentication
- IAM permissions
- network access
- security groups
- environment variables
- region configuration
- failure modes

Important AWS questions:

```text
Which IAM permission is needed?
Is this a credentials problem or network problem?
Could this expose secrets?
Is this safe for production?
What should be different between local/dev/prod?
```

## 6. Database Guidance Rules

When asking Codex about database work, describe:

- database type, such as PostgreSQL, SQL Server, MySQL
- connection method
- table shape or simplified schema
- expected query result
- actual error

Do not share real production credentials or customer data.

Codex should help check:

- SQL correctness
- joins
- indexes basics
- transaction behavior
- input validation
- connection errors
- environment-specific config

Good database prompt:

```text
Here is a simplified schema and query. Explain what the query does, what can go wrong, and how to test it.
```

## 7. Docker Guidance Rules

When asking Codex about Docker, include:

- Dockerfile
- docker-compose.yml if used
- command that failed
- error output
- expected behavior

Codex should explain:

- image vs container
- build vs run
- ports
- volumes
- environment variables
- container networking
- why Docker is useful

Important Docker questions:

```text
What is inside this image?
Which command runs when the container starts?
What files are copied into the image?
Which port is exposed?
How does this container reach the database?
```

## 8. Azure DevOps Pipeline Guidance Rules

When asking Codex about ADO pipelines, include:

- YAML pipeline file
- trigger behavior
- build steps
- test steps
- deploy target
- error message

Codex should explain the pipeline in order:

```text
trigger -> checkout -> setup -> install -> test -> build -> publish -> deploy
```

Important pipeline questions:

```text
What starts this pipeline?
What does each step do?
Where are secrets stored?
How does this connect to AWS?
What happens if tests fail?
What artifact or Docker image is produced?
```

## 9. Git And GitHub Rules

For Git commands, Mert wants to type commands himself.

Codex should:

- explain the command
- ask Mert to run it
- review the output
- then give the next step

Do not automatically commit or push unless Mert clearly asks for it.

Daily Git flow:

```bash
python3 check_course.py
python3 scripts/daily_git_check.py
git status
git add .
git status
git commit -m "Complete day X lesson name"
git push
```

Commit messages should be specific:

```text
Complete day 2 lists lesson
Add GitHub first push experience notes
Practice Docker Compose database setup
```

## 10. How To Review Agent Output

Before accepting agent output, ask:

```text
Do I understand this?
Is the change minimal?
Did it touch unrelated files?
Are there tests?
Did it expose secrets?
Can I explain it to a teammate?
```

If not, ask Codex:

```text
Explain this change line by line.
What assumptions did you make?
What are the risks?
How can I test this?
Make the solution smaller.
```

## 11. Debugging Workflow With Codex

Use this order:

1. Paste the exact error.
2. Explain what you expected.
3. Explain what command you ran.
4. Ask Codex for likely causes.
5. Verify one cause at a time.
6. Apply the smallest fix.
7. Run tests again.
8. Document what was learned.

Good debugging prompt:

```text
I ran this command and got this error. Explain the error, give me 2-3 likely causes, and tell me the first command to verify the most likely cause.
```

## 12. Learning Standard

The learning path should be serious, not shallow.

Codex should regularly ask Mert to explain:

- what the code does
- why the tool exists
- what can fail
- how to test it
- how this appears in real work

A lesson is not complete only because code runs.

A lesson is complete when Mert can explain the concept and test it.

## 13. Personal Project Rule

This repository is for personal learning:

```text
python-devops-journey
```

It should not contain company code or company secrets.

It can contain simplified examples that teach the same concepts safely.

## 14. Future Codex Session Reminder

A new Codex session should read:

```text
docs/START_HERE_FOR_CODEX.md
docs/CODEX_AGENT_GUIDELINES.md
DAILY_TASKS.md
docs/DAILY_PUSH_LOG.md
```

Then continue from the current lesson or Git task.
