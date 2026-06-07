# Day 9: Modules
# Goal: use Python's built-in tools.
#
# Before you code:
# A module is a file or package of code you can import and reuse. Python comes
# with many built-in modules, so you do not have to build everything yourself.
# DevOps scripts often use modules for dates, files, folders, randomness,
# command-line arguments, JSON, and operating system actions.
#
# Key ideas today:
# - import brings a module into your script
# - datetime works with dates and times
# - random creates random values
# - os helps Python interact with folders and files

import datetime
import os
import random

today = datetime.date.today()
print("Today:", today)

random_number = random.randint(1, 10)
print("Random number:", random_number)

current_folder = os.getcwd()
print("Current folder:", current_folder)

files = os.listdir(".")
print("Files:", files)

# Homework:
# 1. Print the current date and time.
# 2. Generate a random password number from 1000 to 9999.
# 3. Print all files in the current folder.
#
# Test cases:
# - Random number is between 1000 and 9999.
# - Current folder prints without error.
