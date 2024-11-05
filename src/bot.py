print("\n\n")  # Needed as some restarts sometimes print on non-empty lines

import asyncio
import datetime
import os
import random
import sys
import functools
import unicodedata

import disnake
from disnake.ext import commands
from disnake.activity import Activity

from rich.console import Console
from rich.console import Text

from deep_translator import GoogleTranslator
from textblob import TextBlob
import yt_dlp

from db_manager import history, feedback, guild_configs

from src.utils.helper import *
from src.utils.sha3 import *
from src.utils.chatbot import *
from src.utils.config_manager import *
from src.utils.word_filter import *

from src.cogs import *

log_info("Loaded all needed imports", True)


CONFIG_PATH = "config.json"
log_info("Loaded config path", True)

log_info("Loading Config", True)
config = load_config(CONFIG_PATH)
log_info("Completed loading config", True)

log_info("Loading default values into Memory", True)
color_manager = ColorManager(config)
log_info("Initialized color manager", True)

FOOTER_TEXT = config["defaults"].get("footer_text")
log_info("Loaded footer text", True)
FOOTER_ICON = config["defaults"].get("footer_icon")
log_info("Loaded footer icon", True)

prefix = config["defaults"].get("prefix", "?")
log_info("Loaded bot prefix", True)
BOT_NAME = config.get("bot_name", "Memo Bot")
log_info("Loaded bot name", True)
BOT_VERSION = config.get("bot_version", "1.0.0")
log_info("Loaded bot version", True)

TTS_MODE = config.get("tts_mode", "normal")
log_info("Loaded tts mode", True)

SYSTEM_PROMT = config.get("system_prompt", "none")
log_info("Loaded system prompt", True)

LOGGING_CHANNEL_ID = int(config.get("log_channel_id", 0))
log_info("Loaded logging channel id", True)

intents = disnake.Intents.all()
log_info("Initialized intents", True)

log_info("Initialized command sync flags", True)

crp_activity = Activity(
    name="Hidden context info",
    type=disnake.ActivityType.custom,
    state=config.get("bot_status", "Run ?help to get help"),
)

log_info("Initialized custom crp activity", True)

Memo = commands.Bot(command_prefix="?", 
                    intents=intents, 
                    activity=crp_activity
                    )

log_info("Initialized bot", True)

chat_bot = ChatBot()

log_info("Initialized chat bot", True)

chat_bot.set_system_prompt(SYSTEM_PROMT)

log_info("Set system prompt", True)

console = Console()
log_info("Initialized console", True)

afk_users: dict[int, str] = {}

set_langdetect_seed(config.get("tts_detector_factory_seed", 0))
log_info("Loaded tts detector factory seed", True)

bot_active = True
log_info("Initialized bot to be active", True)
log_info("Completed loading default values into Memory", True)


async def get_info_text() -> str:
    return f"""
    {BOT_NAME} v{BOT_VERSION}
    Logged in as {Memo.user.name} (ID: {Memo.user.id})
    Connected to {len(Memo.guilds)} guilds
    Bot is ready to use. Ping: {fetch_latency(Memo)}ms
    Prefix: {prefix}
    Initialization complete.
    """


async def restart_memo() -> None:
    log_info("Restarting Memo...")

    for vc in Memo.voice_clients:
        await vc.disconnect(force=True)

    if hasattr(Memo.http, "_client_session") and Memo.http._client_session:
        await Memo.http._client_session.close()
        await asyncio.sleep(1)

    try:
        await Memo.close()
    except:
        pass

    os.execv(sys.executable, ["python", "-B"] + sys.argv)


async def auto_restart():
    while True:
        await asyncio.sleep(21600)
        log_info("Auto restarting Memo...", False)
        await restart_memo()


async def auto_latency_check():
    last_ping = 0
    while True:
        latency = fetch_latency(Memo)
        
        text = Text()
        text.append(f"[{datetime.datetime.utcnow().__format__('%H:%M:%S')}]", style="bold cyan")
        text.append(" [INFO]", style="bold blue")
        text.append(" Latency: ", style="bold")
        text.append(f"{latency}ms", style="bold green")
        text.append(" Last ping: ", style="bold")
        text.append(f"{last_ping}ms", style="bold yellow")
        
        console.print(text)
        
        last_ping = latency
        await asyncio.sleep(20)


