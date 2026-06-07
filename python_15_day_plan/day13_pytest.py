# Day 13: Testing with pytest
# Goal: check code automatically.
#
# Before you code:
# Tests are small checks that prove your code works. Instead of manually trying
# the same inputs again and again, you write tests once and run them whenever
# you change the code. This is important for reliable automation.
#
# Key ideas today:
# - assert checks that something is true
# - pytest finds functions named test_...
# - tests should check both success and failure cases
# - good tests make refactoring safer

def add(a, b):
    return a + b


def can_login(username, password):
    valid_user = username == "admin" or username == "manager"
    valid_password = password == "python123"
    return valid_user and valid_password


print("Manual test add:", add(2, 3))
print("Manual test login:", can_login("admin", "python123"))

# Pytest test examples:
#
# def test_add():
#     assert add(2, 3) == 5
#
# def test_can_login_admin():
#     assert can_login("admin", "python123") is True
#
# def test_guest_cannot_login():
#     assert can_login("guest", "python123") is False

# Homework:
# 1. Create tests/test_day13.py.
# 2. Write tests for add().
# 3. Write tests for can_login().
#
# Test cases:
# - admin + python123 returns True.
# - guest + python123 returns False.
