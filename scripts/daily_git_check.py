# Daily Git Check
# Run this before and after committing to understand what changed.

import subprocess


def run_git(args):
    result = subprocess.run(
        ["git"] + args,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def print_section(title):
    print()
    print("=" * len(title))
    print(title)
    print("=" * len(title))


def print_output(output, empty_message):
    if output:
        print(output)
    else:
        print(empty_message)


def is_git_repo():
    code, _, _ = run_git(["rev-parse", "--is-inside-work-tree"])
    return code == 0


def show_setup_help():
    print("This folder is not a Git repository yet.")
    print()
    print("Run these commands after creating the GitHub repo:")
    print('git init')
    print('git config user.name "Mertjava"')
    print('git config user.email "YOUR_GITHUB_EMAIL"')
    print("git remote add origin https://github.com/Mertjava/python-devops-journey.git")
    print("git branch -M main")


def main():
    if not is_git_repo():
        show_setup_help()
        return

    print_section("Current Branch And Status")
    _, output, _ = run_git(["status", "--short", "--branch"])
    print_output(output, "Working tree is clean.")

    print_section("Staged Changes")
    _, output, _ = run_git(["diff", "--cached", "--name-status"])
    print_output(output, "No staged changes.")

    print_section("Unstaged Changes")
    _, output, _ = run_git(["diff", "--name-status"])
    print_output(output, "No unstaged changes.")

    print_section("Untracked Files")
    _, output, _ = run_git(["ls-files", "--others", "--exclude-standard"])
    print_output(output, "No untracked files.")

    print_section("Last Commit")
    code, output, _ = run_git(["log", "-1", "--pretty=format:%h %s"])
    if code == 0:
        print_output(output, "No commits yet.")
    else:
        print("No commits yet.")

    print_section("Files In Last Commit")
    code, output, _ = run_git(["show", "--name-status", "--format=", "--no-renames", "HEAD"])
    if code == 0:
        print_output(output, "No files found in last commit.")
    else:
        print("No commit exists yet.")

    print_section("Remote")
    _, output, _ = run_git(["remote", "-v"])
    print_output(output, "No remote connected yet.")

    print()
    print("Daily reminder:")
    print("- Run: python3 check_course.py")
    print("- Review changed files before commit.")
    print("- Use a clear commit message.")
    print("- Do not push secrets or company code.")


if __name__ == "__main__":
    main()

