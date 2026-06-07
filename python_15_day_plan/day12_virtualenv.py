# Day 12: Virtual Environments and pip
# Goal: keep project packages organized.
#
# Before you code:
# A virtual environment is a private Python workspace for one project. It keeps
# installed packages separate from other projects. This matters in real work
# because different projects may need different package versions.
#
# Key ideas today:
# - venv creates an isolated environment
# - pip installs packages
# - requirements.txt records what the project needs
# - activate the environment before installing or running project packages

# Terminal commands to practice:
#
# Create a virtual environment:
# python3 -m venv .venv
#
# Activate it on macOS:
# source .venv/bin/activate
#
# Install a package:
# python3 -m pip install requests
#
# Save dependencies:
# python3 -m pip freeze > requirements.txt
#
# Install dependencies later:
# python3 -m pip install -r requirements.txt

print("Virtual environments keep project packages separate.")
print("pip installs Python packages.")
print("requirements.txt records project dependencies.")

# Homework:
# 1. Create a virtual environment.
# 2. Activate it.
# 3. Install requests.
# 4. Create requirements.txt.
#
# Test cases:
# - python3 -m pip show requests works inside the environment.
# - requirements.txt contains requests.
