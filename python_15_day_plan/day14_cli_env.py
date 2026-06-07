# Day 14: CLI Args and Environment Variables
# Goal: make scripts useful for DevOps automation.
#
# Before you code:
# DevOps scripts often run from the terminal, CI/CD pipelines, or scheduled
# jobs. Command-line arguments and environment variables let you change script
# behavior without editing the code.
#
# Key ideas today:
# - sys.argv reads command-line arguments
# - os.getenv() reads environment variables
# - defaults help scripts work even when values are missing
# - this pattern is common in deployment and automation tools

import os
import sys

print("Script name:", sys.argv[0])

if len(sys.argv) > 1:
    environment = sys.argv[1]
else:
    environment = "dev"

owner = os.getenv("OWNER", "unknown")

print("Environment:", environment)
print("Owner:", owner)

# Try:
# OWNER=mert python3 python_15_day_plan/day14_cli_env.py prod

# Homework:
# 1. Accept environment from command-line args.
# 2. Accept owner from an environment variable.
# 3. Print a deployment message.
#
# Test cases:
# - prod argument prints prod.
# - missing argument defaults to dev.