def debug_command(func):
    @functools.wraps(func)
    async def wrapper(message: disnake.Message, *args: any, **kwargs: any):
        embed = disnake.Embed(
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


from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Group

@Memo.event
async def on_ready() -> None:
    Memo.loop.create_task(auto_restart())
    Memo.loop.create_task(auto_latency_check())

    Memo.load_extension("src.cogs.member_join")
    Memo.load_extension("src.cogs.member_remove")
    Memo.load_extension("src.cogs.new_guild")

    log_info(f"Successfully started {BOT_NAME} {BOT_VERSION}v", startup=True)

    info_text = await get_info_text()

    log_info(f"Bot name: {BOT_NAME}", info=True)
    log_info(f"Bot version: {BOT_VERSION}", info=True)
    log_info(f"Logged in as {Memo.user.name} (ID: {Memo.user.id})", info=True)
    log_info(f"Connected to {len(Memo.guilds)} guilds", info=True)
    log_info(f"Prefix: {prefix}", info=True)
    log_info(f"Bot is ready to use. Ping: {fetch_latency(Memo)}ms", info=True)


    channel = Memo.get_channel(LOGGING_CHANNEL_ID)

    if channel:
        embed = disnake.Embed(
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


@Memo.event
async def on_message(message: disnake.Message) -> None:
    guild_prefix = (
        (
            guild_configs.get_guild_config(SHA3.hash_256(message.guild.id))[
                "command_prefix"
            ]
            if guild_configs.get_guild_config(SHA3.hash_256(message.guild.id)) != None
            else "?"
        )
        if isinstance(message.channel, disnake.DMChannel) == False
        else "?"
    )
    global bot_active

    if message.author == Memo.user:
        return

    if isinstance(message.channel, disnake.DMChannel):
        await send_error_embed(
            message,
            "Please run in server",
            "When running commands or interacting with the bot, please do so in the server as we do not currently support DM interactions.",
            FOOTER_TEXT,
            FOOTER_ICON,
            color_manager,
        )
        return

    if not message.content.startswith(guild_prefix):
        if not bot_active:
            return

        content = message.content.lower().strip()

        if any(is_bad_word(word) for word in content.split()):
            await handle_inappropriate_word(message)

        if message.author.id in afk_users:
            embed = disnake.Embed(
                title="AFK Status Removed",
                description=f"{message.author.mention} is no longer AFK. Welcome back!",
                color=color_manager.get_color("Blue"),
            )
            embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
            await message.channel.send(embed=embed)
            del afk_users[message.author.id]

        for mentioned_user in message.mentions:
            if mentioned_user.id in afk_users:
                embed = disnake.Embed(
                    title="User is AFK",
                    description=f"{mentioned_user.mention} is currently AFK.\nMessage: {afk_users[mentioned_user.id]}",
                    color=color_manager.get_color("Yellow"),
                )
                embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
                await message.channel.send(embed=embed)

        if message.reference and message.reference.resolved:
            referenced_user_id = message.reference.resolved.author.id
            if referenced_user_id in afk_users:
                referenced_user = message.reference.resolved.author
                embed = disnake.Embed(
                    title="User is AFK",
                    description=f"{referenced_user.mention} is currently AFK.\nMessage: {afk_users[referenced_user_id]}",
                    color=color_manager.get_color("Yellow"),
                )
                embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
                await message.channel.send(embed=embed)

        if Memo.user in message.mentions:
            await message.channel.send(
                f"Hello {message.author.mention}! You mentioned me. How can I help you?"
            )
        return

    if message.content.startswith("?") and len(message.content.strip()) <= 1:
        return

    if not bot_active and message.content != f"{guild_prefix}start":
        embed = disnake.Embed(
            title="Bot Offline",
            description=f"{BOT_NAME} is currently offline. Use {guild_prefix}start to activate.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    command = message.content.split()[0][len(guild_prefix) :].lower()
    args = message.content.split()[1:]

    history.add_history(
        SHA3.hash_256(message.author.id),
        SHA3.hash_256(str(message.guild.id)),
        command,
        args,
    )

    commands_dict = {
        "help": help_command,
        "timeout": timeout_command,
        "kick": kick_command,
        "ban": ban_command,
        "unban": unban_command,
        "shutdown": shutdown_command,
        "start": start_command,
        "restart": restart_command,
        "charinfo": charinfo_command,
        "join": join_vc_command,
        "leave": leave_vc_command,
        "tts": tts_command,
        "play": play_command,
        "translate": translate_command,
        "ping": ping_command,
        "nick": nick_command,
        "profile": profile_command,
        "feedback": feedback_command,
        "server": server_command,
        "joke": joke_command,
        "coin": coin_command,
        "8ball": eight_ball_command,
        "mute": vc_mute_command,
        "unmute": vc_unmute_command,
        "deafen": vc_deafen_command,
        "undeafen": vc_undeafen_command,
        "setprefix": set_prefix_command,
        "chat": chat_command,
        "afk": afk_command,
        "kiss": kiss_command,
        "rps": rps_command,
        "man": man_command,
        "purge": purge_command,
        "spellcheck": spellcheck_command,
        "setup": setup_command,
    }

    if command not in commands_dict:
        embed = disnake.Embed(
            title="Invalid Command",
            description=f"The command you are running is not valid. Please run `{guild_prefix}help` for a list of commands and their usages!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        await commands_dict[command](message, guild_prefix)

    except Exception as e:
        embed = disnake.Embed(
            title="An Error Occurred",
            description=f"An error occurred while executing the command. Please try again later.\nError: {str(e)}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        log_info(f"An error occurred while executing command '{command}': {str(e)}", error=True)
        return


async def handle_inappropriate_word(message: disnake.Message) -> None:
    user = message.author
    channel = message.channel

    content = message.content.lower().strip()
    words = content.split()

    bad_word_indices = [i for i, word in enumerate(words) if is_bad_word(word)]

    if not bad_word_indices:
        return

    highlighted_content = message.content
    for index in bad_word_indices:
        bad_word = words[index]
        highlighted_content = highlighted_content.replace(bad_word, f"**{bad_word}**")

    context_words = []
    for index in bad_word_indices:
        before_word = words[index - 1] if index > 0 else ""
        after_word = words[index + 1] if index < len(words) - 1 else ""
        context_words.append(f"{before_word} **{words[index]}** {after_word}")

    dm_embed = disnake.Embed(
        title="Inappropriate Word Detected",
        description=f"{BOT_NAME} has detected an inappropriate word! Please do not send racist words in our server! Moderators may have been informed!",
        color=color_manager.get_color("Red"),
    )
    dm_embed.add_field(
        name="Rules",
        value="Please read the rules before sending such messages!",
        inline=False,
    )
    dm_embed.add_field(name="Server", value=f"{message.guild.name}", inline=False)
    dm_embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    dm_embed.set_thumbnail(url=message.guild.icon.url)

    try:
        await user.send(embed=dm_embed)
    except disnake.errors.Forbidden:
        pass

    await message.delete()

    channel_embed = disnake.Embed(
        title="Inappropriate Word Detected",
        description=f"User {user.mention} tried to send a word that is marked not allowed!",
        color=color_manager.get_color("Red"),
    )
    channel_embed.add_field(
        name="Context",
        value="\n".join(context_words),
        inline=False,
    )
    channel_embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=channel_embed)


async def help_command(message: disnake.Message, prefix: str = "?") -> None:
    embed = fetch_help_embed(
        color_manager, BOT_NAME, BOT_VERSION, prefix, FOOTER_TEXT, FOOTER_ICON
    )
    await message.channel.send(embed=embed)


async def kick_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.kick_members:
        embed = disnake.Embed(
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
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to kick. Usage: {prefix}kick @user [reason]",
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
            embed=disnake.Embed(
                title="You've wBeen Kicked",
                description=f"You were kicked from {message.guild.name}.\n**Reason:** {reason}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.kick(reason=reason)
    embed = disnake.Embed(
        title="User Kicked",
        description=f"{member.mention} has been kicked.\n**Reason:** {reason}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def ban_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.ban_members:
        embed = disnake.Embed(
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
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to ban. Usage: {prefix}ban @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.guild.get_member(message.mentions[0].id)

    if member is None:
        embed = disnake.Embed(
            title="Member Not Found",
            description=f"Please mention a user to ban. Usage: {prefix}ban @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    reason = " ".join(message.content.split()[2:]) or "No reason provided"

    try:
        await member.send(
            embed=disnake.Embed(
                title="You've Been Banned",
                description=f"You were banned from {message.guild.name}.\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.ban(reason=reason)
    embed = disnake.Embed(
        title="User Banned",
        description=f"{member.mention} has been banned.\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


@debug_command
async def shutdown_command(message: disnake.Message, prefix: str = "?") -> None:
    global bot_active
    if not message.author.guild_permissions.administrator:
        embed = disnake.Embed(
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
    await Memo.change_presence(status=disnake.Status.invisible)

    for vc in Memo.voice_clients:
        await vc.disconnect()

    embed = disnake.Embed(
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
async def start_command(message: disnake.Message, prefix: str = "?") -> None:
    global bot_active
    if not message.author.guild_permissions.administrator:
        embed = disnake.Embed(
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
    await Memo.change_presence(
        status=disnake.Status.online,
        activity=crp_activity,
    )
    embed = disnake.Embed(
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


async def charinfo_command(message: disnake.Message, prefix: str = "?") -> None:
    try:
        argument_text = " ".join(message.content.split()[1:])
        char_text = argument_text[0]
    except IndexError:
        await message.channel.send(
            embed=disnake.Embed(
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

    embed = disnake.Embed(
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
        file = disnake.File(image_path, filename="character.png")
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


async def unban_command(message: disnake.Message, prefix: str = "?") -> None:
    """
    Unbans a user from the guild and sends them an invite link.

    Args:
        message (disnake.Message): The message that triggered the command
        prefix (str, optional): Command prefix. Defaults to "?"
    """
    if (
        not message.author.guild_permissions.administrator
        or not message.author.guild_permissions.ban_members
    ):
        embed = disnake.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    args = message.content.strip().split()
    if len(args) < 2:
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Please provide a user ID to unban. Usage: {prefix}unban [user_id]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        user_id = int(args[1])
    except ValueError:
        embed = disnake.Embed(
            title="Invalid User ID",
            description="Please provide a valid user ID.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        ban_entry = await message.guild.fetch_ban(disnake.Object(id=user_id))
        banned_user = ban_entry.user

        if not banned_user:
            embed = disnake.Embed(
                title="User Not Found",
                description="This user is not banned from the server.",
                color=color_manager.get_color("Red"),
            )
            embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
            await message.channel.send(embed=embed)
            return

        try:
            invite = await message.channel.create_invite(
                max_uses=1,
                reason=f"Unban invite for {banned_user.name}#{banned_user.discriminator}",
            )
        except disnake.errors.Forbidden:
            invite = None

        await message.guild.unban(banned_user, reason=f"Unbanned by {message.author}")

        if invite:
            try:
                embed = disnake.Embed(
                    title="You've Been Unbanned!",
                    description=f"You have been unbanned from {message.guild.name}.",
                    color=color_manager.get_color("Green"),
                )
                embed.add_field(
                    name="Invite Link",
                    value=f"[Click here to join]({invite.url})",
                    inline=False,
                )
                await banned_user.send(embed=embed)
            except disnake.errors.HTTPException:
                pass

        embed = disnake.Embed(
            title="User Unbanned",
            description=f"Successfully unbanned {banned_user.mention}, invite link: {invite}",
            color=color_manager.get_color("Green"),
        )
        if invite:
            embed.add_field(
                name="Invite Status",
                value="Tried to send a invite link to the user.",
                inline=False,
            )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)

    except disnake.errors.NotFound:
        embed = disnake.Embed(
            title="User Not Found",
            description="This user is not banned from the server.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)

    except disnake.errors.Forbidden as e:
        embed = disnake.Embed(
            title="Permission Error",
            description="I don't have permission to unban members.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)

    except disnake.errors.HTTPException as e:
        embed = disnake.Embed(
            title="Error",
            description=f"An error occurred while unbanning the user: {str(e)}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)


async def timeout_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.moderate_members:
        embed = disnake.Embed(
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
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Usage: {prefix}timeout @user <duration> <unit> [reason]",
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
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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
        await member.timeout(duration=time_delta, reason=reason)
        embed = disnake.Embed(
            title="User Timed Out",
            description=f"{member.mention} has been timed out for {duration}{unit}.\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",  # Fixed: Removed duplicate moderator mention
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

        try:
            dm_embed = disnake.Embed(
                title="You were timed out",
                description=f"You have been timed out for {duration}{unit}.",
                color=color_manager.get_color("Blue"),
            )
            dm_embed.add_field(name="Reason", value=reason, inline=True)
            dm_embed.add_field(name="Moderator", value=message.author.name, inline=True)
            dm_embed.set_footer(
                text=FOOTER_TEXT,
                icon_url=FOOTER_ICON,
            )
            await member.send(embed=dm_embed)
        except:
            pass 

    except disnake.errors.Forbidden:
        embed = disnake.Embed(
            title="Permission Error",
            description="I don't have permission to timeout this user.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

    except disnake.errors.HTTPException:
        embed = disnake.Embed(
            title="Error",
            description="Failed to timeout the user. The duration might be too long.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)


async def join_vc_command(message: disnake.Message, prefix: str = "?") -> None:
    try:
        channel = Memo.get_channel(message.author.voice.channel.id)
        await channel.connect()
    except Exception as e:
        log_info("Error connecting to voice channel", error=True)


async def leave_vc_command(message: disnake.Message, prefix: str = "?") -> None:
    try:
        await message.guild.voice_client.disconnect()
    except Exception as e:
        pass


async def tts_command(message: disnake.Message, prefix: str = "?") -> None:
    text = " ".join(message.content.split()[1:])

    if not text:
        embed = disnake.Embed(
            title="Missing arguments",
            description=f"Please make sure you pass some text for the TTS command. Usage: {prefix}tts [message]",
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
        embed = disnake.Embed(
            title="Error occurred",
            description=f"A issue occurred during the generation of the Text-to-Speech mp3 file! Usage: {prefix}tts [message]",
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
        embed = disnake.Embed(
            title="Join voice channel",
            description=f"Please join a voice channel to use this command! Usage: {prefix}tts [message]",
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
    except disnake.ClientException:
        vc = message.guild.voice_client

    if vc.is_playing():
        vc.stop()

    vc.play(
        disnake.FFmpegPCMAudio(source=output_file),
        after=lambda e: asyncio.run_coroutine_threadsafe(vc.disconnect(), Memo.loop),
    )

    while vc.is_playing():
        await asyncio.sleep(0.1)

    if os.path.exists(output_file):
        os.remove(output_file)

    embed = disnake.Embed(
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


async def play_command(message: disnake.Message, prefix: str = "?") -> None:
    """
    Play audio from a YouTube URL or search query in a voice channel.
    Uses simplified FFmpeg options for better compatibility.
    """
    args = message.content.split(" ", 1)
    if len(args) < 2:
        embed = disnake.Embed(
            title="Invalid Usage",
            description="Please provide a YouTube URL or search term.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        voice_channel = message.author.voice.channel
        if not voice_channel:
            raise AttributeError
    except AttributeError:
        embed = disnake.Embed(
            title="Voice Channel Required",
            description="Please join a voice channel to use this command!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        voice_client = await voice_channel.connect()
    except disnake.ClientException:
        voice_client = message.guild.voice_client

    if voice_client and voice_client.is_playing():
        voice_client.stop()

    status_embed = disnake.Embed(
        title="Processing",
        description="Fetching audio stream...",
        color=color_manager.get_color("Blue"),
    )
    status_embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    status_message = await message.channel.send(embed=status_embed)

    query = args[1]

    ydl_opts = {
        "format": "bestaudio",
        "noplaylist": True,
        "quiet": False,
        "no_warnings": False,
        "extract_flat": "in_playlist",
        "source_address": "0.0.0.0",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if "entries" in info:
                info = info["entries"][0]

            url = info["url"]
            title = info["title"]
            duration = info.get("duration", "Unknown")

            ffmpeg_options = {
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn",
            }

            def after_playing(error):
                if error:
                    log_info(f"Player error: {error}", error=True)
                    asyncio.run_coroutine_threadsafe(
                        message.channel.send(
                            embed=disnake.Embed(
                                title="Playback Error",
                                description=f"An error occurred during playback: {str(error)}",
                                color=color_manager.get_color("Red"),
                            )
                        ),
                        voice_client.loop,
                    )

            log_info(f"Attempting to play URL: {url}", error=True)
            log_info(f"Using FFmpeg options: {ffmpeg_options}", error=True)

            try:
                audio_source = disnake.FFmpegPCMAudio(url, **ffmpeg_options)
                voice_client.play(audio_source, after=after_playing)

                play_embed = disnake.Embed(
                    title="Now Playing",
                    description=f"🎵 **{title}**",
                    color=color_manager.get_color("Green"),
                )
                play_embed.add_field(
                    name="Requested by", value=message.author.mention, inline=True
                )

                if isinstance(duration, (int, float)):
                    play_embed.add_field(
                        name="Duration",
                        value=f"{int(duration/60)}:{int(duration%60):02d}",
                        inline=True,
                    )

                play_embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
                await status_message.edit(embed=play_embed)

            except Exception as e:
                log_info(f"FFmpeg error details: {str(e)}", error=True)
                raise Exception(f"FFmpeg error: {str(e)}")

    except Exception as e:
        error_embed = disnake.Embed(
            title="Error",
            description=f"An error occurred while setting up the audio stream: {str(e)}",
            color=color_manager.get_color("Red"),
        )
        error_embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await status_message.edit(embed=error_embed)

        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()

        log_info(f"Play command error: {str(e)}", error=True)


async def profile_command(message: disnake.Message, prefix: str = "?") -> None:
    if len(message.mentions) < 1:
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Usage: {prefix}profile @user",
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
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Usage: {prefix}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        fetched_user = await Memo.fetch_user(user.id)

    except disnake.errors.NotFound as e:
        embed = disnake.Embed(
            title="Not found",
            description=f"Error occurred while fetching user. Usage: {prefix}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except disnake.errors.HTTPException as e:
        embed = disnake.Embed(
            title="Unknown Error",
            description=f"Error occurred while fetching user, but this exception does not have defined behavior. Usage: {prefix}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if user not in message.guild.members:
        embed = disnake.Embed(
            title="Member not in guild!",
            description=f"Please make sure that the user you are searching for exists and is in this guild. Usage: {prefix}profile @user",
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

    if status == disnake.enums.Status(value="dnd"):
        status = "⛔ Do not disturb"

    elif status == disnake.enums.Status(value="online"):
        status = "🟢 Online"

    elif status == disnake.enums.Status(value="idle"):
        status = "🟡 Idle"

    else:
        status = "⚫ Offline"

    embed = disnake.Embed(
        title=f"{name}'s Profile",
        description="Users public discord information, please don't use for bad or illegal purposes!",
    )

    embed.add_field(name="Display Name", value=name, inline=True)

    embed.add_field(name="Username", value=username, inline=True)

    embed.add_field(name="User ID", value=user_id, inline=True)

    embed.add_field(name="Creation Time", value=creation, inline=True)

    embed.add_field(name="Status", value=status, inline=True)

    embed.add_field(
        name="Badges",
        value=(
            ", ".join(
                " ".join(word.capitalize() for word in badge.replace("_", " ").split())
                for badge in badges
            )
            if len(badges) >= 1
            else "None"
        ),
        inline=True,
    )

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


async def nick_command(message: disnake.Message, prefix: str = "?") -> None:
    if (
        not message.author.guild_permissions.administrator
        | message.author.guild_permissions.administrator
    ):
        embed = disnake.Embed(
            title="Missing permission",
            description=f"Missing required permission `manage_nicknames`. Please run `{prefix}help` for more information!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Usage: {prefix}nick @user [new_nickname]",
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
        embed = disnake.Embed(
            title="Member not in guild!",
            description=f"Please make sure that the user you are searching for exists and is in this guild. Usage: {prefix}nick @user [new_nick]",
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
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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


async def feedback_command(message: disnake.Message, prefix: str = "?") -> None:
    args = message.content.split()[1:]
    feedback_text = " ".join(args)

    if len(args) < 1:
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Usage: {prefix}feedback [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    feedback.add_feedback(message.author.id, feedback_text)

    embed = disnake.Embed(
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
async def restart_command(message: disnake.Message, prefix: str = "?") -> None:
    embed = disnake.Embed(
        title="Restarting",
        description=f"The restart will take approximately 10 to 30 seconds on average.",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)

    await restart_memo()


async def translate_command(message: disnake.Message, prefix: str = "?") -> None:
    translate_text = message.content.split(" ", 1)[1]

    try:
        translator = GoogleTranslator(source="auto", target="en")
        translated_text = translator.translate(translate_text)

        embed = disnake.Embed(
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


async def ping_command(message: disnake.Message, prefix: str = "?") -> None:
    bot_latency = fetch_latency(Memo)

    embed = disnake.Embed(
        title="Bot latency",
        description=f"The current bot latency is approximately `{bot_latency}ms`",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    await message.channel.send(embed=embed)


async def server_command(message: disnake.Message, prefix: str = "?") -> None:
    try:
        guild = message.guild

        if not guild.me.guild_permissions.administrator:
            embed = disnake.Embed(
                title="Permission Denied",
                description="You need administrator permissions to gather all server stats.",
                color=color_manager.get_color("Red"),
            )
            embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
            await message.channel.send(embed=embed)
            return

        if Memo.intents.members:
            try:
                await guild.chunk()
            except disnake.HTTPException:
                log_info("Failed to fetch all members. Some stats may be incomplete.")

        embed = disnake.Embed(
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

    except disnake.Forbidden:
        await send_error_embed(
            message,
            "Permission Error",
            "I don't have permission to access some server information.",
            FOOTER_TEXT=FOOTER_TEXT,
            FOOTER_ICON=FOOTER_ICON,
            color_manager=color_manager,
        )
    except disnake.HTTPException as e:
        await send_error_embed(
            message,
            "HTTP Error",
            f"An HTTP error occurred: {e}",
            FOOTER_TEXT=FOOTER_TEXT,
            FOOTER_ICON=FOOTER_ICON,
            color_manager=color_manager,
        )
    except Exception as e:
        await send_error_embed(
            message,
            "Unexpected Error",
            f"An unexpected error occurred: {e}",
            FOOTER_TEXT=FOOTER_TEXT,
            FOOTER_ICON=FOOTER_ICON,
            color_manager=color_manager,
        )
        log_info(f"Unexpected error in server command: {e}")


async def joke_command(message: disnake.Message, prefix: str = "?") -> None:
    joke = await fetch_random_joke()

    if joke:
        embed = disnake.Embed(
            color=color_manager.get_color("Blue"), title="Dad joke", description=joke
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
    else:
        send_error_embed(
            message=message,
            title="Error",
            description="Sorry, I couldn't fetch a joke at the moment.",
            FOOTER_TEXT=FOOTER_TEXT,
            FOOTER_ICON=FOOTER_ICON,
            color_manager=color_manager,
        )


async def coin_command(message: disnake.Message, prefix: str = "?") -> None:
    embed = disnake.Embed(
        title="Coin Flip",
        description="The coin is spinning...",
        color=color_manager.get_color("Blue"),
    )
    embed.set_thumbnail(
        url="https://media.istockphoto.com/id/141325539/vector/heads-or-tails.jpg?s=612x612&w=0&k=20&c=V8GPGyuVWFMl4awXzlCp1lhYE5hKiKBybnZocR1i7Uw="
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)

    message = await message.channel.send(embed=embed)

    await asyncio.sleep(1.5)

    result = "Heads" if random.choice([True, False]) else "Tails"
    embed.description = f"The coin landed on: **{result}**!"

    embed.set_thumbnail(
        url=(
            "https://e7.pngegg.com/pngimages/547/992/png-clipart-computer-icons-coin-gold-pile-of-gold-coins-gold-coin-gold-thumbnail.png"
            if result == "Heads"
            else "https://e7.pngegg.com/pngimages/443/910/png-clipart-gold-peso-coin-logo-coin-philippine-peso-peso-coin-gold-coin-text-thumbnail.png"
        )
    )

    await message.edit(embed=embed)


async def quote_command(message: disnake.Message, prefix: str = "?") -> None:
    quote = fetch_quote_of_the_day()
    text = quote[0]
    author = quote[1]

    embed = disnake.Embed(
        title="Quote of the day",
        description=f'"{text}" - {author}',
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)

    await message.channel.send(embed=embed)


async def vc_mute_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.mute_members:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You need the `Mute Members` permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1 or len(message.content.split()) < 3:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member and provide a reason. Usage: {prefix}mute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    member = message.guild.get_member(message.mentions[0].id)
    reason = " ".join(message.content.split()[2:])

    if not member:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member. Usage: {prefix}mute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if message.author.top_role <= member.top_role:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You cannot mute this user as they have an equal or higher role than you.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if not member.voice:
        embed = disnake.Embed(
            title="Error",
            description=f"Member not in voice channel. Usage: {prefix}mute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if member.voice.mute:
        embed = disnake.Embed(
            title="Error",
            description=f"Member is already muted. Usage: {prefix}mute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        dm_embed = disnake.Embed(
            title="You've Been Voice Muted",
            description=f"You were voice muted in {message.guild.name}.\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Red"),
        )
        dm_embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await member.send(embed=dm_embed)
    except Exception as e:
        log_info(f"Failed to DM {member.name} about their voice mute.\n {e}")

    try:
        await member.edit(mute=True, reason=reason)
        embed = disnake.Embed(
            title="Voice Mute",
            description=f"Muted {member.mention}\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
    except disnake.Forbidden:
        embed = disnake.Embed(
            title="Error",
            description="I don't have permission to mute this member.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)


async def vc_unmute_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.mute_members:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You need the `Mute Members` permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1 or len(message.content.split()) < 3:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member and provide a reason. Usage: {prefix}unmute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    member = message.guild.get_member(message.mentions[0].id)
    reason = " ".join(message.content.split()[2:])

    if not member:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member. Usage: {prefix}unmute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if message.author.top_role <= member.top_role:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You cannot unmute this user as they have an equal or higher role than you.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if not member.voice:
        embed = disnake.Embed(
            title="Error",
            description=f"Member not in voice channel. Usage: {prefix}unmute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if not member.voice.mute:
        embed = disnake.Embed(
            title="Error",
            description=f"Member is already unmuted. Usage: {prefix}unmute @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        dm_embed = disnake.Embed(
            title="You've Been Voice Unmuted",
            description=f"You were voice unmuted in {message.guild.name}.\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Green"),
        )
        dm_embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await member.send(embed=dm_embed)
    except Exception as e:
        log_info(f"Failed to DM {member.name} about their voice mute.\n {e}")

    try:
        await member.edit(mute=False, reason=reason)
        embed = disnake.Embed(
            title="Voice Unmute",
            description=f"Unmuted {member.mention}\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
    except disnake.Forbidden:
        embed = disnake.Embed(
            title="Error",
            description="I don't have permission to unmute this member.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)


async def vc_deafen_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.deafen_members:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You need the `Deafen Members` permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1 or len(message.content.split()) < 3:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member and provide a reason. Usage: {prefix}deafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    member = message.guild.get_member(message.mentions[0].id)
    reason = " ".join(message.content.split()[2:])

    if not member:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member. Usage: {prefix}deafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if message.author.top_role <= member.top_role:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You cannot deafen this user as they have an equal or higher role than you.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if not member.voice:
        embed = disnake.Embed(
            title="Error",
            description=f"Member not in voice channel. Usage: {prefix}deafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if member.voice.deaf:
        embed = disnake.Embed(
            title="Error",
            description=f"Member is already deafened. Usage: {prefix}deafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        dm_embed = disnake.Embed(
            title="You've Been Voice Deafened",
            description=f"You were voice deafened in {message.guild.name}.\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Red"),
        )
        dm_embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await member.send(embed=dm_embed)
    except Exception as e:
        log_info(f"Failed to DM {member.name} about their voice mute.\n {e}")

    try:
        await member.edit(deafen=True, reason=reason)
        embed = disnake.Embed(
            title="Voice Deafen",
            description=f"Deafened {member.mention}\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
    except disnake.Forbidden:
        embed = disnake.Embed(
            title="Error",
            description="I don't have permission to deafen this member.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)


async def vc_undeafen_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.deafen_members:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You need the `Deafen Members` permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1 or len(message.content.split()) < 3:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member and provide a reason. Usage: {prefix}undeafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    member = message.guild.get_member(message.mentions[0].id)
    reason = " ".join(message.content.split()[2:])

    if not member:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention a valid member. Usage: {prefix}undeafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if message.author.top_role <= member.top_role:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You cannot undeafen this user as they have an equal or higher role than you.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if not member.voice:
        embed = disnake.Embed(
            title="Error",
            description=f"Member not in voice channel. Usage: {prefix}undeafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if not member.voice.deaf:
        embed = disnake.Embed(
            title="Error",
            description=f"Member is already undeafened. Usage: {prefix}undeafen @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    try:
        dm_embed = disnake.Embed(
            title="You've Been Voice Undeafened",
            description=f"You were voice undeafened in {message.guild.name}.\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Green"),
        )
        dm_embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await member.send(embed=dm_embed)
    except Exception as e:
        log_info(f"Failed to DM {member.name} about their voice mute.\n {e}")

    try:
        await member.edit(deafen=False, reason=reason)
        embed = disnake.Embed(
            title="Voice Undeafen",
            description=f"Undeafened {member.mention}\n**Reason:** {reason}\n**Moderator:** {message.author.mention}",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
    except disnake.Forbidden:
        embed = disnake.Embed(
            title="Error",
            description="I don't have permission to undeafen this member.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)


async def eight_ball_command(message: disnake.Message, prefix: str = "?"):
    if len(message.content.split()) < 2:
        embed = disnake.Embed(
            title="Error",
            description=f"Please provide a question. Usage: {prefix}8ball [question]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    choices = [
        "Yes",
        "No",
        "Maybe",
        "Ask again later",
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell",
        "Outlook not so good",
        "Very doubtful",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ]

    random.choice(choices)

    embed = disnake.Embed(
        title="8 Ball",
        description=f"**Question:** {" ".join(message.content.split()[1:])}\n**Answer:** {random.choice(choices)}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    embed.set_thumbnail(
        url="https://e7.pngegg.com/pngimages/322/428/png-clipart-eight-ball-game-pool-computer-icons-ball-game-text.png"
    )

    await message.channel.send(embed=embed)


async def set_prefix_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.administrator:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You need the `Administrator` permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if len(message.content.split()) < 2:
        embed = disnake.Embed(
            title="Error",
            description=f"Please provide a new prefix. Usage: {prefix}setprefix [new prefix]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    new_prefix = message.content.split()[1][0]

    hashed_guild_id = SHA3.hash_256(message.guild.id)

    if guild_configs.set_guild_config(hashed_guild_id, new_prefix):
        success = True
    else:
        success = guild_configs.add_guild_config(hashed_guild_id, new_prefix)

    if success:
        embed = disnake.Embed(
            title="Prefix Changed",
            description=f"The prefix has been changed from {prefix} to `{new_prefix}`",
            color=color_manager.get_color("Blue"),
        )
    else:
        embed = disnake.Embed(
            title="Error",
            description="Failed to update the prefix. Please try again later.",
            color=color_manager.get_color("Red"),
        )

    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)

    if new_prefix == "/":
        embed = disnake.Embed(
            title="Warning",
            description="Setting the command prefix to `/` will not make it appear as a regular slash command but instead as a on message command trigger!",
            color=color_manager.get_color("Orange"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return
    
    if new_prefix == prefix:
        embed = disnake.Embed(
            title="Warning",
            description="Setting the command prefix to the same as the current one will not have any effect.",
            color=color_manager.get_color("Orange"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return


async def setup_command(message: disnake.Message, prefix: str = "?") -> None:
    embed = disnake.Embed(
        title="Setup Instructions",
        description="Here are some useful commands to get you started setting up your bot!.",
        color=color_manager.get_color("Blue"),
    )
    embed.add_field(
        name="Set command prefix",
        value=f"The default prefix for commands is `?`. To change this, use the `setprefix` command. This command must be used in the server where you want to change the prefix.",
        inline=False,
    )
    embed.add_field(
        name="Advanced Options",
        value=f"To start setting up advanced options go to https://memo.nerd-bear.org/dashboard",
        inline=False,
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)


async def chat_command(message: disnake.Message, prefix: str = "?") -> None:
    if len(message.content.strip().split(" ")) < 2:
        embed = disnake.Embed(
            title="Error",
            description=f"Please provide a message. Usage: {prefix}chat [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    user_prompt = " ".join(message.content.split()[1:])
    groq_response = chat_bot.send_msg(user_prompt)

    if len(groq_response) > 1900:
        groq_response = f"Response too long. Truncated to 1900 characters: {groq_response[:1900]}..."

    await message.channel.send(groq_response)


async def afk_command(message: disnake.Message, prefix: str = "?") -> None:
    afk_msg = (
        " ".join(message.content.split()[1:])
        if len(message.content.split()) > 1
        else "None"
    )

    if message.author.id in afk_users:
        del afk_users[message.author.id]

        embed = disnake.Embed(
            title="AFK Status Removed",
            description=f"Welcome back! You are no longer AFK.",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    afk_users[message.author.id] = afk_msg

    embed = disnake.Embed(
        title="AFK Status Set",
        description=f"You are now AFK.\nMessage: {afk_msg}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)


async def kiss_command(message: disnake.Message, prefix: str = "?") -> None:
    if len(message.mentions) < 1:
        embed = disnake.Embed(
            title="Error",
            description=f"Please mention someone to kiss them. Usage: {prefix}kiss @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if message.mentions[0] == message.author:
        embed = disnake.Embed(
            title="Error",
            description="You can't kiss yourself.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    embed = disnake.Embed(
        title="Kiss",
        description=f"{message.mentions[0].mention} got kisses from {message.author.mention}!",
        color=color_manager.get_color("Blue"),
    )
    await message.channel.send(content=f"{message.mentions[0].mention}")
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)


async def rps_command(message: disnake.Message, prefix: str = "?") -> None:
    choices = ["rock", "paper", "scissors"]
    emojis = {"rock": "🗻", "paper": "📄", "scissors": "✂️"}

    if len(message.content.strip().split(" ")) < 2:
        embed = disnake.Embed(
            title="Error",
            description=f"Please provide your choice. Usage: {prefix}rps [rock, paper, scissors]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    user_choice = message.content.split()[1].lower()

    for choice in choices:
        if Levenshtein.ratio(user_choice, choice) * 100 >= 50:
            user_choice = choice
            break

    if user_choice not in choices:
        embed = disnake.Embed(
            title="Error",
            description=f"Invalid choice. Please choose from: {', '.join(choices)}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
        color = color_manager.get_color("Blue")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "User Wins!"
        color = color_manager.get_color("Green")
    else:
        result = "Computer Wins!"
        color = color_manager.get_color("Red")

    embed = disnake.Embed(
        title=result,
        description=f"You chose {emojis[user_choice]}, and the computer chose {emojis[computer_choice]}.",
        color=color,
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)


async def man_command(message: disnake.Message, prefix: str = "?") -> None:
    if len(message.content.strip().split(" ")) < 2:
        embed = disnake.Embed(
            title="Error",
            description=f"Please provide a man's name. Usage: {prefix}man [name_command]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    command_name = message.content.split()[1]

    try:
        help_dict: dict = fetch_help_dict(
            color_manager, BOT_NAME, BOT_VERSION, prefix, FOOTER_TEXT, FOOTER_ICON
        )[command_name]
        description = help_dict.get("desc", "No description provided.")
        usage = help_dict.get("usage", "No usage provided.")

    except KeyError:
        embed = disnake.Embed(
            title="Error",
            description=f"Command '{command_name}' not found.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    embed = disnake.Embed(
        title=f"{command_name.capitalize()} Manual Page",
        description=f"**Description:** {description}\n\
                      **Usage:** `{usage.split()[0]}` {" ".join(usage.split()[1:])}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)


async def purge_command(message: disnake.Message, prefix: str = "?") -> None:
    if not message.author.guild_permissions.manage_messages:
        embed = disnake.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    if len(message.content.strip().split(" ")) < 2:
        embed = disnake.Embed(
            title="Error",
            description=f"Please provide a number of messages to delete. Usage: {prefix}purge [number_of_messages]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return
    
    number_of_messages = int(message.content.split()[1])
    deleted_messages = await message.channel.purge(limit=number_of_messages + 1)

    embed = disnake.Embed(
        title="Message Purge",
        description=f"Deleted {len(deleted_messages) - 1} messages.",
        color=color_manager.get_color("Green"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)
    return


async def spellcheck_command(message: disnake.Message, prefix: str = "?") -> None:
    if len(message.content.strip().split(" ")) < 2:
        embed = disnake.Embed(
            title="Error",
            description=f"Please provide a sentence to spellcheck. Usage: {prefix}spellcheck [sentence]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return
    
    sentence = " ".join(message.content.split()[1:])

    if len(sentence) > 500:
        embed = disnake.Embed(
            title="Error",
            description="The sentence is too long. Please provide a sentence with a maximum length of 500 characters.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
        await message.channel.send(embed=embed)
        return

    text_blob = TextBlob(sentence)
    corrected_sentence = text_blob.correct()

    embed = disnake.Embed(
        title="Spellcheck Results",
        description=f"{corrected_sentence}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    await message.channel.send(embed=embed)
    return


@Memo.event
async def on_message_delete(message: disnake.Message):
    if message.author == Memo.user:
        return

    channel = Memo.get_channel(LOGGING_CHANNEL_ID)
    if not channel:
        return

    embed = disnake.Embed(
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


@Memo.event
async def on_message_edit(before: disnake.Message, after: disnake.Message):
    if before.author == Memo.user:
        return

    channel = Memo.get_channel(LOGGING_CHANNEL_ID)
    if not channel:
        return

    if before.content == after.content:
        return

    embed = disnake.Embed(
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


@commands.slash_command(
    name="help", description="Shows help information about commands"
)
async def slash_help(interaction: disnake.ApplicationCommandInteraction):
    embed = fetch_help_embed(
        color_manager, BOT_NAME, BOT_VERSION, prefix, FOOTER_TEXT, FOOTER_ICON
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@Memo.slash_command(
    name="info", description="Shows important information about the bot."
)
async def slash_info(interaction: disnake.ApplicationCommandInteraction):
    embed = fetch_info_embed(
        color_manager, BOT_NAME, BOT_VERSION, prefix, FOOTER_TEXT, FOOTER_ICON
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@Memo.slash_command(
    description="Send information about the Playground server!",
    guild_ids=[1288144110880030795],
)
async def playground_info(inter: disnake.ApplicationCommandInteraction):

    embed = disnake.Embed(
        description="""
        * Welcome to **Playground**, the server for the **Discord Memo community**! We offer some amazing community content, fun and unique features and great support for Memo. There are some rules that you need to follow to enjoy our community. Please check that out in the <#1291572712652804157> channel.
        """,
        title="Welcome to Playground!",
        color=disnake.Color.blue(),
    )

    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)
    embed.set_author(name="Memo - Playground")

    await inter.user.send(
        embed=embed,
        components=[
            disnake.ui.Button(
                label="Support",
                style=disnake.ButtonStyle.blurple,
                custom_id="help_support",
            ),
            disnake.ui.Button(
                label="More information",
                style=disnake.ButtonStyle.link,
                url="https://memo.nerd-bear.org",
            ),
        ],
    )


@Memo.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["help_support"]:
        return

    embed = disnake.Embed(
        description="We see you are looking for some support... Well here you go! You can visit our website at https://memo.nerd-bear.org. If you want more direct responses, then you can message the lead developer and official holder of the Memo Discord Development Team by sending a message to nerd.bear on Discord!",
        title="Support",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(text=FOOTER_TEXT, icon_url=FOOTER_ICON)

    await inter.user.send(embed=embed)