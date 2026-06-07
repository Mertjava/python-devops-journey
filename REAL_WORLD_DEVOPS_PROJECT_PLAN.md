# Real-World Python + Docker + SQL + AWS + Azure DevOps Plan

This plan starts after the 15-day Python course.

Goal: become strong enough to work confidently on real professional backend/devops tasks, understand the tools used at work, and explain the full system clearly.

Important truth: this is not an easy beginner plan. The goal is to move from "I use these tools but do not fully understand them" to "I understand how the pieces connect and can build/debug/deploy a real system."

## Final Project

Project name: Cloud Task Manager

What it will do:

- Users can create, read, update, and delete tasks.
- Tasks are stored in a SQL database.
- The app runs locally with Docker.
- The app connects to a cloud database on AWS.
- Files or reports can be uploaded to S3.
- Git is used with branches and pull requests.
- Azure DevOps runs tests and builds the app.
- Pipeline connects to AWS for deployment.
- Codex/Copilot are used as pair-programming tools, not as magic shortcuts.

## Main Technologies

- Python
- FastAPI
- SQL
- PostgreSQL
- Docker
- Docker Compose
- Git
- Azure DevOps
- AWS RDS
- AWS S3
- AWS IAM
- Basic frontend or API testing UI
- Pytest
- Environment variables
- CI/CD pipelines

## Architecture

Basic flow:

```text
User / Frontend / API Client
        |
        v
Python FastAPI Backend
        |
        +--> PostgreSQL Database
        |
        +--> AWS S3
        |
        +--> Logs / Config / Environment Variables
```

Development and deployment flow:

```text
Developer writes code
        |
        v
Git commit + branch
        |
        v
Azure DevOps Pipeline
        |
        +--> run tests
        +--> build Docker image
        +--> connect to AWS
        +--> deploy application
```

## 12-Week Plan

| Week | Main Focus | What You Must Be Able To Explain |
|---|---|---|
| 1 | Python review for real projects | functions, modules, files, errors, JSON, tests |
| 2 | SQL fundamentals | tables, rows, columns, CRUD, joins, indexes basics |
| 3 | FastAPI basics | routes, request/response, validation, status codes |
| 4 | Database integration | connecting Python to PostgreSQL, CRUD with database |
| 5 | Docker fundamentals | image, container, Dockerfile, why Docker exists |
| 6 | Docker Compose | running app + database locally together |
| 7 | AWS foundations | IAM, RDS, S3, security groups, environment variables |
| 8 | AWS integration | app connects to RDS and uploads to S3 |
| 9 | Git workflow | branch, commit, PR, merge, conflict basics |
| 10 | Azure DevOps pipelines | YAML pipeline, tests, build steps, artifacts |
| 11 | CI/CD to AWS | pipeline builds Docker image and deploys to AWS |
| 12 | Final hardening | tests, docs, debugging, architecture explanation |

## Weekly Structure

Each week has:

- 2 concept sessions
- 2 coding sessions
- 1 debugging/review session
- 1 written explanation from you
- 1 Codex review

The written explanation matters. If you cannot explain a topic simply, we will not count it as learned.

## Daily Structure

Each study day:

1. Learn one concept.
2. Code one small piece.
3. Break it on purpose.
4. Debug it.
5. Add a test or test case.
6. Explain what happened in your own words.

## Senior-Level Learning Rules

- Do not only copy working code.
- Always ask: why does this exist?
- Always ask: what breaks if this is wrong?
- Always test at least one success case and one failure case.
- Always learn the error messages.
- Always connect the tool to the real workflow.
- If Docker is used, explain what is inside the container.
- If AWS is used, explain credentials, network access, and security.
- If a pipeline is used, explain every step in order.
- If Codex writes code, you must be able to explain the code before accepting it.

## How We Will Use Codex/Copilot

Good prompts:

- Explain this file like I am a junior developer.
- Show the data flow from API request to database.
- Give me 3 test cases for this function.
- Review this Dockerfile for mistakes.
- Explain this Azure DevOps pipeline step by step.
- What could fail in this AWS connection?
- Ask me questions to check if I really understand this.

Bad usage:

- Write everything for me and I will not read it.
- Fix the error without explaining it.
- Generate a whole project before I understand the pieces.
- Skip tests.

## Success Criteria

By the end of this project, you should be able to:

- Build a Python API from scratch.
- Connect Python to a SQL database.
- Explain Docker images and containers.
- Run a local app with Docker Compose.
- Explain how an app connects to AWS RDS.
- Upload or read files from AWS S3.
- Use Git branches and pull requests confidently.
- Read and explain an Azure DevOps pipeline.
- Understand how CI/CD connects code to deployment.
- Use Codex/Copilot as a serious engineering assistant.
- Debug common problems instead of freezing.

## Start Condition

Do not start this big project until the 15-day Python course is complete.

Current next step:

```bash
python3 python_15_day_plan/day02_lists.py
```

