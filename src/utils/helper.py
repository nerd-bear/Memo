from rich import print as richPrint
import json
import datetime
import discord
import aiohttp
import requests
import ssl
import os
import urllib3
from discord.ext import commands
import tempfile
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
from gtts import gTTS
import hashlib


class SHA3:
    @staticmethod
    def salt_hash(input_str: str, salt: bytes = None) -> tuple:
        if salt is None:
            salt = SHA3.generate_salt(size=32, hex=True)
        encoded_str = input_str.encode("utf-8")
        hashed = hashlib.pbkdf2_hmac("sha256", encoded_str, salt, 100000)
        return salt, hashed

    @staticmethod
    def hash_256(input_str: str) -> str:
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_256(encoded_str).hexdigest()

    @staticmethod
    def hash_384(input_str: str) -> str:
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_384(encoded_str).hexdigest()

    @staticmethod
    def hash_512(input_str: str) -> str:
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_512(encoded_str).hexdigest()

    @staticmethod
    def hash_224(input_str: str) -> str:
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_224(encoded_str).hexdigest()

    @staticmethod
    def generate_salt(size: int = 32, hex: bool = True) -> bytes:
        salt = os.urandom(size).hex() if hex else os.urandom(size)
        return salt

    @staticmethod
    def compare_hash_to_salted(
        stored_salt: bytes, salted_and_hashed: bytes, hashed: str
    ) -> bool:
        _, new_hash = SHA3.salt_hash(hashed, stored_salt)
        return new_hash == salted_and_hashed


def set_langdetect_seed(seed: int = 0):
    """
    Set the seed for language detection to ensure consistent results.

    Args:
        seed (int): The seed value for language detection. Defaults to 0.
    """
    DetectorFactory.seed = seed


def text_to_speech(text: str, output_file: str, tts_mode: str) -> None:
    """
    Convert text to speech and save it to a file.

    Args:
        text (str): The text to convert to speech.
        output_file (str): The path to save the output audio file.
        tts_mode (str): The speed mode for text-to-speech conversion ('slow' or 'normal').

    Raises:
        Exception: If an error occurs during the text-to-speech conversion.
    """
    try:
        slow = tts_mode.lower() == "slow"

        # Detect the language of the input text
        language = detect(text)

        # Create and save the text-to-speech audio
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(output_file)
    except Exception as e:
        richPrint(f"ERROR_LOG ~ Text-to-speech conversion failed: {e}")
        # Consider re-raising the exception or returning a status code


def load_config(config_path: str = "config.json") -> dict:
    """
    Load the configuration from a JSON file.

    Args:
        config_path (str): The path to the configuration file. Defaults to "config.json".

    Returns:
        dict: The loaded configuration or a default configuration if the file is not found.
    """
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        richPrint(
            f"WARNING: Config file not found at {config_path}. Using default configuration."
        )
        return {"default_prefix": "?", "guilds": {}}
    except json.JSONDecodeError:
        richPrint(
            f"ERROR: Invalid JSON in config file {config_path}. Using default configuration."
        )
        return {"default_prefix": "?", "guilds": {}}


def save_config(config: dict, config_path: str = "config.json") -> None:
    """
    Save the configuration to a JSON file.

    Args:
        config (dict): The configuration to save.
        config_path (str): The path to save the configuration file. Defaults to "config.json".
    """
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        richPrint(f"ERROR: Failed to save config to {config_path}: {e}")


