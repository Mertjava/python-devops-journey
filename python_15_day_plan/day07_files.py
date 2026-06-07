# Day 7: Files
# Goal: save and read data from files.
#
# Before you code:
# Programs become more useful when they can remember information. Files let
# your script save data and read it later. In DevOps, scripts often read config
# files, write logs, save reports, or create temporary output files.
#
# Key ideas today:
# - "w" writes a file and replaces old content
# - "a" appends new content to the end
# - "r" reads existing content
# - with open(...) closes the file automatically

file_path = "user_data.txt"

# Write creates or replaces a file.
with open(file_path, "w") as file:
    file.write("name=Mert\n")
    file.write("city=Samsun\n")

# Append adds to the end.
with open(file_path, "a") as file:
    file.write("skill=python\n")

# Read loads file content.
with open(file_path, "r") as file:
    content = file.read()

print(content)

# Homework:
# 1. Ask the user for name and city.
# 2. Save both to user_data.txt.
# 3. Read the file and print it.
#
# Test cases:
# - File contains the entered name.
# - File contains the entered city.
