import json
from typing import Dict, Any
from src.utils.helper import log_info


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load the configuration from a JSON file.
    """
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        log_info(
            f"Config file not found at {config_path}. Using default configuration.", 
            warning=True
        )
        return {"default_prefix": "?", "guilds": {}}
    except json.JSONDecodeError:
        log_info(
            f"Invalid JSON in config file {config_path}. Using default configuration.",
            error=True
        )
        return {"default_prefix": "?", "guilds": {}}


def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """
    Save the configuration to a JSON file.
    """
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        log_info(f"Failed to save config to {config_path}: {e}", error=True)
