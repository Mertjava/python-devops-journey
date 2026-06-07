# Day 2: Lists
# Goal: store many values in one variable.
#
# Before you code:
# A list is like a container that keeps multiple items in order.
# Instead of creating movie1, movie2, and movie3 variables, you can keep
# all movies inside one list. In DevOps, lists are useful for server names,
# AWS regions, usernames, file paths, and tasks you want to repeat.
#
# Key ideas today:
# - Lists use square brackets: ["apple", "banana"]
# - Python starts counting from 0, so the first item is list_name[0]
# - You can add items with append()
# - You can process every item with a for loop

# Lesson 1: create a list
favorite_movies = ["Interstellar", "Inception", "The Matrix"]

# Lesson 2: indexes
# Python starts counting at 0.
print("First movie:", favorite_movies[0])
print("Second movie:", favorite_movies[1])

# Lesson 3: add and remove items
favorite_movies.append("Avatar")
print("After append:", favorite_movies)

favorite_movies.remove("Avatar")
print("After remove:", favorite_movies)

# Lesson 4: loop over a list
for movie in favorite_movies:
    print("Movie:", movie)

# Homework:
# 1. Change the list to your real 3 favorite movies.
# 2. Add one new movie with append().
# 3. Print every movie with a for loop.
#
# Test cases:
# - The first movie prints correctly.
# - The loop prints all movies.
