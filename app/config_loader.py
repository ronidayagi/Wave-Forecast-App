import json
from pathlib import Path


def load_user_config():
    """Load user preferences from config file"""
    config_path = Path("app/user_config.json")

    if not config_path.exists():
        raise FileNotFoundError("user_config.json not found!")

    with open(config_path, "r") as f:
        return json.load(f)


def get_user_email():
    """Get user's notification email"""
    config = load_user_config()
    return config["user"]["email"]


def get_locations():
    """Get all configured locations"""
    config = load_user_config()
    return config["locations"]

