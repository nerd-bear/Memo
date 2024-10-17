from rich import print as richPrint
import json
import datetime
import discord
from discord.ext import commands
import tempfile
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
from gtts import gTTS

def set_langdetect_seed(seed: int = 0):
    DetectorFactory.seed = seed

def text_to_speech(text: str, output_file: str, tts_mode: str) -> None:
    try:
        if tts_mode == "slow":
            slow = True
        else:
            slow = False

        language = detect(text)
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(output_file)

    except Exception as e:
        richPrint("ERROR_LOG ~ e:", e)

def load_config(config_path: str = "config.json") -> dict:
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"default_prefix": "?", "guilds": {}}


def save_config(config: dict, config_path: str = "config.json") -> None:
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)


def log_info(value: str = "None") -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp, end=" ")
    richPrint(f"[bold][blue]INFO[/blue][/bold] {value}")


def fetch_latency(client: commands.Bot, shouldRound: bool = True) -> int:
    return round(client.latency * 1000) if shouldRound else (client.latency * 1000)


def get_char_image(
    char: str, bg: str = "white", fg: str = "black", format: str = "png"
) -> str:
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
        return None
    
def detect_language(text):
    detections = [detect(text) for _ in range(5)]
    most_common = Counter(detections).most_common(1)[0][0]
    return most_common


class ColorManager:
    def __init__(self, config: dict):
        self.colors = config.get("colors", {})

    def get_color(self, color_name: str) -> int:
        if color_name not in self.colors:
            raise ValueError(f"Color '{color_name}' not found in configuration")
        return int(self.colors[color_name].lstrip("#"), 16)

    def list_colors(self) -> list:
        return list(self.colors.keys())

    def create_color_embed(
        self, title: str, description: str, color_name: str
    ) -> discord.Embed:
        color = self.get_color(color_name)
        return discord.Embed(title=title, description=description, color=color)