def log_info(value: str = "None") -> None:
    """
    Log an information message with a timestamp.

    Args:
        value (str): The message to log. Defaults to "None".
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp, end=" ")
    richPrint(f"[bold][blue]INFO[/blue][/bold]     {value}")


def fetch_latency(client: commands.Bot, shouldRound: bool = True) -> float:
    """
    Fetch the latency of the Discord client.

    Args:
        client (commands.Bot): The Discord client.
        shouldRound (bool): Whether to round the latency. Defaults to True.

    Returns:
        float: The latency in milliseconds.
    """
    latency = client.latency * 1000
    return round(latency) if shouldRound else latency


def get_char_image(
    char: str, bg: str = "white", fg: str = "black", format: str = "png"
) -> str:
    """
    Generate an image of a single character.

    Args:
        char (str): The character to render in the image.
        bg (str): The background color. Defaults to "white".
        fg (str): The foreground color. Defaults to "black".
        format (str): The image format. Defaults to "png".

    Returns:
        str: The path to the generated image file, or None if an error occurred.
    """
    try:
        img = Image.new("RGB", (200, 200), color=bg)
        d = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 120)
        except IOError:
            font = ImageFont.load_default()

        d.text((100, 100), char, font=font, fill=fg, anchor="mm")

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=f".{format}"
        ) as temp_file:
            img.save(temp_file, format=format.upper())
            temp_file_path = temp_file.name

        return temp_file_path
    except Exception as e:
        richPrint(f"ERROR: Failed to generate character image: {e}")
        return None


def detect_language(text: str) -> str:
    """
    Detect the language of the given text using multiple attempts for improved accuracy.

    Args:
        text (str): The text to detect the language for.

    Returns:
        str: The detected language code.
    """
    try:
        detections = [detect(text) for _ in range(5)]
        most_common = Counter(detections).most_common(1)[0][0]
        return most_common
    except LangDetectException as e:
        richPrint(f"ERROR: Language detection failed: {e}")
        return "unknown"


def fetch_help_embed(
    color_manager,
    bot_name: str,
    bot_version: str,
    bot_prefix: str,
    footer_text: str,
    footer_icon: str,
) -> discord.Embed:
    help_embed = discord.Embed(
        color=color_manager.get_color("Blue"),
        title=f"{bot_name} v{bot_version} Help Information",
        description=f"Here are the available commands (prefix: {bot_prefix}):",
    )
    help_embed.set_footer(text=footer_text, icon_url=footer_icon)

    commands = {
        "help": {"desc": "Show this help message", "usage": f"{bot_prefix}help"},
        "charinfo": {
            "desc": "Shows information and a image of the character provided",
            "usage": f"{bot_prefix}charinfo [character]",
        },
        "tts": {
            "desc": "Join the vc you are in and uses Text-to-Speech to say your text",
            "usage": f"{bot_prefix}tts [input_text]",
        },
        "nick": {
            "desc": "Changes guild specific username of a member (Mod only)",
            "usage": f"{bot_prefix}nick @user [new_nick]",
        },
        "feedback": {
            "desc": "Adds your feedback to our database",
            "usage": f"{bot_prefix}feedback [message]",
        },
        "play": {
            "desc": "Plays a song in the voice channel you are in",
            "usage": f"{bot_prefix}play [youtube_url]",
        },
        "profile": {
            "desc": "Gets information about the user",
            "usage": f"{bot_prefix}profile @user",
        },
        "server": {
            "desc": "Gets information about the server",
            "usage": f"{bot_prefix}server",
        },
        "joke": {
            "desc": "Fetches a random dad joke",
            "usage": f"{bot_prefix}joke",
        },
        "coin": {
            "desc": "Flips a coin, and lands on heads or tails",
            "usage": f"{bot_prefix}coin",
        },
        "quote": {
            "desc": "Fetches a random quote of the day",
            "usage": f"{bot_prefix}quote",
        },
        "ping": {
            "desc": "Gets the ping (latency) of the Discord Bot",
            "usage": f"{bot_prefix}ping",
        },
        "translate": {
            "desc": "Translates the provided text to english",
            "usage": f"{bot_prefix}translate [text]",
        },
        "timeout": {
            "desc": "Timeout a user for a specified duration (Mod only)",
            "usage": f"{bot_prefix}timeout @user <duration> <unit> [reason]",
        },
        "kick": {
            "desc": "Kick a user from the server (Mod only)",
            "usage": f"{bot_prefix}kick @user [reason]",
        },
        "ban": {
            "desc": "Ban a user from the server (Admin only)",
            "usage": f"{bot_prefix}ban @user [reason]",
        },
        "unban": {
            "desc": "Unbans a user from the server (Admin only)",
            "usage": f"{bot_prefix}unban @user",
        },
    }

    for cmd, info in commands.items():
        help_embed.add_field(
            name=f"{bot_prefix}{cmd}",
            value=f"{info['desc']}\nUsage: `{info['usage']}`",
            inline=False,
        )

    return help_embed


async def fetch_random_joke() -> str:
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data["joke"]
            else:
                return None


def fetch_quote_of_the_day() -> tuple:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = "https://api.quotable.io/random"

    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()

        quote = data["content"]
        author = data["author"]

        return quote, author

    except requests.RequestException as e:
        return f"An error occurred: {e}"


class ColorManager:
    """
    Manage colors for Discord embeds and other color-related functionality.
    """

    def __init__(self, config: dict):
        """
        Initialize the ColorManager with a configuration dictionary.

        Args:
            config (dict): A dictionary containing color configurations.
        """
        self.colors = config.get("colors", {})

    def get_color(self, color_name: str) -> int:
        """
        Get the integer representation of a color by its name.

        Args:
            color_name (str): The name of the color to retrieve.

        Returns:
            int: The integer representation of the color.

        Raises:
            ValueError: If the color name is not found in the configuration.
        """
        if color_name not in self.colors:
            raise ValueError(f"Color '{color_name}' not found in configuration")
        return int(self.colors[color_name].lstrip("#"), 16)

    def list_colors(self) -> list:
        """
        Get a list of all available color names.

        Returns:
            list: A list of color names.
        """
        return list(self.colors.keys())

    def create_color_embed(
        self, title: str, description: str, color_name: str
    ) -> discord.Embed:
        """
        Create a Discord embed with the specified color.

        Args:
            title (str): The title of the embed.
            description (str): The description of the embed.
            color_name (str): The name of the color to use for the embed.

        Returns:
            discord.Embed: The created Discord embed.
        """
        try:
            color = self.get_color(color_name)
            return discord.Embed(title=title, description=description, color=color)
        except ValueError as e:
            richPrint(f"ERROR: Failed to create color embed: {e}")
            # Fallback to a default color (e.g., Discord's default embed color)
            return discord.Embed(title=title, description=description)