# Day 4: Dictionaries
# Goal: store labeled data with key/value pairs.
#
# Before you code:
# A dictionary stores data with labels. The label is called a key, and the
# stored data is called a value. This is perfect when plain position is not
# enough. For example, a user has a username, role, and status. A server has
# a name, region, and owner.
#
# Dictionaries are very important for AWS/DevOps because JSON data from APIs
# often becomes a Python dictionary. Config files, AWS responses, and user
# settings often look like dictionaries.
#
# Key ideas today:
# - Dictionaries use curly braces: {"username": "admin"}
# - You read values with keys: user["username"]
# - You can update values, add new keys, and loop through key/value pairs
# - Dictionaries can contain other dictionaries

user = {
    "username": "admin",
    "role": "manager",
    "active": True,
}

print("Username:", user["username"])
print("Role:", user["role"])

# Update a value.
user["role"] = "devops"
print("Updated role:", user["role"])

# Add a new key.
user["environment"] = "dev"
print("Environment:", user["environment"])

# Loop over keys and values.
for key, value in user.items():
    print(key, "=", value)

# Nested data: a dictionary inside a dictionary.
server = {
    "name": "web-01",
    "metadata": {
        "region": "us-east-1",
        "owner": "mert",
    },
}

print("Server region:", server["metadata"]["region"])

# Homework:
# 1. Create a dictionary for yourself: name, city, skill_level.
# 2. Print each value.
# 3. Add a nested dictionary called contact with email and phone.
#
# Test cases:
# - Your name prints correctly.
# - Your nested email prints correctly.
