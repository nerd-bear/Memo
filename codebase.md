# BotUpdate\cogs\__init__.py

```py

```

# BotUpdate\cogs\admin.py

```py
import discord
from discord.ext import commands
from utils.config_manager import ColorManager, load_config
from utils.db_manager import add_history
import sys
import os

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.color_manager = ColorManager(self.config)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        add_history(ctx.author.id, "shutdown")
        embed = discord.Embed(
            title=f"{self.config['bot_name']} Shutting Down",
            description=f"{self.config['bot_name']} is now offline.",
            color=self.color_manager.get_color("Red"),
            timestamp=ctx.message.created_at
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)
        await self.bot.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def start(self, ctx):
        add_history(ctx.author.id, "start")
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(name=f"Run {self.config['defaults']['prefix']}help for help")
        )
        embed = discord.Embed(
            title=f"{self.config['bot_name']} Starting Up",
            description=f"{self.config['bot_name']} is now online.",
            color=self.color_manager.get_color("Blue"),
            timestamp=ctx.message.created_at
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx):
        add_history(ctx.author.id, "restart")
        embed = discord.Embed(
            title="Restarting",
            description="The restart will take approximately 10 to 30 seconds on average.",
            color=self.color_manager.get_color("Blue")
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)
        await self.bot.close()
        os.execv(sys.executable, ['python'] + sys.argv)

async def setup(bot):
    await bot.add_cog(Admin(bot))
```

# BotUpdate\cogs\events.py

```py
import discord
from discord.ext import commands
from utils.config_manager import ColorManager, load_config
import datetime

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.color_manager = ColorManager(self.config)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.bot.user:
            return

        log_channel_id = self.config.get("log_channel_id")
        if not log_channel_id:
            return

        channel = self.bot.get_channel(int(log_channel_id))
        if not channel:
            return

        embed = discord.Embed(
            title="Message Deleted",
            color=self.color_manager.get_color("Red"),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name="Author", value=message.author.mention)
        embed.add_field(name="Channel", value=message.channel.mention)
        embed.add_field(name="Content", value=message.content or "No content")

        if message.attachments:
            embed.add_field(
                name="Attachments",
                value="\n".join([a.url for a in message.attachments])
            )

        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author == self.bot.user:
            return

        if before.content == after.content:
            return

        log_channel_id = self.config.get("log_channel_id")
        if not log_channel_id:
            return

        channel = self.bot.get_channel(int(log_channel_id))
        if not channel:
            return

        embed = discord.Embed(
            title="Message Edited",
            color=self.color_manager.get_color("Orange"),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name="Author", value=before.author.mention)
        embed.add_field(name="Channel", value=before.channel.mention)
        embed.add_field(name="Before", value=before.content or "No content")
        embed.add_field(name="After", value=after.content or "No content")

        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to use this command.")
            return

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument: {error.param}")
            return

        # For other types of errors, you might want to log them
        print(f"An error occurred: {error}")

async def setup(bot):
    await bot.add_cog(Events(bot))
```

# BotUpdate\cogs\fun.py

```py
import discord
from discord.ext import commands
from utils.config_manager import ColorManager, load_config
from utils.db_manager import add_history
from utils.helper import get_char_image
import unicodedata
import os

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.color_manager = ColorManager(self.config)

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):
        add_history(ctx.author.id, "charinfo", [characters])
        if len(characters) > 1:
            await ctx.send("Please provide only one character for information.")
            return

        char = characters[0]
        unicode_value = ord(char)
        char_name = unicodedata.name(char, "Could not find name!")
        char_category = unicodedata.category(char)

        unicode_escape = f"\\u{unicode_value:04x}"
        unicode_escape_full = f"\\U{unicode_value:08x}"
        python_escape = repr(char)

        embed = discord.Embed(
            color=self.color_manager.get_color("Blue"),
            title="Character info",
            description=f"Information on character: {char}"
        )

        embed.add_field(name="Original character", value=char, inline=True)
        embed.add_field(name="Character name", value=char_name, inline=True)
        embed.add_field(name="Character category", value=char_category, inline=True)
        embed.add_field(name="Unicode value", value=f"U+{unicode_value:04X}", inline=True)
        embed.add_field(name="Unicode escape", value=unicode_escape, inline=True)
        embed.add_field(name="Full Unicode escape", value=unicode_escape_full, inline=True)
        embed.add_field(name="Python escape", value=python_escape, inline=True)

        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )

        image_path = get_char_image(char)

        if image_path:
            file = discord.File(image_path, filename="character.png")
            embed.set_thumbnail(url="attachment://character.png")
            await ctx.send(embed=embed, file=file)
            os.remove(image_path)
        else:
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
```

# BotUpdate\cogs\moderation.py

```py
import discord
from discord.ext import commands
from utils.config_manager import ColorManager, load_config
from utils.db_manager import add_history
import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.color_manager = ColorManager(self.config)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        add_history(ctx.author.id, "kick", [str(member.id), reason])
        try:
            await member.send(
                embed=discord.Embed(
                    title="You've Been Kicked",
                    description=f"You were kicked from {ctx.guild.name}.\nReason: {reason}",
                    color=self.color_manager.get_color("Red")
                )
            )
        except:
            pass  # Unable to DM the user

        await member.kick(reason=reason)
        embed = discord.Embed(
            title="User Kicked",
            description=f"{member.mention} has been kicked.\nReason: {reason}",
            color=self.color_manager.get_color("Blue")
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        add_history(ctx.author.id, "ban", [str(member.id), reason])
        try:
            await member.send(
                embed=discord.Embed(
                    title="You've Been Banned",
                    description=f"You were banned from {ctx.guild.name}.\nReason: {reason}",
                    color=self.color_manager.get_color("Red")
                )
            )
        except:
            pass  # Unable to DM the user

        await member.ban(reason=reason)
        embed = discord.Embed(
            title="User Banned",
            description=f"{member.mention} has been banned.\nReason: {reason}",
            color=self.color_manager.get_color("Blue")
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        add_history(ctx.author.id, "unban", [member])
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="User Unbanned",
                    description=f"{user.mention} has been unbanned.",
                    color=self.color_manager.get_color("Blue")
                )
                embed.set_footer(
                    text=self.config["defaults"]["footer_text"],
                    icon_url=self.config["defaults"]["footer_icon"]
                )
                await ctx.send(embed=embed)
                return

        await ctx.send(f"User {member} not found in ban list.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def timeout(self, ctx, member: discord.Member, duration: int, unit, *, reason="No reason provided"):
        add_history(ctx.author.id, "timeout", [str(member.id), str(duration), unit, reason])
        time_units = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}
        if unit not in time_units:
            await ctx.send("Invalid time unit. Use 's' for seconds, 'm' for minutes, 'h' for hours, or 'd' for days.")
            return

        time_delta = datetime.timedelta(**{time_units[unit]: duration})
        await member.timeout(time_delta, reason=reason)
        
        embed = discord.Embed(
            title="User Timed Out",
            description=f"{member.mention} has been timed out for {duration}{unit}.\nReason: {reason}",
            color=self.color_manager.get_color("Blue")
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

        try:
            await member.send(
                embed=discord.Embed(
                    title="You were timed out",
                    description=f"You have been timed out in {ctx.guild.name} for {duration}{unit}.\nReason: {reason}",
                    color=self.color_manager.get_color("Red")
                )
            )
        except:
            pass  # Unable to DM the user

async def setup(bot):
    await bot.add_cog(Moderation(bot))
```

# BotUpdate\cogs\music.py

```py
import discord
from discord.ext import commands
from utils.config_manager import ColorManager, load_config
from utils.db_manager import add_history
import yt_dlp
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.color_manager = ColorManager(self.config)

    @commands.command()
    async def join(self, ctx):
        add_history(ctx.author.id, "join")
        if ctx.author.voice is None:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel.name}")

    @commands.command()
    async def leave(self, ctx):
        add_history(ctx.author.id, "leave")
        if ctx.voice_client is None:
            await ctx.send("I'm not in a voice channel.")
            return

        await ctx.voice_client.disconnect()
        await ctx.send("Left the voice channel")

    @commands.command()
    async def play(self, ctx, *, query):
        add_history(ctx.author.id, "play", [query])
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                return

        async with ctx.typing():
            try:
                with yt_dlp.YoutubeDL({"format": "bestaudio", "noplaylist": "True"}) as ydl:
                    info = ydl.extract_info(query, download=False)
                    URL = info["url"]
                    title = info["title"]
            except Exception as e:
                await ctx.send(f"An error occurred: {str(e)}")
                return

            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()

            FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn'
            }
            audio_source = discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)
            ctx.voice_client.play(audio_source)

        embed = discord.Embed(
            title="Now Playing",
            description=f"Now playing: {title}",
            color=self.color_manager.get_color("Blue")
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Music(bot))
```

# BotUpdate\cogs\utility.py

