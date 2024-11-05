from typing import Optional, Tuple, Union
from rich.console import Console
from rich.console import Text
import datetime
import disnake
import aiohttp
import requests
import ssl
import urllib3
from disnake.ext import commands
import tempfile
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
from gtts import gTTS


def set_langdetect_seed(seed: int = 0) -> None:
    """
    Set the seed for language detection to ensure consistent results.
    """
    DetectorFactory.seed = seed


def text_to_speech(text: str, output_file: str, tts_mode: str) -> None:
    """
    Convert text to speech and save it to a file.
    """
    try:
        slow = tts_mode.lower() == "slow"

        language = detect(text)

        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(output_file)
    except Exception as e:
        log_info(f"Text-to-speech conversion failed: {e}", error=True)


def log_info(*values: str, startup: bool = False, error: bool = False, warning: bool = False, end: str = "\n", sep: str = " ") -> None:
    """
    Log an information message with a timestamp and supports different formats such as error, warning, info and startup.
    """

    console = Console()

    text_type = "INFO"
    if error:
        text_type = "ERROR"
        text_style = "bold red"
    elif startup:
        text_type = "STARTUP"
        text_style = "bold blue"
    elif warning:
        text_type = "WARNING"
        text_style = "bold yellow"

    text = Text()
    text.append(f"[{datetime.datetime.utcnow().__format__('%H:%M:%S')}]", style="bold cyan")
    text.append(f" [{text_type}]", style=text_style)
    text.append(f" {sep.join(values)}", style="#ffeab0")

    console.print(text, end=end)

def fetch_latency(client: commands.Bot, shouldRound: bool = True) -> float:
    """
    Fetch the latency of the Discord client.
    """
    latency = client.latency * 1000
    return round(latency) if shouldRound else latency


