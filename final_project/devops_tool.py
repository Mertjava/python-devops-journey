# Final Project: DevOps Automation Tool
# This script validates a user and environment, then saves the action to JSON.

import json
from datetime import datetime


CONFIG_PATH = "final_project/config.json"
OUTPUT_PATH = "final_project/actions.json"


def load_config():
    with open(CONFIG_PATH, "r") as file:
        return json.load(file)


def is_valid_user(username, config):
    return username in config["allowed_users"]


def is_valid_environment(environment, config):
    return environment in config["allowed_environments"]


def build_action(username, environment):
    return {
        "username": username,
        "environment": environment,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }


def save_action(action):
    with open(OUTPUT_PATH, "w") as file:
        json.dump(action, file, indent=4)


def main():
    try:
        config = load_config()
    except FileNotFoundError:
        print("Config file not found.")
        return
    except json.JSONDecodeError:
        print("Config file is not valid JSON.")
        return

    username = input("Enter username: ").strip().lower()
    environment = input("Enter environment: ").strip().lower()

    if not is_valid_user(username, config):
        print("Invalid user.")
        return

    if not is_valid_environment(environment, config):
        print("Invalid environment.")
        return

    action = build_action(username, environment)
    save_action(action)
    print("Action saved.")


if __name__ == "__main__":
    main()