```py
import discord
from discord.ext import commands
from utils.config_manager import ColorManager, load_config
from utils.db_manager import add_history, add_feedback
from utils.helper import fetch_latency, text_to_speech
import os
import asyncio
from deep_translator import GoogleTranslator

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.color_manager = ColorManager(self.config)

    @commands.command()
    async def ping(self, ctx):
        add_history(ctx.author.id, "ping")
        latency = fetch_latency(self.bot)
        embed = discord.Embed(
            title="Bot Latency",
            description=f"The current bot latency is approximately `{latency}ms`",
            color=self.color_manager.get_color("Blue")
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        add_history(ctx.author.id, "profile", [str(member.id)])

        embed = discord.Embed(
            title=f"{member.name}'s Profile",
            description="User's public Discord information",
            color=self.color_manager.get_color("Blue")
        )
        embed.add_field(name="Display Name", value=member.display_name, inline=True)
        embed.add_field(name="User ID", value=member.id, inline=True)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%d/%m/%y %H:%M:%S"), inline=True)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%d/%m/%y %H:%M:%S"), inline=True)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=True)
        embed.add_field(name="Status", value=str(member.status).title(), inline=True)

        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)

        await ctx.send(embed=embed)

    @commands.command()
    async def feedback(self, ctx, *, message):
        add_history(ctx.author.id, "feedback", [message])
        if add_feedback(str(ctx.author.id), message):
            embed = discord.Embed(
                title="Feedback Received",
                description="Thank you for your feedback!",
                color=self.color_manager.get_color("Green")
            )
        else:
            embed = discord.Embed(
                title="Feedback Error",
                description="There was an error submitting your feedback. Please try again later.",
                color=self.color_manager.get_color("Red")
            )
        
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def tts(self, ctx, *, text):
        add_history(ctx.author.id, "tts", [text])
        if not ctx.author.voice:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        output_file = f"./temp/audio/tts_{ctx.message.id}.mp3"
        
        try:
            text_to_speech(text, output_file, self.config.get("tts_mode", "normal"))
        except Exception as e:
            await ctx.send(f"An error occurred while generating the TTS: {str(e)}")
            return

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            vc = await voice_channel.connect()
        else:
            vc = ctx.voice_client

        if vc.is_playing():
            vc.stop()

        vc.play(
            discord.FFmpegPCMAudio(source=output_file),
            after=lambda e: asyncio.run_coroutine_threadsafe(vc.disconnect(), self.bot.loop)
        )

        while vc.is_playing():
            await asyncio.sleep(1)

        if os.path.exists(output_file):
            os.remove(output_file)

        embed = discord.Embed(
            title="TTS Completed",
            description=f"Successfully played TTS in {voice_channel.mention}",
            color=self.color_manager.get_color("Blue")
        )
        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def translate(self, ctx, *, text):
        add_history(ctx.author.id, "translate", [text])
        try:
            translator = GoogleTranslator(source="auto", target="en")
            translated_text = translator.translate(text)

            embed = discord.Embed(
                title="Translation",
                description=translated_text,
                color=self.color_manager.get_color("Blue")
            )
            embed.set_footer(
                text=self.config["defaults"]["footer_text"],
                icon_url=self.config["defaults"]["footer_icon"]
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred during translation: {str(e)}")

async def setup(bot):
    await bot.add_cog(Utility(bot))
```

# BotUpdate\config.json

```json

```

# BotUpdate\logs\bot.log

```log

```

# BotUpdate\main.py

```py
Here's the main.py file without comments or explanations:

\`\`\`python
import os
import discord
from discord.ext import commands
import json
import logging
from utils.config_manager import load_config

intents = discord.Intents.all()
config = load_config()

bot = commands.Bot(command_prefix=config['defaults']['prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded cog: {filename[:-3]}')
            except Exception as e:
                print(f'Failed to load cog {filename[:-3]}: {str(e)}')

async def main():
    logging.basicConfig(filename='logs/bot.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    
    await load_cogs()
    await bot.start(config['token'])

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
\`\`\`
```

# BotUpdate\utils\__init__.py

```py

```

# BotUpdate\utils\config_manager.py

```py
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
```

# BotUpdate\utils\db_manager.py

```py
import sqlite3
import datetime
import json

DB_PATH = "./data/crac.db"

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def execute_query(query: str, params: tuple = (), fetch: bool = False):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return True

def add_feedback(user_id: str, message: str) -> bool:
    datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
    query = "INSERT INTO feedback VALUES (?, ?, ?)"
    return execute_query(query, (user_id, message, datetime_value))

def add_history(user_id: int, command: str, arguments: list[str] = ["none"]) -> bool:
    args_json = json.dumps(arguments)
    datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
    query = "INSERT INTO history (user_id, command, arguments, datetime) VALUES (?, ?, ?, ?)"
    return execute_query(query, (user_id, command, args_json, datetime_value))

def get_usage(command_name: str) -> tuple[str, str, str]:
    query = "SELECT command_name, arguments, level FROM usage WHERE command_name = ?"
    result = execute_query(query, (command_name,), fetch=True)
    return result[0] if result else None

def get_all_usages() -> list[tuple[str, str, str]]:
    query = "SELECT command_name, arguments, level FROM usage"
    return execute_query(query, fetch=True)

def add_usage(command_name: str, arguments: list[str], level: int) -> bool:
    if not 0 <= level <= 3:
        raise ValueError("Level must be between 0 and 3")
    query = "INSERT INTO usage (command_name, arguments, level) VALUES (?, ?, ?)"
    args_json = json.dumps(arguments)
    return execute_query(query, (command_name, args_json, str(level)))

def create_tables():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS feedback (user_id TEXT, message TEXT, datetime TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS history (user_id INTEGER, command TEXT, arguments TEXT, datetime TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS usage (command_name TEXT, arguments TEXT, level TEXT)")
        conn.commit()

# Call this function when initializing the bot to ensure tables exist
create_tables()
```

# BotUpdate\utils\helper.py

```py
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
```

# config.json

```json
{
    "defaults": {
        "prefix": "?",
        "footer_text": "This bot is created and hosted by Nerd bear",
        "footer_icon": "https://as2.ftcdn.net/v2/jpg/01/17/00/87/1000_F_117008730_0Dg5yniuxPQLz3shrJvLIeBsPfPRBSE1.jpg"
    },

    "bot_version": "0.4.6",
    "bot_name": "CRAC",
    "tts_mode":"fast",
    "log_channel_id": "1290060885485948950",
    "tts_detector_factory_seed": "0",
    
    "colors": {
      "Red": "#FFB3BA",
      "Coral": "#FFCCB6",
      "Orange": "#FFE5B4",
      "Gold": "#FFF1B5",
      "Yellow": "#FFFFD1",
      "Lime": "#DCFFB8",
      "Green": "#BAFFC9",
      "Teal": "#B5EAD7",
      "Cyan": "#C7F2FF",
      "Blue": "#B5DEFF",
      "Navy": "#C5CAE9",
      "Purple": "#D0B8FF",
      "Magenta": "#F2B5D4",
      "Pink": "#FFCCE5",
      "Gray": "#E0E0E0",
      "Lavender": "#E6E6FA"
    },

    "guilds": {
        "1288144110880030795": {
            "prefix": "*"
        }
    }
}
```

# db_manager\__intit__.py

```py

```

# db_manager\feedback.py

```py
import sqlite3
import datetime


def add_feedback(user_id: str, message: str) -> bool:
    """Uses SQLite to add user's feedback to feedback db table

    ### Params:
        `used_id`  `str`   The user id of the person who submitted the feedback.
        `message`  `str`   The name of the command that the user ran.

    ### Return:
        Returns a bool (True on success)
    """

    datetime_value = datetime.datetime.today().now().__format__("%S:%M:%H %d/%m/%y")

    db_connection = sqlite3.connect("./crac.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        f'INSERT INTO feedback VALUES (\'{user_id}\', "{message}", "{datetime_value}")'
    )
    db_connection.commit()

    return True

```

# db_manager\history.py

```py
import sqlite3
import datetime
import json

def add_history(user_id: int, command: str, arguments: list[str] = ["none"]) -> bool:
    """Uses SQLite to add user command to history of commands ran

    ### Params:
        `user_id`  `int`   The user id of the person who ran the command.
        `command`  `str`   The name of the command that the user ran.
        `arguments`  `list[str]`   The arguments passed in to the command, defaults to ["none"].

    ### Return:
        Returns a bool (True on success)
    """
    args_json = json.dumps(arguments)
    datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
    
    db_connection = sqlite3.connect("./crac.db")
    db_cursor = db_connection.cursor()
    
    try:
        db_cursor.execute(
            "INSERT INTO history (user_id, command, arguments, datetime) VALUES (?, ?, ?, ?)",
            (user_id, command, args_json, datetime_value)
        )
        db_connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"ERROR_LOG: SQLite error: {e}")
        return False
    finally:
        db_connection.close()
```

# db_manager\usage.py

```py
import sqlite3
from typing import List, Tuple
import json

DB_PATH = "./crac.db"


def get_db_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DB_PATH)


def execute_query(query: str, params: Tuple = (), fetch: bool = False):
    """Execute a SQL query and optionally fetch results."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return True


def get_usage(command_name: str) -> Tuple[str, str, str]:
    """Get usage information for a specific command.

    Args:
        command_name (str): The name of the command to retrieve.

    Returns:
        Tuple[str, str, str]: A tuple containing (command_name, arguments, level).
        Returns None if the command is not found.
    """
    query = "SELECT command_name, arguments, level FROM usage WHERE command_name = ?"
    result = execute_query(query, (command_name,), fetch=True)
    return result[0] if result else None


def get_all_usages() -> List[Tuple[str, str, str]]:
    """Get usage information for all commands.

    Returns:
        List[Tuple[str, str, str]]: A list of tuples, each containing (command_name, arguments, level).
    """
    query = "SELECT command_name, arguments, level FROM usage"
    return execute_query(query, fetch=True)


def add_usage(command_name: str, arguments: List[str], level: int) -> bool:
    """Add usage information for a command.

    Args:
        command_name (str): The name of the command to add.
        arguments (List[str]): The list of arguments the command accepts.
        level (int): The permission level of the command (0-3).

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    if not 0 <= level <= 3:
        raise ValueError("Level must be between 0 and 3")

    query = "INSERT INTO usage (command_name, arguments, level) VALUES (?, ?, ?)"
    args_json = json.dumps(arguments)
    return execute_query(query, (command_name, args_json, str(level)))
```

# launcher.py

```py
from src.bot import CRAC

CRAC.run("MTI4OTkyMTQ3NjYxNDU1MzY3Mg.GNo3VX.kjVPN-1ri34TtfuWZ-ADqhSeW56fARaLu7pMnk")
```

# requirements.txt

