import datetime
import tempfile
from PIL import Image, ImageDraw, ImageFont
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from collections import Counter
from gtts import gTTS
import discord

def set_langdetect_seed(seed: int = 0):
    DetectorFactory.seed = seed

def text_to_speech(text: str, output_file: str, tts_mode: str) -> None:
    try:
        slow = tts_mode.lower() == "slow"
        language = detect(text)
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(output_file)
    except Exception as e:
        print(f"ERROR_LOG ~ Text-to-speech conversion failed: {e}")

def log_info(value: str = "None") -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} [INFO] {value}")

def fetch_latency(client: discord.Client, shouldRound: bool = True) -> float:
    latency = client.latency * 1000
    return round(latency) if shouldRound else latency

def get_char_image(char: str, bg: str = "white", fg: str = "black", format: str = "png") -> str:
    try:
        img = Image.new("RGB", (200, 200), color=bg)
        d = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 120)
        except IOError:
            font = ImageFont.load_default()
        d.text((100, 100), char, font=font, fill=fg, anchor="mm")
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{format}") as temp_file:
            img.save(temp_file, format=format.upper())
            temp_file_path = temp_file.name
        return temp_file_path
    except Exception as e:
        print(f"ERROR: Failed to generate character image: {e}")
        return None
    
def detect_language(text: str) -> str:
    try:
        detections = [detect(text) for _ in range(5)]
        most_common = Counter(detections).most_common(1)[0][0]
        return most_common
    except LangDetectException as e:
        print(f"ERROR: Language detection failed: {e}")
        return "unknown"