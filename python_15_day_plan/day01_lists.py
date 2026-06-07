# Day 1: Python Basics
# Goal: learn the basic building blocks of a Python program.
#
# Before you code:
# This first file teaches the foundation. You ask the user for information,
# store answers in variables, do simple math, and make decisions with if/else.
# These basics appear in almost every real Python script.
#
# Key ideas today:
# - print() shows output in the terminal
# - input() gets information from the user
# - variables store values
# - int() converts text into a number
# - if, elif, else, and, or, not control decisions

# Lesson 1: print()
# print() shows text or values in the terminal.
print("Hello Python")


# Lesson 2: input() and variables
# input() asks the user a question.
# The answer is stored in a variable like name, city, or age.
name = input("What is your name? ")
city = input("Which city do you live in? ")

# input() gives us text, so int() converts the age into a number.
age = int(input("How old are you? "))


# Lesson 3: using variables with print()
print("Hello", name)
print(city, "is a nice city.")


# Lesson 4: math with variables
birth_year = 2026 - age


# Lesson 5: if / elif / else
# Python checks these conditions from top to bottom.
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

print("Next year you will be", age + 1, "years old.")
print("Estimated birth year:", birth_year)


# Lesson 6: basic math operators
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# Lesson 7: and / or
# This login works only when:
# - username is admin or manager
# - password is python123
username = input("Enter username: ")
password = input("Enter password: ")

if (username == "admin" or username == "manager") and password == "python123":
    print("Login Successful.")
else:
    print("Login Failed.")


# Lesson 8: not
# not changes True to False, and False to True.
is_banned = True

if not is_banned:
    print("You can access the content.")
else:
    print("You are banned from accessing the content.")