```txt
aiohappyeyeballs==2.4.3
aiohttp==3.10.8
aiosignal==1.3.1
aiosqlite==0.20.0
annotated-types==0.7.0
anyio==4.6.0
async-timeout==4.0.3
attrs==24.2.0
beautifulsoup4==4.12.3
blinker==1.8.2
Brotli==1.1.0
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
comtypes==1.4.7
cryptography==43.0.1
dataclasses-json==0.6.7
deep-translator==1.11.4
Deprecated==1.2.14
discord==2.3.2
discord.py==2.4.0
disnake==2.9.2
distro==1.9.0
duckduckgo_search==6.2.13
edge-tts==6.1.12
fastapi==0.115.0
ffmpeg-python==0.2.0
Flask==3.0.3
Flask-Cors==5.0.0
frozenlist==1.4.1
future==1.0.0
gevent==24.2.1
greenlet==3.1.1
groq==0.11.0
gTTS==2.5.3
h11==0.14.0
httpcore==1.0.5
httpx==0.27.2
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.4
joblib==1.4.2
jsonpatch==1.33
jsonpointer==3.0.0
langchain==0.3.1
langchain-community==0.3.1
langchain-core==0.3.6
langchain-groq==0.2.0
langchain-ollama==0.2.0
langchain-text-splitters==0.3.0
langdetect==1.0.9
langsmith==0.1.129
lxml==5.3.0
lyrics-extractor==3.0.1
lyricsgenius==3.0.1
markdown-it-py==3.0.0
MarkupSafe==2.1.5
marshmallow==3.22.0
mdurl==0.1.2
multidict==6.1.0
mutagen==1.47.0
mypy-extensions==1.0.0
nltk==3.9.1
numpy==1.26.4
ollama==0.3.3
orjson==3.10.7
packaging==24.1
pillow==10.4.0
primp==0.6.3
pycparser==2.22
pycryptodomex==3.20.0
pydantic==2.9.2
pydantic-settings==2.5.2
pydantic_core==2.23.4
PyGithub==2.4.0
Pygments==2.18.0
PyJWT==2.9.0
PyNaCl==1.5.0
pypiwin32==223
PySide6==6.7.3
PySide6_Addons==6.7.3
PySide6_Essentials==6.7.3
python-dotenv==1.0.1
pyttsx3==2.98
pytube==15.0.0
pywin32==306
PyYAML==6.0.2
redis==5.1.0
regex==2024.9.11
requests==2.32.3
rich==13.8.1
shiboken6==6.7.3
six==1.16.0
sniffio==1.3.1
soupsieve==2.6
spotipy==2.24.0
SQLAlchemy==2.0.35
starlette==0.38.6
tenacity==8.5.0
timeout==0.1.2
tqdm==4.66.5
typing-inspect==0.9.0
typing_extensions==4.12.2
urllib3==2.2.3
uvicorn==0.31.0
websocket==0.2.1
websocket-client==1.8.0
websockets==13.1
Werkzeug==3.0.4
wikipedia==1.4.0
wrapt==1.16.0
yarl==1.13.1
youtube-transcript-api==0.6.2
yt-dlp==2024.9.27
zope.event==5.0
zope.interface==7.0.3

```

# setup\clear_feedback_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE feedback")
db_cursor.execute("CREATE TABLE feedback(used_id, message, datetime)")
db_connection.commit()
```

# setup\clear_history_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE history")
db_cursor.execute("CREATE TABLE history(user_id, command, arguments, datetime)")
db_connection.commit()
```

# setup\clear_usage_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE usage")
db_cursor.execute("CREATE TABLE usage(command_name, arguments, level)")
db_connection.commit()
```

# setup\create_feedback_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE feedback(used_id, message, datetime)")
db_connection.commit()
```

# setup\create_history_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE history(user_id, command, arguments, datetime)")
db_connection.commit()
```

# setup\create_usage_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE usage(command_name, arguments, level)")
db_connection.commit()
```

# src\bot.py

