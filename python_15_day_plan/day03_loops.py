# Day 3: Loops
# Goal: repeat work without copying code.
#
# Before you code:
# A loop tells Python to repeat an action. This is one of the most useful
# ideas in automation. If you have 10 servers, 20 files, or 50 users, you do
# not want to write the same code again and again.
#
# Key ideas today:
# - for loops are good when you know what you want to loop through
# - while loops keep going while a condition is true
# - break stops a loop early
# - continue skips the current loop step and moves to the next one

# Lesson 1: for loop with range()
for number in range(1, 6):
    print("For loop number:", number)

# Lesson 2: while loop
count = 1

while count <= 5:
    print("While loop count:", count)
    count = count + 1

# Lesson 3: break
for number in range(1, 10):
    if number == 4:
        break
    print("Before break:", number)

# Lesson 4: continue
for number in range(1, 6):
    if number == 3:
        continue
    print("Skipping 3:", number)

# Practice: number guessing game starter
secret_number = 7
guess = int(input("Guess the number: "))

if guess == secret_number:
    print("Correct!")
else:
    print("Try again.")

# Homework:
# 1. Use a while loop to keep asking until the guess is correct.
# 2. Use break when the user guesses correctly.
#
# Test cases:
# - Guess 7 -> Correct!
# - Guess 3, then 7 -> asks again, then succeeds.
