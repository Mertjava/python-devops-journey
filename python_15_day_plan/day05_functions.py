# Day 5: Functions
# Goal: organize reusable code.
#
# Before you code:
# A function is a named block of code that performs a job. Functions help you
# avoid repeating yourself. If your script logs in, validates data, or saves a
# file, you can put that logic inside a function and call it when needed.
#
# Key ideas today:
# - def creates a function
# - parameters are values you send into a function
# - return sends a result back from a function
# - good function names describe the job clearly

def greet_user(name):
    print("Hello", name)


def add_numbers(a, b):
    return a + b


def calculate_birth_year(age):
    return 2026 - age


greet_user("Mert")

total = add_numbers(10, 5)
print("Total:", total)

birth_year = calculate_birth_year(25)
print("Birth year:", birth_year)

# Practice: calculator with functions
def multiply(a, b):
    return a * b


print("Multiplication:", multiply(4, 3))

# Homework:
# 1. Create subtract(a, b).
# 2. Create divide(a, b).
# 3. Ask the user for two numbers and print all results.
#
# Test cases:
# - 10 and 5 -> subtract is 5.
# - 10 and 5 -> divide is 2.0.