```py
import asyncio
import datetime
import os
import random
import sys
import functools
import unicodedata

import discord
import yt_dlp
from discord.ext import commands
from deep_translator import GoogleTranslator
from discord.ui import Button, Select, Modal, TextInput, View
from rich import print as richPrint
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from db_manager import history, feedback
from src.utils.helper import *


CONFIG_PATH = "config.json"

log_info("Loading Config")
config = load_config(CONFIG_PATH)
log_info("Completed loading config")

log_info("Loading default values into memory")
color_manager = ColorManager(config)
FOOTER_TEXT = config["defaults"].get("footer_text")
FOOTER_ICON = config["defaults"].get("footer_icon")
BOT_PREFIX = config["defaults"].get("prefix", "?")
BOT_NAME = config.get("bot_name", "CRAC Bot")
BOT_VERSION = config.get("bot_version", "1.0.0")
TTS_MODE = config.get("tts_mode", "normal")
LOGGING_CHANNEL_ID = int(config.get("log_channel_id", 0))

intents = discord.Intents.all()
CRAC = commands.Bot(command_prefix="/", intents=intents)
console = Console()

set_langdetect_seed(config.get("tts_detector_factory_seed", 0))

bot_active = True
log_info("Completed loading default values into memory")


async def get_info_text() -> str:
    return f"""
    {BOT_NAME} v{BOT_VERSION}
    Logged in as {CRAC.user.name} (ID: {CRAC.user.id})
    Connected to {len(CRAC.guilds)} guilds
    Bot is ready to use. Ping: {fetch_latency(CRAC)}ms
    Prefix: {BOT_PREFIX}
    Initialization complete.
    """


def debug_command(func):
    @functools.wraps(func)
    async def wrapper(message: discord.Message, *args: any, **kwargs: any):
        embed = discord.Embed(
            title="Warning",
            description=f"WARNING! This is a dev/debug command and will not be included in full release v1.0.0",
            color=color_manager.get_color("Orange"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return await func(message, *args, **kwargs)

    return wrapper


async def send_error_embed(
    message: discord.Message, title: str, description: str
) -> None:
    embed = discord.Embed(
        title=title,
        description=description,
        color=color_manager.get_color("Red"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)


@CRAC.event
async def on_ready() -> None:
    markdown = Markdown(f"# Discord {BOT_NAME} version {BOT_VERSION}")
    console.print(markdown)

    info_text = await get_info_text()
    panel = Panel(
        info_text, title=f"{BOT_NAME} v{BOT_VERSION} Initialization Info", expand=False
    )

    console.print(panel)

    channel = CRAC.get_channel(LOGGING_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title=f"{BOT_NAME} v{BOT_VERSION} Initialization Info",
            description=info_text,
            color=color_manager.get_color("Blue"),
            timestamp=datetime.datetime.utcnow(),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await channel.send(embed=embed)

    await CRAC.change_presence(
        activity=discord.Game(name=f"Run {BOT_PREFIX}help for help")
    )


@CRAC.event
async def on_message(message: discord.Message) -> None:
    global bot_active

    if message.author == CRAC.user:
        return

    if not message.content.startswith(BOT_PREFIX):
        if bot_active == False:
            return
        content = message.content.lower()
        if any(word in content for word in ["nigger", "nigga", "negro", "nigro"]):
            await handle_inappropriate_word(message)
        if CRAC.user in message.mentions:
            await message.channel.send(
                f"Hello {message.author.mention}! You mentioned me. How can I help you?"
            )
        return

    if message.content.startswith("?") and len(message.content.strip()) <= 1:
        return

    if not bot_active and message.content != f"{BOT_PREFIX}start":
        embed = discord.Embed(
            title="Bot Offline",
            description=f"{BOT_NAME} is currently offline. Use {BOT_PREFIX}start to activate.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    command = message.content.split()[0][len(BOT_PREFIX) :].lower()
    args = message.content.split()[1:]

    history.add_history(message.author.id, command, args)

    if command == "help":
        await help_command(message)

    elif command == "timeout":
        await timeout_command(message)

    elif command == "kick":
        await kick_command(message)

    elif command == "ban":
        await ban_command(message)

    elif command == "unban":
        await unban_command(message)

    elif command == "shutdown":
        await shutdown_command(message)

    elif command == "start":
        await start_command(message)

    elif command == "charinfo":
        await charinfo_command(message)

    elif command == "join":
        await join_vc_command(message)

    elif command == "leave":
        await leave_vc_command(message)

    elif command == "tts":
        await tts_command(message)

    elif command == "play":
        await play_command(message)

    elif command == "profile":
        await profile_command(message)

    elif command == "nick":
        await nick_command(message)

    elif command == "feedback":
        await feedback_command(message)

    elif command == "restart":
        await restart_command(message)

    elif command == "translate":
        await translate_command(message)

    elif command == "ping":
        await ping_command(message)

    elif command == "server":
        await server_command(message)

    else:
        embed = discord.Embed(
            title="Invalid Command",
            description=f"The command you are running is not valid. Please run `?help` for a list of commands and their usages!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return


async def handle_inappropriate_word(message: discord.Message) -> None:
    user = message.author
    channel = message.channel

    dm_embed = discord.Embed(
        title="Inappropriate Word Detected",
        description=f"{BOT_NAME} has detected an inappropriate word! Please do not send racist words in our server! Moderators have been informed!",
        color=0xFF697A,
    )
    dm_embed.add_field(
        name="Rules",
        value="Please read our rules before sending such messages!",
        inline=False,
    )
    dm_embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    try:
        await user.send(embed=dm_embed)
    except discord.errors.Forbidden:
        pass

    await message.delete()

    channel_embed = discord.Embed(
        title="Inappropriate Word Detected",
        description=f"User {user.mention} tried to send a word that is marked not allowed!",
        color=0xFF697A,
    )
    channel_embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=channel_embed)


async def help_command(message: discord.Message) -> None:
    embed = discord.Embed(
        title=f"{BOT_NAME} v{BOT_VERSION} Help Information",
        description=f"Here are the available commands (prefix: {BOT_PREFIX}):",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    commands = {
        "help": {"desc": "Show this help message", "usage": f"{BOT_PREFIX}help"},
        "charinfo": {
            "desc": "Shows information and a image of the character provided",
            "usage": f"{BOT_PREFIX}charinfo [character]",
        },
        "tts": {
            "desc": "Join the vc you are in and uses Text-to-Speech to say your text",
            "usage": f"{BOT_PREFIX}tts [input_text]",
        },
        "nick": {
            "desc": "Changes guild specific username of a member (Mod only)",
            "usage": f"{BOT_PREFIX}nick @user [new_nick]",
        },
        "feedback": {
            "desc": "Adds your feedback to our database",
            "usage": f"{BOT_PREFIX}feedback [message]",
        },
        "play": {
            "desc": "Plays a song in the voice channel you are in",
            "usage": f"{BOT_PREFIX}play [youtube_url]",
        },
        "profile": {
            "desc": "Gets information about the user",
            "usage": f"{BOT_PREFIX}profile @user",
        },
        "server": {
            "desc": "Gets information about the server",
            "usage": f"{BOT_PREFIX}server",
        },
        "ping": {
            "desc": "Gets the ping (latency) of the Discord Bot",
            "usage": f"{BOT_PREFIX}ping",
        },
        "translate": {
            "desc": "Translates the provided text to english",
            "usage": f"{BOT_PREFIX}translate [text]",
        },
        "timeout": {
            "desc": "Timeout a user for a specified duration (Mod only)",
            "usage": f"{BOT_PREFIX}timeout @user <duration> <unit> [reason]",
        },
        "kick": {
            "desc": "Kick a user from the server (Mod only)",
            "usage": f"{BOT_PREFIX}kick @user [reason]",
        },
        "ban": {
            "desc": "Ban a user from the server (Admin only)",
            "usage": f"{BOT_PREFIX}ban @user [reason]",
        },
        "unban": {
            "desc": "Unbans a user from the server (Admin only)",
            "usage": f"{BOT_PREFIX}unban @user",
        }
    }

    for cmd, info in commands.items():
        embed.add_field(
            name=f"{BOT_PREFIX}{cmd}",
            value=f"{info['desc']}\nUsage: `{info['usage']}`",
            inline=False,
        )

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def kick_command(message: discord.Message) -> None:
    if not message.author.guild_permissions.kick_members:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to kick. Usage: {BOT_PREFIX}kick @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0]
    reason = " ".join(message.content.split()[2:]) or "No reason provided"

    try:
        await member.send(
            embed=discord.Embed(
                title="You've wBeen Kicked",
                description=f"You were kicked from {message.guild.name}.\nReason: {reason}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.kick(reason=reason)
    embed = discord.Embed(
        title="User Kicked",
        description=f"{member.mention} has been kicked.\nReason: {reason}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def ban_command(message: discord.Message) -> None:
    if not message.author.guild_permissions.ban_members:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to ban. Usage: {BOT_PREFIX}ban @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0]
    reason = " ".join(message.content.split()[2:]) or "No reason provided"

    try:
        await member.send(
            embed=discord.Embed(
                title="You've Been Banned",
                description=f"You were banned from {message.guild.name}.\nReason: {reason}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.ban(reason=reason)
    embed = discord.Embed(
        title="User Banned",
        description=f"{member.mention} has been banned.\nReason: {reason}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


@debug_command
async def shutdown_command(message: discord.Message) -> None:
    global bot_active
    if not message.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    bot_active = False
    await CRAC.change_presence(status=discord.Status.invisible)

    for vc in CRAC.voice_clients:
        await vc.disconnect()

    embed = discord.Embed(
        title=f"{BOT_NAME} Shutting Down",
        description=f"{BOT_NAME} is now offline.",
        color=color_manager.get_color("Red"),
        timestamp=datetime.datetime.utcnow(),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


@debug_command
async def start_command(message: discord.Message) -> None:
    global bot_active
    if not message.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    bot_active = True
    await CRAC.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name=f"Run {BOT_PREFIX}help for help"),
    )
    embed = discord.Embed(
        title=f"{BOT_NAME} Starting Up",
        description=f"{BOT_NAME} is now online.",
        color=color_manager.get_color("Blue"),
        timestamp=datetime.datetime.utcnow(),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def charinfo_command(message: discord.Message) -> None:

    try:
        argument_text = " ".join(message.content.split()[1:])
        char_text = argument_text[0]
    except IndexError:
        await message.channel.send(
            embed=discord.Embed(
                title="ERROR",
                color=color_manager.get_color("Blue"),
                description="Please provide a character to get information about.",
            )
        )
        return

    unicode_value = ord(char_text)
    char_name = unicodedata.name(char_text, "Could not find name!")
    char_category = unicodedata.category(char_text)

    unicode_escape = f"\\u{unicode_value:04x}"
    unicode_escape_full = f"\\U{unicode_value:08x}"
    python_escape = repr(char_text)

    embed = discord.Embed(
        color=color_manager.get_color("Blue"),
        title="Character info",
        type="rich",
        description=f"Information on character: {char_text}",
    )

    embed.add_field(name="Original character", value=char_text, inline=True)
    embed.add_field(name="Character name", value=char_name, inline=True)
    embed.add_field(name="Character category", value=char_category, inline=True)
    embed.add_field(name="Unicode value", value=f"U+{unicode_value:04X}", inline=True)
    embed.add_field(name="Unicode escape", value=unicode_escape, inline=True)
    embed.add_field(name="Full Unicode escape", value=unicode_escape_full, inline=True)
    embed.add_field(name="Python escape", value=python_escape, inline=True)

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    image_path = get_char_image(char_text)

    if image_path:
        file = discord.File(image_path, filename="character.png")
        embed.set_thumbnail(url="attachment://character.png")
    else:
        file = None

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    await message.channel.send(embed=embed, file=file)

    if image_path and os.path.exists(image_path):
        os.remove(image_path)


async def unban_command(message: discord.Message) -> None:

    if not message.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to unban. Usage: {BOT_PREFIX}unban @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0]
    invite = message.channel.create_invite(reason="Invite unbanned user")

    try:
        await member.send(
            embed=discord.Embed(
                title="You've Been unbanned",
                description=f"You were unbanned from {message.guild.name}",
                color=color_manager.get_color("Blue"),
            ).add_field(name="Invite link", value=invite)
        )
    except:
        pass

    try:
        await message.guild.unban(user=member)

    except discord.errors.Forbidden as e:
        embed = discord.Embed(
            title="Forbidden",
            description=f"Could not unban, {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except discord.errors.NotFound as e:
        embed = discord.Embed(
            title="Not found",
            description=f"Could not unban, {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except discord.errors.HTTPException as e:
        embed = discord.Embed(
            title="Unknown",
            description=f"Could not unban, {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    embed = discord.Embed(
        title="User Unbanned",
        description=f"{member.mention} has been unbanned.",
        color=color_manager.get_color("Red"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def timeout_command(message: discord.Message) -> None:
    if not message.author.guild_permissions.moderate_members:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    args = message.content.split()[1:]
    if len(args) < 3:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}timeout @user <duration> <unit> [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0] if message.mentions else None
    if not member:
        embed = discord.Embed(
            title="Invalid Usage",
            description="Please mention a user to timeout.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        duration = int(args[1])
        unit = args[2].lower()

    except ValueError:
        embed = discord.Embed(
            title="Invalid Usage",
            description="Duration must be a number.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    reason = " ".join(args[3:]) if len(args) > 3 else "No reason provided"

    if message.author.top_role <= member.top_role:
        embed = discord.Embed(
            title="Permission Denied",
            description="You cannot timeout this user as they have an equal or higher role.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    time_units = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}
    if unit not in time_units:
        embed = discord.Embed(
            title="Invalid Usage",
            description="Invalid time unit. Use 's' for seconds, 'm' for minutes, 'h' for hours, or 'd' for days.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    time_delta = datetime.timedelta(**{time_units[unit]: duration})

    try:
        await member.timeout(time_delta, reason=reason)
        embed = discord.Embed(
            title="User Timed Out",
            description=f"{member.mention} has been timed out for {duration}{unit}.\nReason: {reason}",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

    except discord.errors.Forbidden:
        embed = discord.Embed(
            title="Permission Error",
            description="I don't have permission to timeout this user.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

    except discord.errors.HTTPException:
        embed = discord.Embed(
            title="Error",
            description="Failed to timeout the user. The duration might be too long.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

    try:
        await member.timeout(time_delta, reason=reason)
        embed = discord.Embed(
            title="You were timed out",
            description=f"You (aka {member.mention}) have been timed out for {duration}{unit}.",
            color=color_manager.get_color("Blue"),
        )
        embed.add_field(name="reason", value=reason, inline=True)
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await member.send(embed=embed)

    except:
        pass


async def join_vc_command(message: discord.Message) -> None:
    try:
        channel = CRAC.get_channel(message.author.voice.channel.id)
        await channel.connect()
    except Exception as e:
        richPrint(e)


async def leave_vc_command(message: discord.Message) -> None:
    try:
        await message.guild.voice_client.disconnect()
    except Exception as e:
        pass


async def tts_command(message: discord.Message) -> None:
    text = " ".join(message.content.split()[1:])

    if not text:
        embed = discord.Embed(
            title="Missing arguments",
            description=f"Please make sure you pass some text for the TTS command. Usage: {BOT_PREFIX}tts [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return
        return

    output_file = f"./temp/audio/{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}.mp3"

    try:
        text_to_speech(text, output_file, TTS_MODE)
    except Exception as e:
        embed = discord.Embed(
            title="Error occurred",
            description=f"A issue occurred during the generation of the Text-to-Speech mp3 file! Usage: {BOT_PREFIX}tts [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        voice_channel = message.author.voice.channel
    except:
        embed = discord.Embed(
            title="Join voice channel",
            description=f"Please join a voice channel to use this command! Usage: {BOT_PREFIX}tts [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        vc = await voice_channel.connect()
    except discord.ClientException:
        vc = message.guild.voice_client

    if vc.is_playing():
        vc.stop()

    vc.play(
        discord.FFmpegPCMAudio(source=output_file),
        after=lambda e: asyncio.run_coroutine_threadsafe(vc.disconnect(), CRAC.loop),
    )

    while vc.is_playing():
        await asyncio.sleep(0.1)

    if os.path.exists(output_file):
        os.remove(output_file)

    embed = discord.Embed(
        title="Ended TTS",
        description=f"Successfully generated and played TTS file. Disconnecting from <#{voice_channel.id}>",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)
    return


async def play_command(message: discord.Message) -> None:
    args = message.content.split(" ", 1)
    if len(args) < 2:
        await message.channel.send("Please provide a YouTube URL or search term.")
        return

    query = args[1]

    try:
        voice_channel = message.author.voice.channel
        if not voice_channel:
            raise AttributeError
    except AttributeError:
        embed = discord.Embed(
            title="Join voice channel",
            description="Please join a voice channel to use this command!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        vc = await voice_channel.connect()
    except discord.ClientException:
        vc = message.guild.voice_client

    if vc.is_playing():
        vc.stop()

    try:
        with yt_dlp.YoutubeDL({"format": "bestaudio", "noplaylist": "True"}) as ydl:
            info = ydl.extract_info(query, download=False)
            URL = info["url"]
            title = info["title"]
    except Exception as e:
        embed = discord.Embed(
            title="Error occurred",
            description=f"An issue occurred while trying to fetch the audio: {str(e)}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    vc.play(
        discord.FFmpegPCMAudio(
            URL,
            **{
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn",
            },
        )
    )

    embed = discord.Embed(
        title="Now Playing",
        description=f"Now playing: {title}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def profile_command(message: discord.Message) -> None:
    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        user = message.mentions[0]

    except Exception as e:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        fetched_user = await CRAC.fetch_user(user.id)

    except discord.errors.NotFound as e:
        embed = discord.Embed(
            title="Not found",
            description=f"Error occurred while fetching user. Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except discord.errors.HTTPException as e:
        embed = discord.Embed(
            title="Unknown Error",
            description=f"Error occurred while fetching user, but this exception does not have defined behavior. Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if user not in message.guild.members:
        embed = discord.Embed(
            title="Member not in guild!",
            description=f"Please make sure that the user you are searching for exists and is in this guild. Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    avatar = user.avatar
    name = user.display_name
    username = user.name
    user_id = user.id
    status = user.status
    creation = user.created_at.strftime("%d/%m/%y %H:%M:%S")
    badges = [badge.name for badge in user.public_flags.all()]
    banner_url = None
    top_role = "<@&" + str(user.roles[-1].id) + ">"
    roles: list[str] = []
    print(user.premium_since)
    roles_str = ""

    for role in user.roles:
        roles.append(f"<@&{role.id}>")

    roles.pop(0)  # Removes @everyone role

    for i in range(len(roles)):
        roles_str = roles_str + str(roles[i])

    try:
        banner_url = fetched_user.banner.url
    except:
        pass

    if status == discord.enums.Status(value="dnd"):
        status = "⛔ Do not disturb"

    elif status == discord.enums.Status(value="online"):
        status = "🟢 Online"

    elif status == discord.enums.Status(value="idle"):
        status = "🟡 Idle"

    else:
        status = "⚫ Offline"

    embed = discord.Embed(
        title=f"{name}'s Profile",
        description="Users public discord information, please don't use for bad or illegal purposes!",
    )
    embed.add_field(name="Display Name", value=name, inline=True)
    embed.add_field(name="Username", value=username, inline=True)
    embed.add_field(name="User ID", value=user_id, inline=True)
    embed.add_field(name="Creation Time", value=creation, inline=True)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="Badges", value=badges, inline=True)
    embed.add_field(name="Top role", value=top_role, inline=True)
    embed.add_field(
        name="Roles",
        value=("No roles" if roles_str.strip() == "" else roles_str),
        inline=True,
    )
    embed.set_thumbnail(
        url=(
            avatar
            if avatar
            else "https://i.pinimg.com/474x/d6/c1/09/d6c109542c43e5b7c6699761c8c78d16.jpg"
        )
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    embed.set_image(url=(banner_url if banner_url != None else ""))
    embed.color = color_manager.get_color("Blue")

    await message.channel.send(embed=embed)


async def nick_command(message: discord.Message) -> None:
    if (
        not message.author.guild_permissions.administrator
        | message.author.guild_permissions.administrator
    ):
        embed = discord.Embed(
            title="Missing permission",
            description=f"Missing required permission `manage_nicknames`. Please run `{BOT_PREFIX}help` for more information!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}nick @user [new_nickname]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    user = message.mentions[0]

    if user not in message.guild.members:
        embed = discord.Embed(
            title="Member not in guild!",
            description=f"Please make sure that the user you are searching for exists and is in this guild. Usage: {BOT_PREFIX}nick @user [new_nick]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    args = message.content.split(" ")

    try:
        await user.edit(nick=" ".join(args[2:]))
        embed = discord.Embed(
            title="Successfully updated nickname!",
            description=f"Successfully updated nickname of <@{user.id}> to {" ".join(args[2:])}",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except Exception as e:
        embed = discord.Embed(
            title="Issue occurred",
            description=f"An issue occurred during this operation. This exception was caught by a general handler. {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return


async def feedback_command(message: discord.Message) -> None:
    args = message.content.split()[1:]
    feedback_text = " ".join(args)

    if len(args) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}feedback [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    feedback.add_feedback(message.author.id, feedback_text)

    embed = discord.Embed(
        color=color_manager.get_color("Blue"),
        title="Recorded Feedback",
        description=f"Recorded feedback from <@{message.author.id}>",
    )
    embed.add_field(name="Message", value=feedback_text, inline=False)
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


@debug_command
async def restart_command(message: discord.Message) -> None:
    embed = discord.Embed(
        title="Restarting",
        description=f"The restart will take approximately 10 to 30 seconds on average.",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)
    await CRAC.close()
    os.execv(sys.executable, ["python"] + sys.argv)


async def translate_command(message: discord.Message) -> None:
    translate_text = message.content.split(" ", 1)[1]

    try:
        translator = GoogleTranslator(source="auto", target="en")
        translated_text = translator.translate(translate_text)

        embed = discord.Embed(
            title="Translation",
            description=translated_text,
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )

        await message.channel.send(embed=embed)

    except Exception as e:
        await message.channel.send(f"An error occurred: {str(e)}")


async def ping_command(message: discord.Message) -> None:
    bot_latency = fetch_latency(CRAC)

    embed = discord.Embed(
        title="Bot latency",
        description=f"The current bot latency is approximately `{bot_latency}ms`",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    await message.channel.send(embed=embed)


async def server_command(message: discord.Message) -> None:
    try:
        guild = message.guild

        if not guild.me.guild_permissions.administrator:
            embed = discord.Embed(
                title="Permission Denied",
                description="You need administrator permissions to gather all server stats.",
                color=color_manager.get_color("Red"),
            )
            embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
            await message.channel.send(embed=embed)
            return

        if CRAC.intents.members:
            try:
                await guild.chunk()
            except discord.HTTPException:
                log_info("Failed to fetch all members. Some stats may be incomplete.")

        embed = discord.Embed(
            title=f"{guild.name} Server Stats",
            color=color_manager.get_color("Blue"),
            timestamp=datetime.datetime.utcnow(),
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name="Server ID", value=guild.id, inline=True)
        embed.add_field(
            name="Owner",
            value=guild.owner.mention if guild.owner else "Unknown",
            inline=True,
        )
        embed.add_field(
            name="Created At",
            value=f"<t:{int(guild.created_at.timestamp())}:F>",
            inline=True,
        )
        embed.add_field(
            name="Boost Level", value=f"Level {guild.premium_tier}", inline=True
        )
        embed.add_field(
            name="Boost Count", value=guild.premium_subscription_count, inline=True
        )

        total_members = guild.member_count
        bots = sum(1 for m in guild.members if m.bot)
        embed.add_field(name="Members", value=total_members, inline=True)
        embed.add_field(name="Bots", value=bots, inline=True)

        embed.add_field(name="Total Channels", value=len(guild.channels), inline=True)
        embed.add_field(name="Roles", value=len(guild.roles), inline=True)

        if guild.description:
            embed.add_field(name="Description", value=guild.description, inline=False)
        if guild.banner:
            embed.set_image(url=guild.banner.url)

        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)

        await message.channel.send(embed=embed)

    except discord.Forbidden:
        await send_error_embed(
            message,
            "Permission Error",
            "I don't have permission to access some server information.",
        )
    except discord.HTTPException as e:
        await send_error_embed(message, "HTTP Error", f"An HTTP error occurred: {e}")
    except Exception as e:
        await send_error_embed(
            message, "Unexpected Error", f"An unexpected error occurred: {e}"
        )
        log_info(f"Unexpected error in server command: {e}")


@CRAC.event
async def on_message_delete(message):
    if message.author == CRAC.user:
        return

    channel = CRAC.get_channel(LOGGING_CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title="Message Deleted",
        color=color_manager.get_color("Red"),
        timestamp=datetime.datetime.utcnow(),
    )
    embed.add_field(name="Author", value=message.author.mention)
    embed.add_field(name="Channel", value=message.channel.mention)
    embed.add_field(name="Content", value=message.content or "No content")

    if message.attachments:
        embed.add_field(
            name="Attachments", value="\n".join([a.url for a in message.attachments])
        )

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=embed)


@CRAC.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if before.author == CRAC.user:
        return

    channel = CRAC.get_channel(LOGGING_CHANNEL_ID)
    if not channel:
        return

    if before.content == after.content:
        return

    embed = discord.Embed(
        title="Message Edited",
        color=color_manager.get_color("Orange"),
        timestamp=datetime.datetime.utcnow(),
    )
    embed.add_field(name="Author", value=before.author.mention)
    embed.add_field(name="Channel", value=before.channel.mention)
    embed.add_field(name="Before", value=before.content or "No content")
    embed.add_field(name="After", value=after.content or "No content")

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=embed)
```

