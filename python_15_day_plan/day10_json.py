# Day 10: JSON
# Goal: save structured data like dictionaries and lists.
#
# Before you code:
# JSON is a text format for structured data. It looks very similar to Python
# dictionaries and lists. APIs, AWS responses, config files, and many DevOps
# tools use JSON, so this is a major skill for automation.
#
# Key ideas today:
# - json.dump() saves Python data into a JSON file
# - json.load() reads JSON back into Python
# - indent=4 makes the saved file easier to read
# - JSON is great for config, reports, and saved user data

import json

user = {
    "username": "admin",
    "role": "devops",
    "environments": ["dev", "test", "prod"],
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

with open("user.json", "r") as file:
    loaded_user = json.load(file)

print("Loaded username:", loaded_user["username"])
print("Environments:", loaded_user["environments"])

# Homework:
# 1. Ask for username and role.
# 2. Save them into user.json.
# 3. Load user.json and print the data.
#
# Test cases:
# - Saved username loads correctly.
# - Saved role loads correctly.
