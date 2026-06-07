# Day 11: APIs and HTTP
# Goal: understand how Python talks to web services.
#
# Before you code:
# An API lets one program talk to another program. Many cloud tools, including
# AWS services, expose APIs. Python can call an API, receive data, and use that
# data in your automation script.
#
# Key ideas today:
# - HTTP GET asks a server for data
# - status code 200 usually means success
# - APIs often return JSON
# - requests is a popular Python library for calling APIs

# Install requests later with:
# python3 -m pip install requests
#
# This file is written so it does not require internet to understand the idea.

api_url = "https://api.github.com"

print("API URL:", api_url)
print("HTTP GET means: ask a server for data.")
print("HTTP status 200 means: success.")
print("APIs often return JSON data.")

# Example after installing requests:
#
# import requests
#
# response = requests.get(api_url)
# print(response.status_code)
# print(response.json())

# Homework:
# 1. Install requests in a virtual environment.
# 2. Call https://api.github.com.
# 3. Print the status code.
#
# Test cases:
# - Status code is 200 when internet works.
# - Program handles connection errors with try/except.
