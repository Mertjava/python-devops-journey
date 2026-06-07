from final_project.devops_tool import (
    build_action,
    is_valid_environment,
    is_valid_user,
)


def test_valid_user():
    config = {"allowed_users": ["admin", "manager"]}
    assert is_valid_user("admin", config) is True


def test_invalid_user():
    config = {"allowed_users": ["admin", "manager"]}
    assert is_valid_user("guest", config) is False


def test_valid_environment():
    config = {"allowed_environments": ["dev", "test", "prod"]}
    assert is_valid_environment("prod", config) is True


def test_build_action():
    action = build_action("admin", "dev")
    assert action["username"] == "admin"
    assert action["environment"] == "dev"
    assert "created_at" in action

