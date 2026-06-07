# Day 8: Error Handling
# Goal: keep programs from crashing on bad input.
#
# Before you code:
# Real users make mistakes. Files can be missing. APIs can fail. A strong
# script handles problems calmly instead of crashing with a confusing error.
# Error handling lets you show a friendly message and keep control.
#
# Key ideas today:
# - try means "attempt this code"
# - except means "if this error happens, do this instead"
# - ValueError often happens when converting bad input to int
# - ZeroDivisionError happens when dividing by zero

try:
    age = int(input("Enter age: "))
    print("Next year:", age + 1)
except ValueError:
    print("Please enter a valid number.")

# Practice: safe division
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Both values must be numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Homework:
# 1. Improve one old program with try/except.
# 2. Handle bad age input.
# 3. Handle empty username input.
#
# Test cases:
# - Age "abc" -> friendly error.
# - Division by 0 -> friendly error.