# src\utils\helper.py

```py
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
        richPrint(f"WARNING: Config file not found at {config_path}. Using default configuration.")
        return {"default_prefix": "?", "guilds": {}}
    except json.JSONDecodeError:
        richPrint(f"ERROR: Invalid JSON in config file {config_path}. Using default configuration.")
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
    richPrint(f"[bold][blue]INFO[/blue][/bold] {value}")

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
```

# website\articles\articles.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Articles</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Articles">
    <meta property="og:description" content="Explore all articles about CRAC Bot, including guides on commands, configuration, and feedback submission.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/articles">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/articles" class="hover:text-blue-600 transition">Articles</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <h2 class="text-4xl font-bold mb-8 text-center">CRAC Bot Articles</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Config Guide Article -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Configuration Guide</h3>
                    <p class="text-gray-600 mb-4">Learn how to configure CRAC Bot for your server's needs.</p>
                    <div class="flex items-center justify-between mt-4">
                        <div class="flex items-center">
                            <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-8 h-8 rounded-full mr-2">
                            <span class="text-sm text-gray-600">Nerd Bear</span>
                        </div>
                        <span class="text-sm text-gray-500">5 min read</span>
                    </div>
                    <a href="/support/article/config-guide" class="mt-4 inline-block text-blue-600 hover:text-blue-800">Read More →</a>
                </div>
            </div>

            <!-- Commands Guide Article -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Commands Guide</h3>
                    <p class="text-gray-600 mb-4">Explore all available commands and how to use them effectively.</p>
                    <div class="flex items-center justify-between mt-4">
                        <div class="flex items-center">
                            <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-8 h-8 rounded-full mr-2">
                            <span class="text-sm text-gray-600">Nerd Bear</span>
                        </div>
                        <span class="text-sm text-gray-500">8 min read</span>
                    </div>
                    <a href="/support/article/commands-guide" class="mt-4 inline-block text-blue-600 hover:text-blue-800">Read More →</a>
                </div>
            </div>

            <!-- Feedback Submission Article -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Submitting Feedback</h3>
                    <p class="text-gray-600 mb-4">Learn how to submit feedback to help improve CRAC Bot.</p>
                    <div class="flex items-center justify-between mt-4">
                        <div class="flex items-center">
                            <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-8 h-8 rounded-full mr-2">
                            <span class="text-sm text-gray-600">Nerd Bear</span>
                        </div>
                        <span class="text-sm text-gray-500">3 min read</span>
                    </div>
                    <a href="/support/article/add-feedback" class="mt-4 inline-block text-blue-600 hover:text-blue-800">Read More →</a>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('.grid > div', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                stagger: 0.2,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# website\articles\commands.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Commands Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Commands Guide">
    <meta property="og:description" content="Learn how to use CRAC Bot's commands effectively for server management and user interaction.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/support/article/commands-guide">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">CRAC Bot Commands Guide</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">CRAC Bot Developer</p>
                    </div>
                </div>
                
                <div class="flex items-center text-gray-600 text-sm mb-6">
                    <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path>
                    </svg>
                    <time datetime="2024-10-17">October 17, 2024</time>
                    <span class="mx-2">•</span>
                    <span>4 min read</span>
                </div>

                <div class="prose max-w-none">
                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Getting Started with CRAC Bot Commands</h3>
                    <p class="mb-4">CRAC Bot comes packed with a variety of commands to help you manage your server and engage with your community. In this guide, we'll walk you through the most important commands and how to use them effectively.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Basic Command Structure</h4>
                    <p class="mb-4">All CRAC Bot commands start with a prefix. By default, this prefix is set to "?", but it can be customized in the config file. Here's the basic structure of a command:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?commandName [argument1] [argument2] ...</pre>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Essential Commands</h3>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">1. Help Command</h4>
                    <p class="mb-4">The help command is your go-to for information about all available commands:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?help</pre>
                    <p>This will display a list of all available commands along with a brief description of each.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">2. Moderation Commands</h4>
                    <p class="mb-4">CRAC Bot offers several moderation commands to help you manage your server:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>Kick:</strong> ?kick @user [reason]</li>
                        <li><strong>Ban:</strong> ?ban @user [reason]</li>
                        <li><strong>Unban:</strong> ?unban @user</li>
                        <li><strong>Timeout:</strong> ?timeout @user &lt;duration&gt; &lt;unit&gt; [reason]</li>
                    </ul>
                    <p>Remember, you need the appropriate permissions to use these commands.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">3. Fun and Utility Commands</h4>
                    <p class="mb-4">CRAC Bot also includes commands for entertainment and utility:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>Character Info:</strong> ?charinfo [character]</li>
                        <li><strong>Text-to-Speech:</strong> ?tts [message]</li>
                        <li><strong>Play Music:</strong> ?play [youtube_url]</li>
                        <li><strong>User Profile:</strong> ?profile @user</li>
                    </ul>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">4. Bot Management Commands</h4>
                    <p class="mb-4">For server administrators, there are commands to manage the bot itself:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>Shutdown:</strong> ?shutdown</li>
                        <li><strong>Start:</strong> ?start</li>
                        <li><strong>Change Nickname:</strong> ?nick @user [new_nickname]</li>
                    </ul>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Advanced Usage Tips</h3>
                    <p class="mb-4">Here are some tips to help you get the most out of CRAC Bot:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li>Use the ?help command followed by a specific command name for detailed usage information.</li>
                        <li>When using moderation commands, always provide a reason to maintain transparency.</li>
                        <li>The ?tts command is great for making announcements in voice channels.</li>
                        <li>Use ?profile to quickly get information about a user, including their roles and join date.</li>
                    </ul>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Troubleshooting Common Issues</h3>
                    <p class="mb-4">If you're experiencing issues with commands, try these steps:</p>
                    <ol class="list-decimal list-inside mb-4 space-y-2">
                        <li>Ensure you're using the correct prefix (default is "?").</li>
                        <li>Check that you have the necessary permissions for the command.</li>
                        <li>Verify that the bot is online and has the required permissions in your server.</li>
                        <li>If a command isn't working, try restarting the bot using the ?shutdown and ?start commands (admin only).</li>
                    </ol>

                    <p class="text-lg font-semibold mt-8">Remember, the key to effectively using CRAC Bot is experimentation. Don't be afraid to try out different commands and see how they can benefit your server!</p>

                    <div class="mt-8 p-4 bg-blue-100 rounded-md">
                        <p class="font-bold text-blue-800">Pro Tip:</p>
                        <p>Create a dedicated channel for bot commands to keep your main chat channels clutter-free. This also helps new users learn how to interact with the bot by seeing others use it.</p>
                    </div>
                </div>
            </div>
        </article>

        <div class="mt-8">
            <h3 class="text-2xl font-bold mb-4">Comments</h3>
            <p>No comments could be found for this article</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('article', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# website\articles\config.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Config Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
    
    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Config Guide">
    <meta property="og:description" content="Learn how to change and use the config file for CRAC Bot, a versatile Discord bot for server management and user interaction.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/support/article/config-guide">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">CRAC Bot Config Guide</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">CRAC Bot Developer</p>
                    </div>
                </div>
                
                <div class="flex items-center text-gray-600 text-sm mb-6">
                    <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path>
                    </svg>
                    <time datetime="2024-05-15">October 17, 2024</time>
                    <span class="mx-2">•</span>
                    <span>5 min read</span>
                </div>

                <div class="prose max-w-none">
                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Understanding the Config File</h3>
                    <p class="mb-4">The config file for CRAC Bot is a JSON file named <code class="bg-gray-100 p-1 rounded">config.json</code>. It contains various settings that control the bot's behavior. Let's dive into its structure and how you can customize it to suit your needs.</p>

                    <pre class="bg-gray-100 p-4 rounded-md mb-4 overflow-x-auto">
{
    "defaults": {
        "prefix": "?",
        "footer_text": "This bot is created and hosted by Nerd bear",
        "footer_icon": "https://as2.ftcdn.net/v2/jpg/01/17/00/87/1000_F_117008730_0Dg5yniuxPQLz3shrJvLIeBsPfPRBSE1.jpg"
    },
    "bot_version": "0.4.6",
    "bot_name": "CRAC",
    "tts_mode": "fast",
    "log_channel_id": "1290060885485948950",
    "tts_detector_factory_seed": "0",
    "colors": {
        "Red": "#FFB3BA",
        "Blue": "#B5DEFF"
        // ... other colors ...
    },
    "guilds": {
        "1288144110880030795": {
            "prefix": "*"
        }
    }
}
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Key Sections:</h4>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>defaults:</strong> Contains default settings for the bot.</li>
                        <li><strong>bot_version:</strong> The current version of the bot.</li>
                        <li><strong>bot_name:</strong> The name of the bot.</li>
                        <li><strong>tts_mode:</strong> The mode for text-to-speech functionality.</li>
                        <li><strong>log_channel_id:</strong> The ID of the channel where logs will be sent.</li>
                        <li><strong>colors:</strong> A list of color codes used for various bot functions.</li>
                        <li><strong>guilds:</strong> Server-specific settings, such as custom prefixes.</li>
                    </ul>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">How to Modify the Config File</h3>
                    <p class="mb-4">Customizing your CRAC Bot installation is straightforward. Follow these steps to modify the config file:</p>
                    <ol class="list-decimal list-inside mb-4 space-y-2">
                        <li>Locate the <code class="bg-gray-100 p-1 rounded">config.json</code> file in your bot's root directory.</li>
                        <li>Open the file with a text editor (e.g., Notepad++, Visual Studio Code).</li>
                        <li>Make your desired changes, ensuring to maintain the correct JSON format.</li>
                        <li>Save the file after making changes.</li>
                        <li>Restart the bot for the changes to take effect.</li>
                    </ol>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Common Modifications</h3>
                    <p class="mb-4">Let's explore some common modifications you might want to make to your CRAC Bot configuration:</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Changing the Default Prefix</h4>
                    <p class="mb-4">To change the default prefix, modify the "prefix" value under "defaults":</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"defaults": {
    "prefix": "!",  // Change '?' to your desired prefix
    ...
}
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Setting a Custom Prefix for a Specific Server</h4>
                    <p class="mb-4">To set a custom prefix for a specific server, add or modify an entry under "guilds":</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"guilds": {
    "YOUR_SERVER_ID": {
        "prefix": "$"  // Replace with your desired prefix
    }
}
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Changing the Bot Name</h4>
                    <p class="mb-4">To change the bot's name, modify the "bot_name" value:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"bot_name": "Your New Bot Name",
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Modifying Colors</h4>
                    <p class="mb-4">To change or add colors, modify the "colors" section:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"colors": {
    "Red": "#FF0000",
    "Blue": "#0000FF",
    "CustomColor": "#HEXCODE"
}
                    </pre>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Important Notes</h3>
                    <p class="mb-4">Before you start tweaking your config file, keep these important points in mind:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li>Always backup your config file before making changes.</li>
                        <li>Ensure your JSON syntax is correct to avoid errors.</li>
                        <li>Some changes may require a bot restart to take effect.</li>
                        <li>Be cautious when changing critical settings like log_channel_id.</li>
                    </ul>

                    <p class="text-lg font-semibold mt-8">Remember, customizing your CRAC Bot is all about making it work best for your server and community. Don't be afraid to experiment with different settings to find what works best for you!</p>

                    <div class="mt-8 p-4 bg-blue-100 rounded-md">
                        <p class="font-bold text-blue-800">Pro Tip:</p>
                        <p>Consider using a JSON validator tool to check your config file for syntax errors before restarting your bot. This can save you time and prevent potential issues.</p>
                    </div>
                </div>
            </div>
        </article>

        <div class="mt-8">
            <h3 class="text-2xl font-bold mb-4">Comments</h3>
            <p>No comments could be found for this article</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('article', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# website\articles\feedback.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Feedback Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Feedback Guide">
    <meta property="og:description" content="Learn how to submit feedback for CRAC Bot using the feedback command. Your input helps improve the bot!">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/support/article/add-feedback">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">Submitting Feedback for CRAC Bot</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">CRAC Bot Developer</p>
                    </div>
                </div>
                
                <div class="flex items-center text-gray-600 text-sm mb-6">
                    <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path>
                    </svg>
                    <time datetime="2024-10-17">October 17, 2024</time>
                    <span class="mx-2">•</span>
                    <span>3 min read</span>
                </div>

                <div class="prose max-w-none">
                    <h3 class="text-2xl font-bold mb-4 text-blue-600">The Importance of Your Feedback</h3>
                    <p class="mb-4">Your feedback is crucial for the continuous improvement of CRAC Bot. Whether you've encountered a bug, have a feature request, or simply want to share your thoughts, we want to hear from you! The feedback command makes it easy to submit your input directly through Discord.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Using the Feedback Command</h4>
                    <p class="mb-4">Submitting feedback is straightforward with the <code class="bg-gray-100 p-1 rounded">?feedback</code> command. Here's how to use it:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?feedback [your message]</pre>
                    <p>Replace [your message] with your actual feedback. Be as detailed as possible to help us understand your thoughts or the issue you're experiencing.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Examples of Good Feedback</h4>
                    <p class="mb-4">Here are some examples of effective feedback submissions:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><code class="bg-gray-100 p-1 rounded">?feedback The ?play command sometimes fails to join the voice channel. Could you look into this?</code></li>
                        <li><code class="bg-gray-100 p-1 rounded">?feedback I love the ?profile command! It would be great if it could also show the user's top 3 most active channels.</code></li>
                        <li><code class="bg-gray-100 p-1 rounded">?feedback The bot seems to lag when processing commands in servers with over 1000 members. Any way to optimize this?</code></li>
                    </ul>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">What Happens After You Submit Feedback</h4>
                    <p class="mb-4">After submitting your feedback:</p>
                    <ol class="list-decimal list-inside mb-4 space-y-2">
                        <li>Your feedback is securely stored in our database.</li>
                        <li>The development team regularly reviews all feedback submissions.</li>
                        <li>Your input may influence future updates and improvements to CRAC Bot.</li>
                        <li>For urgent issues, consider also reaching out through our support channels.</li>
                    </ol>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Best Practices for Submitting Feedback</h3>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li>Be specific: Provide as much detail as possible about your experience or suggestion.</li>
                        <li>One idea per submission: If you have multiple suggestions, submit them separately for easier processing.</li>
                        <li>Be constructive: Explain not just what you dislike, but how you think it could be improved.</li>
                        <li>Include context: Mention your server size, the command you were using, or any relevant settings.</li>
                    </ul>

                    <p class="text-lg font-semibold mt-8">Your feedback plays a vital role in shaping the future of CRAC Bot. We appreciate every submission and take your input seriously in our development process.</p>

                    <div class="mt-8 p-4 bg-blue-100 rounded-md">
                        <p class="font-bold text-blue-800">Pro Tip:</p>
                        <p>If you're reporting a bug, try to include steps to reproduce the issue. This helps our development team identify and fix the problem more quickly!</p>
                    </div>
                </div>
            </div>
        </article>

        <div class="mt-8">
            <h3 class="text-2xl font-bold mb-4">Comments</h3>
            <p>No comments could be found for this article</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('article', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# website\home-page.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC - Discord Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Home">
    <meta property="og:description" content="A versatile Discord bot for server management and user interaction. Features include moderation tools, customizable status, character info lookup, and message logging. Actively developed with frequent updates. Created by Nerd Bear for enhancing Discord communities.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-5xl font-bold mb-4 text-gray-900"><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Welcome to CRAC Bot</a></h2>
            <p class="text-xl mb-12 text-gray-600">The ultimate do-it-all Discord bot for moderation and fun!</p>
            <button id="cta-button" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-full transition shadow-lg">
                Add to Discord
            </button>
        </div>
    </main>

    <section id="features" class="container mx-auto mt-24 p-6">
        <h3 class="text-3xl font-bold mb-12 text-center text-gray-800">Features</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h4 class="text-xl font-bold mb-4 text-blue-600">Moderation</h4>
                <p class="text-gray-600">Powerful tools to keep your server safe and clean.</p>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h4 class="text-xl font-bold mb-4 text-blue-600">Fun Commands</h4>
                <p class="text-gray-600">Engage your community with interactive and entertaining commands.</p>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h4 class="text-xl font-bold mb-4 text-blue-600">Customization</h4>
                <p class="text-gray-600">Tailor CRAC to fit your server's unique needs.</p>
            </div>
        </div>
    </section>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const ctaButton = document.getElementById('cta-button');
            
            ctaButton.addEventListener('mouseenter', () => {
                gsap.to(ctaButton, {scale: 1.05, duration: 0.3});
            });

            ctaButton.addEventListener('mouseleave', () => {
                gsap.to(ctaButton, {scale: 1, duration: 0.3});
            });

            // Easter egg
            let clickCount = 0;
            ctaButton.addEventListener('click', (e) => {
                window.location.href = "https://discord.com/oauth2/authorize?client_id=1289921476614553672&permissions=8&integration_type=0&scope=bot";
            });
        })
    </script>
</body>
</html>
```

# website\privacy-policy.html

```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CRAC - Discord Bot | Privacy Policy</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

        <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

        <!-- Open Graph Meta Tags (for Discord and other platforms) -->
        <meta property="og:title" content="CRAC Bot | Privacy Policy">
        <meta property="og:description" content="Privacy Policy for CRAC Bot - Learn how we collect, use, and protect your data when you use our Discord bot.">
        <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
        <meta property="og:url" content="https://crac.nerd-bear.org/privacy">
        <meta property="og:type" content="website">

        <style>
            .pfp-hover {
                transition: transform 0.3s ease-in-out;
            }
            
            .pfp-hover:hover {
                transform: scale(1.1);
            }
        </style>
    </head>

    <body class="bg-gray-50 text-gray-800">
        <nav class="container mx-auto p-6">
            <div class="flex justify-between items-center">
                <h1 class="text-3xl font-bold text-blue-600">
                    <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
                </h1>
                <ul class="flex space-x-6">
                    <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                    <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                    <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                    <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
                </ul>
            </div>
        </nav>

        <main class="container mx-auto mt-24 p-6">
            <div class="flex flex-col items-center mb-12">
                <a href="https://crac.nerd-bear.org/" class="mb-8">
                    <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
                </a>
                <h2 class="text-4xl font-bold mb-4 text-gray-900">
                    <a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Privacy Policy</a>
                </h2>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h3 class="text-2xl font-bold mb-4 text-blue-600">1. Information We Collect</h3>
                <p class="mb-6">When you use CRAC Bot, we may collect certain information such as your Discord user ID, server ID, message content when using bot commands, and other relevant data necessary for the bot's functionality.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">2. How We Use Your Information</h3>
                <p class="mb-6">We use the collected information to provide and improve CRAC Bot's services, including command execution, server management, and user interaction. We do not sell or share your personal information with third parties.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">3. Data Storage and Security</h3>
                <p class="mb-6">We take reasonable measures to protect your data from unauthorized access or disclosure. However, no method of transmission over the internet or electronic storage is 100% secure.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">4. Your Rights</h3>
                <p class="mb-6">You have the right to access, correct, or delete your personal information. To exercise these rights, please contact us using the information provided in the "Contact Us" section.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">5. Changes to This Privacy Policy</h3>
                <p class="mb-6">We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">6. Compliance with Discord's Policies</h3>
                <p class="mb-6">CRAC Bot complies with Discord's Developer Terms of Service and Developer Policy. We do not collect or use any data beyond what is necessary for the bot's functionality and what is allowed by Discord's policies.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">7. Children's Privacy</h3>
                <p class="mb-6">CRAC Bot is not intended for use by children under the age of 13. We do not knowingly collect personal information from children under 13. If you are a parent or guardian and you are aware that your child has provided us with personal information,
                    please contact us.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">8. Contact Us</h3>
                <p>If you have any questions about this Privacy Policy, please contact us at crac@nerd-bear.org.</p>
            </div>
        </main>

        <footer class="bg-gray-100 mt-24 py-8">
            <div class="container mx-auto text-center text-gray-600">
                <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
                <div class="mt-4">
                    <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                    <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                    <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
                </div>
            </div>
        </footer>
    </body>
</html>
```

# website\terms-of-use.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC - Discord Bot | Terms of Use</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Terms of Use">
    <meta property="og:description" content="Terms of Use for CRAC Bot - A versatile Discord bot for server management and user interaction. Please read these terms carefully before using CRAC Bot.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/terms">
    <meta property="og:type" content="website">
    
    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Terms of Use</a>
            </h2>
        </div>

        <div class="bg-white p-8 rounded-lg shadow-md">
            <h3 class="text-2xl font-bold mb-4 text-blue-600">1. Acceptance of Terms</h3>
            <p class="mb-6">By using CRAC Bot, you agree to these Terms of Use. If you disagree with any part of these terms, please do not use our bot.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">2. Use of the Bot</h3>
            <p class="mb-6">CRAC Bot is provided for Discord server management and entertainment purposes. You agree to use it only for its intended purposes and in compliance with Discord's Terms of Service.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">3. User Responsibilities</h3>
            <p class="mb-6">You are responsible for all activities that occur under your Discord account while using CRAC Bot. Do not use the bot for any illegal or unauthorized purpose.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">4. Modifications to Bot or Terms</h3>
            <p class="mb-6">We reserve the right to modify or discontinue CRAC Bot at any time. We may also revise these Terms of Use at our discretion. Continued use of the bot after any changes constitutes acceptance of those changes.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">5. Limitation of Liability</h3>
            <p class="mb-6">CRAC Bot is provided "as is" without warranties of any kind. We are not liable for any damages or losses related to your use of the bot.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">6. Privacy</h3>
            <p class="mb-6">Our use and collection of your information is governed by our Privacy Policy. By using CRAC Bot, you consent to our data practices as described in that policy.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">7. Termination</h3>
            <p class="mb-6">We may terminate or suspend your access to CRAC Bot immediately, without prior notice, for conduct that we believe violates these Terms of Use or is harmful to other users of the bot, us, or third parties, or for any other reason.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">8. Governing Law</h3>
            <p class="mb-6">These Terms shall be governed by and construed in accordance with the laws of United States of America and the United Kingdom, without regard to its conflict of law provisions.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">9. Contact Us</h3>
            <p>If you have any questions about these Terms, please contact us at crac@nerd-bear.org.</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>
</body>
</html>
```

# website\versions.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Version History</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Version History">
    <meta property="og:description" content="Explore the version history of CRAC Bot, a versatile Discord bot for server management and user interaction. See the latest updates, features, and improvements.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/versions">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">CRAC Bot Version History</a>
            </h2>
        </div>
        
        <div class="mb-8">
            <input type="text" id="search-input" placeholder="Search versions..." class="w-full p-2 border border-gray-300 rounded-md">
        </div>

        <div class="mb-8" id="toc">
            <h3 class="text-2xl font-bold mb-4">Table of Contents</h3>
            <ul class="space-y-2">
                <li><a href="#v0-4-4" class="text-blue-600 hover:underline">CRAC 0.4.4 Beta pre-release</a></li>
                <li><a href="#v0-4-3" class="text-blue-600 hover:underline">CRAC 0.4.3 Beta pre-release</a></li>
                <li><a href="#v0-4-2" class="text-blue-600 hover:underline">CRAC 0.4.2 Beta pre-release</a></li>
                <li><a href="#v0-4-1" class="text-blue-600 hover:underline">CRAC 0.4.1 Beta pre-release</a></li>
            </ul>
        </div>
        
        <div class="space-y-12" id="versions-container">
            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-4">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.4 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.04 MB (~43.1 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 05/10/2024 2:45 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.4" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.4</a>
                
                <p class="mb-4">This is a simple beta testing release with around 17 simple commands, the commands are: help, charinfo, tts, profile, play, join, leave, timeout, kick, ban, unban, shutdown, start, stream, play, watch, and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behaviour, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>The charinfo command still has no support for a large number of special characters</li>
                    <li>Ban & Unban commands don't handle all exceptions and may cause undefined/buggy behaviour</li>
                    <li>There is no untimeout command and timeouts can only be in one unit of one amount</li>
                    <li>Status config commands still exist and have not been removed yet</li>
                    <li>Join/leave commands still not added to help embed</li>
                    <li>Many commands missing proper or any error handling</li>
                    <li>More unknown issues may exist</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-green-600">Change log:</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>Changed the default Logger construct-er log output path to ./logs/output.log instead of ./logs/output.log</li>
                    <li>Added tts command</li>
                    <li>Added tts command to the help embed</li>
                    <li>Added leave command</li>
                    <li>Added join command</li>
                    <li>Added run logs to join the command</li>
                    <li>Added run logs to leave command</li>
                    <li>Added run logs to TTS command</li>
                    <li>Changed tts command messages to be embedded</li>
                    <li>Added more error handling to the tts command</li>
                    <li>Updated tts command success embed to have a channel link and not a name</li>
                    <li>Added play command</li>
                    <li>Patched play command to not leave after starting to play</li>
                    <li>Added play command to help embed</li>
                    <li>Added profile command</li>
                    <li>Added profile command to help embed</li>
                    <li>Added failsafes and exception handling in the profile command</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-blue-600">Update notes:</h4>
                <p class="mb-4">I will remove all status config commands as they affect the bot across all guilds (Servers) and are just added as a proof of concept. The commands and features I will be adding are config files, untimeout commands, voice chat mute commands, per guild config, music features, and other fun features! Another feature, probably the biggest one (since it will allow for a lot of new features) will be the music queue backend change since it will allow for many new features.</p>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-3">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.3 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.03 MB (~30.8 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 04/10/2024 2:17 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.3" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.3</a>
                
                <p class="mb-4">This is a simple beta testing release with around 12 simple commands, the commands are: help, charinfo, timeout, kick, ban, unban, shutdown, start, stream, play, watch, and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behavior, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>The charinfo command still has no support for a large number of special characters</li>
                    <li>Ban & Unban commands don't handle all exceptions and may cause undefined/buggy behavior</li>
                    <li>There is no untimeout command and timeouts can only be in one unit of one amount</li>
                    <li>Status config commands still exist and have not been removed yet</li>
                    <li>More unknown issues may exist</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-green-600">Change log:</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>Added unban command</li>
                    <li>Added unban command to help embed</li>
                    <li>Added exception handling to all cases of unban command</li>
                    <li>Changed Bot Intents from default to all</li>
                    <li>Changed the Logger class constructer to default to a relative output path</li>
                    <li>Ran blacklint on source code to increase readability</li>
                    <li>Specified bot command parameter types for syntax highlighting</li>
                    <li>Added timeout command</li>
                    <li>Added timeout command to help embed</li>
                    <li>Changed the timeout command to send a dm to the user</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-blue-600">Update notes:</h4>
                <p class="mb-4">I will be removing all status config commands as they affect the bot across all guilds (Servers) and are just added as a proof of concept. The commands and features I will be adding are config files, untimeout command, voice chat mute commands, per guild config, music features, and other fun features!</p>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-2">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.2 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.02 MB (~18.3 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 03/10/2024 3:39 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.2" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.2</a>
                
                <p class="mb-4">This is a simple beta testing release with around 10 simple commands, the commands are: help, charinfo, kick, ban, shutdown, start, stream, play, watch and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behaviour, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>The charinfo command still has no support for a large number of special characters</li>
                    <li>More unknown issues may exist</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-green-600">Change log:</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>Removed all logger.info logs</li>
                    <li>Added footer to the DM_EMBED of the word filter</li>
                    <li>Added the charinfo command to the help embed</li>
                    <li>Changed the logger initialization to be a relative logger output path</li>
                    <li>Added logger info level logs to show what user ran what command when</li>
                </ul>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-1">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.1 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.02 MB (~18.3 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 02/10/2024 4:09 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.1" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.1</a>
                
                <p class="mb-4">This is a simple beta testing release with around 10 simple commands, the commands are: help, charinfo, kick, ban, shutdown, start, stream, play, watch and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behaviour, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>May include hard-coded paths to files that may not exist or path formats meant for another OS</li>
                    <li>More unknown issues may exist</li>
                </ul>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.getElementById('search-input');
            const versionContainers = document.querySelectorAll('#versions-container > div');

            // Search functionality
            searchInput.addEventListener('input', () => {
                const searchTerm = searchInput.value.toLowerCase();

                versionContainers.forEach(container => {
                    const versionContent = container.textContent.toLowerCase();
                    if (versionContent.includes(searchTerm)) {
                        container.style.display = 'block';
                    } else {
                        container.style.display = 'none';
                    }
                });
            });

            // Animation
            gsap.from('#versions-container > div', {
                duration: 0.5,
                opacity: 0,
                y: 50,
                stagger: 0.2,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

