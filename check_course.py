# Course Checker
# Run this file to verify the main course files exist and have valid Python syntax.

from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "DAILY_TASKS.md",
    "REAL_WORLD_DEVOPS_PROJECT_PLAN.md",
    "docs/GIT_DAILY_PUSH_GUIDE.md",
    "docs/DAILY_PUSH_LOG.md",
    ".gitignore",
    "requirements.txt",
    "final_project/config.json",
    "final_project/devops_tool.py",
    "tests/test_final_project.py",
    "python_15_day_plan/day01_lists.py",
    "python_15_day_plan/day02_lists.py",
    "python_15_day_plan/day03_loops.py",
    "python_15_day_plan/day04_dictionaries.py",
    "python_15_day_plan/day05_functions.py",
    "python_15_day_plan/day06_strings.py",
    "python_15_day_plan/day07_files.py",
    "python_15_day_plan/day08_errors.py",
    "python_15_day_plan/day09_modules.py",
    "python_15_day_plan/day10_json.py",
    "python_15_day_plan/day11_api_requests.py",
    "python_15_day_plan/day12_virtualenv.py",
    "python_15_day_plan/day13_pytest.py",
    "python_15_day_plan/day14_cli_env.py",
    "python_15_day_plan/day15_final_review.py",
]


PYTHON_FILES = [
    "check_course.py",
    "scripts/daily_git_check.py",
    "final_project/devops_tool.py",
    "tests/test_final_project.py",
    "python_15_day_plan/day01_lists.py",
    "python_15_day_plan/day02_lists.py",
    "python_15_day_plan/day03_loops.py",
    "python_15_day_plan/day04_dictionaries.py",
    "python_15_day_plan/day05_functions.py",
    "python_15_day_plan/day06_strings.py",
    "python_15_day_plan/day07_files.py",
    "python_15_day_plan/day08_errors.py",
    "python_15_day_plan/day09_modules.py",
    "python_15_day_plan/day10_json.py",
    "python_15_day_plan/day11_api_requests.py",
    "python_15_day_plan/day12_virtualenv.py",
    "python_15_day_plan/day13_pytest.py",
    "python_15_day_plan/day14_cli_env.py",
    "python_15_day_plan/day15_final_review.py",
]


def check_required_files():
    missing_files = []

    for file_name in REQUIRED_FILES:
        if not Path(file_name).exists():
            missing_files.append(file_name)

    return missing_files


def check_python_syntax():
    errors = []

    for file_name in PYTHON_FILES:
        path = Path(file_name)
        source = path.read_text()

        try:
            compile(source, file_name, "exec")
        except SyntaxError as error:
            errors.append((file_name, error.lineno, error.msg))

    return errors


def main():
    missing_files = check_required_files()
    syntax_errors = check_python_syntax()

    if missing_files:
        print("Missing files:")
        for file_name in missing_files:
            print("-", file_name)
    else:
        print("All required files exist.")

    if syntax_errors:
        print("Syntax errors:")
        for file_name, line_number, message in syntax_errors:
            print("-", file_name, "line", line_number, message)
    else:
        print("All Python files have valid syntax.")

    if not missing_files and not syntax_errors:
        print("Course check passed.")


if __name__ == "__main__":
    main()