async def send_error_embed(
    message: disnake.Message,
    title: str,
    description: str,
    FOOTER_TEXT: str,
    FOOTER_ICON: str,
    color_manager: "ColorManager",
) -> None:
    """
    Send an error embed to the specified Discord message channel.
    """
    embed = disnake.Embed(
        title=title,
        description=description,
        color=color_manager.get_color("Red"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)


def get_char_image(
    char: str, bg: str = "white", fg: str = "black", format: str = "png"
) -> Optional[str]:
    """
    Generate an image of a single character.
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
        log_info(f"Failed to generate character image: {e}", error=True)
        return None


def detect_language(text: str) -> str:
    """
    Detect the language of the given text using multiple attempts for improved accuracy.
    """
    try:
        detections = [detect(text) for _ in range(5)]
        most_common = Counter(detections).most_common(1)[0][0]
        return most_common
    except LangDetectException as e:
        log_info(f"Language detection failed: {e}", error=True)
        return "unknown"


def fetch_help_dict(
    color_manager: "ColorManager",
    bot_name: str,
    bot_version: str,
    bot_prefix: str,
    footer_text: str,
    footer_icon: str,
) -> dict:
    return {
        "help": {"desc": "Show this help message", "usage": f"{bot_prefix}help"},
        "charinfo": {
            "desc": "Shows information and a image of the character provided",
            "usage": f"{bot_prefix}charinfo [character]",
        },
        "man": {
            "desc": "Displays information about the command",
            "usage": f"{bot_prefix}man [command_name]",
        },
        "tts": {
            "desc": "Join the vc you are in and uses Text-to-Speech to say your text",
            "usage": f"{bot_prefix}tts [input_text]",
        },
        "chat": {
            "desc": "Lets you send a message to the chat bot and it will send back a response",
            "usage": f"{bot_prefix}chat [input_text]",
        },
        "afk": {
            "desc": "Allows users to toggle AFK status on/off",
            "usage": f"{bot_prefix}afk [message]",
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
        "8ball": {
            "desc": "Answers a yes or no question",
            "usage": f"{bot_prefix}8ball [question]",
        },
        "rps": {
            "desc": "Allowed you to play rock-paper-scissors against the bot",
            "usage": f"{bot_prefix}rps [rock|paper|scissors]",
        },
        "kiss": {
            "desc": "Allows you to kiss a user",
            "usage": f"{bot_prefix}kiss @user",
        },
        "ping": {
            "desc": "Gets the ping (latency) of the Discord Bot",
            "usage": f"{bot_prefix}ping",
        },
        "translate": {
            "desc": "Translates the provided text to english",
            "usage": f"{bot_prefix}translate [text]",
        },
        "spellcheck": {
            "desc": "Returns the text spelled correctly",
            "usage": f"{bot_prefix}spellcheck [text]",
        },
        "setprefix": {
            "desc": "Changes the command prefix for your guild (Admin only)",
            "usage": f"{bot_prefix}setprefix [prefix]",
        },
        "purge": {
            "desc": "Removes the specified number of messages from the channel (Mod only)",
            "usage": f"{bot_prefix}purge [number_of_messages]",
        },
        
        "timeout": {
            "desc": "Timeout a user for a specified duration (Mod only)",
            "usage": f"{bot_prefix}timeout @user <duration> <unit> [reason]",
        },
        "mute": {
            "desc": "Server mutes a member (Mod only)",
            "usage": f"{bot_prefix}mute @user [reason]",
        },
        "unmute": {
            "desc": "Server unmutes a member (Mod only)",
            "usage": f"{bot_prefix}unmute @user [reason]",
        },
        "deafen": {
            "desc": "Server deafens a member (Mod only)",
            "usage": f"{bot_prefix}deafen @user [reason]",
        },
        "undeafen": {
            "desc": "Server undeafens a member (Mod only)",
            "usage": f"{bot_prefix}undeafen @user [reason]",
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
            "usage": f"{bot_prefix}unban [user_id]",
        },
    }


def fetch_help_embed(
    color_manager: "ColorManager",
    bot_name: str,
    bot_version: str,
    bot_prefix: str,
    footer_text: str,
    footer_icon: str,

) -> disnake.Embed:
    """
    Create and return a help embed for the bot.
    """
    help_embed = disnake.Embed(
        color=color_manager.get_color("Blue"),
        title=f"{bot_name} Help Information",
        description=f"Here are the available commands (prefix: {bot_prefix}):\n",
    )
    help_embed.set_footer(text=footer_text, icon_url=footer_icon)

    commands = fetch_help_dict(color_manager, bot_name, bot_version, bot_prefix, footer_text, footer_icon)
    
    for cmd, info in commands.items():
        help_embed.description = help_embed.description + f"\n **{bot_prefix}{cmd}** \n{info['desc']}\nUsage: `{info['usage']}`\n"
    
    return help_embed


def fetch_info_embed(
    color_manager: "ColorManager",
    bot_name: str,
    bot_version: str,
    bot_prefix: str,
    footer_text: str,
    footer_icon: str,
) -> disnake.Embed:
    """
    Create and return an info embed for the bot.
    """
    info_embed = disnake.Embed(
        color=color_manager.get_color("Blue"),
        title=f"{bot_name} v{bot_version} Info",
        description=f"Here is some general information about the bot, please keep in mind that the bot is in development.",
    )

    info_embed.add_field(name="Command Information", value=f"Prefix: `{bot_prefix}`")
    info_embed.set_footer(text=footer_text, icon_url=footer_icon)

    return info_embed


async def fetch_random_joke() -> Optional[str]:
    """
    Fetch a random joke from an API.
    """
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data["joke"]
            else:
                return None


def fetch_quote_of_the_day() -> Union[Tuple[str, str], str]:
    """
    Fetch the quote of the day from an API.
    Returns either a tuple of (quote, author) or an error message string.
    """
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
        self.colors: dict = config.get("colors", {})

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
    ) -> disnake.Embed:
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
            return disnake.Embed(title=title, description=description, color=color)
        except ValueError as e:
            log_info(f"Failed to create color embed: {e}", error=True)
            return disnake.Embed(title=title, description=description)
