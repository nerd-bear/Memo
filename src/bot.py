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