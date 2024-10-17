import discord
from src.utils.helper import *


def load_config(config_path: str = "config.json") -> dict:
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"WARNING: Config file not found at {config_path}. Using default configuration.")
        return {"default_prefix": "?", "guilds": {}}
    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON in config file {config_path}. Using default configuration.")
        return {"default_prefix": "?", "guilds": {}}

def save_config(config: dict, config_path: str = "config.json") -> None:
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"ERROR: Failed to save config to {config_path}: {e}")

class ColorManager:
    def __init__(self, config: dict):
        self.colors = config.get("colors", {})

    def get_color(self, color_name: str) -> int:
        if color_name not in self.colors:
            raise ValueError(f"Color '{color_name}' not found in configuration")
        return int(self.colors[color_name].lstrip("#"), 16)

    def list_colors(self) -> list:
        return list(self.colors.keys())

    def create_color_embed(self, title: str, description: str, color_name: str) -> discord.Embed:
        try:
            color = self.get_color(color_name)
            return discord.Embed(title=title, description=description, color=color)
        except ValueError as e:
            print(f"ERROR: Failed to create color embed: {e}")
            return discord.Embed(title=title, description=description)