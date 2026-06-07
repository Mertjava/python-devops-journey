# Day 6: Strings
# Goal: clean and transform text.
#
# Before you code:
# A string is text. Usernames, emails, passwords, file names, log lines,
# environment names, and API responses all contain strings. DevOps scripts
# often need to clean text before using it.
#
# Key ideas today:
# - strip() removes extra spaces from the beginning and end
# - lower() makes text lowercase
# - split() breaks text into a list of words
# - slicing lets you take part of a string, like text[:5]

message = "  Hello Python DevOps  "

print("Original:", message)
print("Strip:", message.strip())
print("Lower:", message.lower())
print("Upper:", message.upper())

clean_message = message.strip().lower()
print("Clean message:", clean_message)

words = clean_message.split()
print("Words:", words)

print("First 5 characters:", clean_message[:5])

# Practice: normalize username input
username = input("Enter username: ")
username = username.strip().lower()

print("Normalized username:", username)

# Homework:
# 1. Ask for an email.
# 2. Strip spaces.
# 3. Lowercase it.
# 4. Print the cleaned email.
#
# Test cases:
# - " TEST@EMAIL.COM " -> "test@email.com"
# - " mert@example.com" -> "mert@example.com"
