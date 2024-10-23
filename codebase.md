# .gitignore

```
.vscode
```

# assets\emojis\gif\0_percent_battery.gif

This is a binary file of the type: Image

# assets\emojis\gif\25_percent_battery_blinking.gif

This is a binary file of the type: Image

# assets\emojis\gif\50_percent_battery.gif

This is a binary file of the type: Image

# assets\emojis\gif\75_percent_battery_blinking.gif

This is a binary file of the type: Image

# assets\emojis\gif\75_percent_battery.gif

This is a binary file of the type: Image

# assets\emojis\gif\100_percent_battery.gif

This is a binary file of the type: Image

# assets\emojis\gif\active_developer.gif

This is a binary file of the type: Image

# assets\emojis\gif\help_heart.gif

This is a binary file of the type: Image

# assets\emojis\gif\linked.gif

This is a binary file of the type: Image

# assets\emojis\gif\verified_developer.gif

This is a binary file of the type: Image

# assets\emojis\webp\0_percent_battery.webp

This is a binary file of the type: Image

# assets\emojis\webp\25_percent_battery_blinking.webp

This is a binary file of the type: Image

# assets\emojis\webp\50_percent_battery.webp

This is a binary file of the type: Image

# assets\emojis\webp\75_percent_battery_blinking.webp

This is a binary file of the type: Image

# assets\emojis\webp\75_percent_battery.webp

This is a binary file of the type: Image

# assets\emojis\webp\100_percent_battery.webp

This is a binary file of the type: Image

# assets\emojis\webp\active_developer.webp

This is a binary file of the type: Image

# assets\emojis\webp\help_heart.webp

This is a binary file of the type: Image

# assets\emojis\webp\linked.webp

This is a binary file of the type: Image

# assets\emojis\webp\verified_developer.webp

This is a binary file of the type: Image

# assets\logo\editable\variation-1.ai

This is a binary file of the type: Binary

# assets\logo\editable\variation-2.ai

This is a binary file of the type: Binary

# assets\logo\editable\variation-3.ai

This is a binary file of the type: Binary

# assets\logo\editable\variation-4.ai

This is a binary file of the type: Binary

# assets\logo\png\bear.png

This is a binary file of the type: Image

# assets\logo\png\padded_bear.png

This is a binary file of the type: Image

# assets\logo\svg\variation-1.svg

This is a file of the type: SVG Image

# assets\logo\svg\variation-2.svg

This is a file of the type: SVG Image

# assets\logo\svg\variation-3.svg

This is a file of the type: SVG Image

# assets\logo\svg\variation-4.svg

This is a file of the type: SVG Image

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

# BotUpdate\cogs\md.md

```md
### Approach to Developing a 2FA Email Sending Project Using Custom Domain Email

#### **Objective:**
You aim to develop a test project that sends Two-Factor Authentication (2FA) emails using Python, leveraging a custom email address with a custom domain (`nerd-bear.org`). The current setup involves GoDaddy for domain registration, Cloudflare for DNS management, and free email forwarding to a Gmail account. However, this setup does not support sending emails directly from the custom domain email address.

#### **Requirements:**
- **Primary Requirement:** Send emails from the custom domain email address (`nerd-bear.org`) for the 2FA project.
- **Constraints:** The current setup does not support sending emails directly from the custom domain email address.

#### **Proposed Solution:**

1. **Set Up a Custom Email Service:**
   - **Option 1: Use a Third-Party Email Service Provider (ESP):**
     - **Service Providers:** Consider using services like **SendGrid**, **Mailgun**, or **Amazon SES** (Simple Email Service).
     - **Steps:**
       1. **Sign Up:** Create an account with the chosen ESP.
       2. **Domain Verification:** Verify your domain (`nerd-bear.org`) with the ESP to ensure you can send emails from it. This usually involves adding DNS records provided by the ESP to your Cloudflare DNS settings.
       3. **API Integration:** Use the ESP's API to send emails from your Python application. Most ESPs provide Python libraries or SDKs for easy integration.
       4. **Custom Email Address:** Configure the ESP to send emails from your custom domain email address (e.g., `noreply@nerd-bear.org`).
     - **Example with SendGrid:**
       \`\`\`python
       from sendgrid import SendGridAPIClient
       from sendgrid.helpers.mail import Mail

       message = Mail(
           from_email='noreply@nerd-bear.org',
           to_emails='user@example.com',
           subject='Your 2FA Code',
           html_content='Your code is: 123456')

       try:
           sg = SendGridAPIClient('YOUR_SENDGRID_API_KEY')
           response = sg.send(message)
           print(response.status_code, response.body, response.headers)
       except Exception as e:
           print(e.message)
       \`\`\`

   - **Option 2: Set Up a Mail Server:**
     - **Service Providers:** Consider using **Mailcow**, **Mailu**, or **Postfix/Dovecot** to set up your own mail server.
     - **Steps:**
       1. **Server Setup:** Deploy a mail server on a VPS (Virtual Private Server) or a dedicated server.
       2. **Domain Configuration:** Configure the mail server to use your custom domain (`nerd-bear.org`). This involves setting up DNS records (MX, SPF, DKIM, DMARC) in Cloudflare.
       3. **Email Sending:** Use Python's `smtplib` library to send emails from your custom domain email address.
     - **Example with SMTP:**
       \`\`\`python
       import smtplib
       from email.mime.text import MIMEText

       msg = MIMEText('Your code is: 123456')
       msg['Subject'] = 'Your 2FA Code'
       msg['From'] = 'noreply@nerd-bear.org'
       msg['To'] = 'user@example.com'

       with smtplib.SMTP('your-mail-server.com', 587) as server:
           server.starttls()
           server.login('noreply@nerd-bear.org', 'your-email-password')
           server.sendmail('noreply@nerd-bear.org', 'user@example.com', msg.as_string())
       \`\`\`

2. **Leverage Existing Infrastructure:**
   - **Cloudflare:** Ensure that Cloudflare is configured to allow outbound SMTP traffic if you choose to set up your own mail server.
   - **GoDaddy:** Verify that GoDaddy is correctly pointing to Cloudflare for DNS management.

3. **Security Considerations:**
   - **API Keys:** If using an ESP, store API keys securely (e.g., environment variables, encrypted storage).
   - **Email Authentication:** Ensure that your emails are authenticated using SPF, DKIM, and DMARC to prevent them from being marked as spam.

#### **Conclusion:**
The best approach depends on your specific needs, such as the volume of emails, budget, and technical expertise. Using a third-party ESP like SendGrid or Mailgun is generally easier and more scalable, while setting up your own mail server offers more control but requires more technical effort.

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
{
    "defaults": {
        "prefix": "?",
        "footer_text": "This bot is created and hosted by Nerd bear",
        "footer_icon": "https://as2.ftcdn.net/v2/jpg/01/17/00/87/1000_F_117008730_0Dg5yniuxPQLz3shrJvLIeBsPfPRBSE1.jpg"
    },

    "bot_version": "0.4.6",
    "bot_name": "Memo",
    "tts_mode":"fast",
    "log_channel_id": "1290060885485948950",
    "tts_detector_factory_seed": "0",
    "token": "token",
    
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

# BotUpdate\data\crac.db

```db

```

# BotUpdate\logs\bot.log

```log

```

# BotUpdate\main.py

```py
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
```

# BotUpdate\requirements.txt

```txt
aiohappyeyeballs        == 2.4.3
aiohttp                 == 3.10.8
aiosignal               == 1.3.1
aiosqlite               == 0.20.0
annotated-types         == 0.7.0
anyio                   == 4.6.0
async-timeout           == 4.0.3
attrs                   == 24.2.0
beautifulsoup4          == 4.12.3
blinker                 == 1.8.2
Brotli                  == 1.1.0
certifi                 == 2024.8.30
cffi                    == 1.17.1
charset-normalizer      == 3.3.2
click                   == 8.1.7
colorama                == 0.4.6
comtypes                == 1.4.7
cryptography            == 43.0.1
dataclasses-json        == 0.6.7
deep-translator         == 1.11.4
Deprecated              == 1.2.14
discord                 == 2.3.2
discord.py              == 2.4.0
disnake                 == 2.9.2
distro                  == 1.9.0
duckduckgo_search       == 6.2.13
edge-tts                == 6.1.12
fastapi                 == 0.115.0
ffmpeg-python           == 0.2.0
Flask                   == 3.0.3
Flask-Cors              == 5.0.0
frozenlist              == 1.4.1
future                  == 1.0.0
gevent                  == 24.2.1
greenlet                == 3.1.1
groq                    == 0.11.0
gTTS                    == 2.5.3
h11                     == 0.14.0
httpcore                == 1.0.5
httpx                   == 0.27.2
idna                    == 3.10
itsdangerous            == 2.2.0
Jinja2                  == 3.1.4
joblib                  == 1.4.2
jsonpatch               == 1.33
jsonpointer             == 3.0.0
langchain               == 0.3.1
langchain-community     == 0.3.1
langchain-core          == 0.3.6
langchain-groq          == 0.2.0
langchain-ollama        == 0.2.0
langchain-text-splitter == 0.3.0
langdetect              == 1.0.9
langsmith               == 0.1.129
lxml                    == 5.3.0
lyrics-extractor        == 3.0.1
lyricsgenius            == 3.0.1
markdown-it-py          == 3.0.0
MarkupSafe              == 2.1.5
marshmallow             == 3.22.0
mdurl                   == 0.1.2
multidict               == 6.1.0
mutagen                 == 1.47.0
mypy-extensions         == 1.0.0
nltk                    == 3.9.1
numpy                   == 1.26.4
ollama                  == 0.3.3
orjson                  == 3.10.7
packaging               == 24.1
pillow                  == 10.4.0
primp                   == 0.6.3
pycparser               == 2.22
pycryptodomex           == 3.20.0
pydantic                == 2.9.2
pydantic-settings       == 2.5.2
pydantic_core           == 2.23.4
PyGithub                == 2.4.0
Pygments                == 2.18.0
PyJWT                   == 2.9.0
PyNaCl                  == 1.5.0
pypiwin32               == 223
PySide6                 == 6.7.3
PySide6_Addons          == 6.7.3
PySide6_Essentials      == 6.7.3
python-dotenv           == 1.0.1
pyttsx3                 == 2.98
pytube                  == 15.0.0
pywin32                 == 306
PyYAML                  == 6.0.2
redis                   == 5.1.0
regex                   == 2024.9.11
requests                == 2.32.3
rich                    == 13.8.1
shiboken6               == 6.7.3
six                     == 1.16.0
sniffio                 == 1.3.1
soupsieve               == 2.6
spotipy                 == 2.24.0
SQLAlchemy              == 2.0.35
starlette               == 0.38.6
tenacity                == 8.5.0
timeout                 == 0.1.2
tqdm                    == 4.66.5
typing-inspect          == 0.9.0
typing_extensions       == 4.12.2
urllib3                 == 2.2.3
uvicorn                 == 0.31.0
websocket               == 0.2.1
websocket-client        == 1.8.0
websockets              == 13.1
Werkzeug                == 3.0.4
wikipedia               == 1.4.0
wrapt                   == 1.16.0
yarl                    == 1.13.1
youtube-transcript-api  == 0.6.2
yt-dlp                  == 2024.9.27
zope.event              == 5.0
zope.interface          == 7.0.3
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

DB_PATH = "./data/memo.db"

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

# changes.md

```md
# Memo Bot Changelog

## Latest Updates

+ Added restart command
+ Updated shutdown command to disconect from all voice channels
+ Updated start command to set RPC to the help info
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
    "bot_name": "Memo",
    "tts_mode":"fast",
    "log_channel_id": "1290060885485948950",
    "tts_detector_factory_seed": "0",
    
    "colors": {
      "Red":      "#FFB3BA",
      "Coral":    "#FFCCB6",
      "Orange":   "#FFE5B4",
      "Gold":     "#FFF1B5",
      "Yellow":   "#FFFFD1",
      "Lime":     "#DCFFB8",
      "Green":    "#BAFFC9",         
      "Teal":     "#B5EAD7",
      "Cyan":     "#C7F2FF",
      "Blue":     "#B5DEFF",
      "Navy":     "#C5CAE9",
      "Purple":   "#D0B8FF",
      "Magenta":  "#F2B5D4",
      "Pink":     "#FFCCE5",
      "Gray":     "#E0E0E0",
      "Lavender": "#E6E6FA"
    },

    "guilds": {
        "1288144110880030795": {
            "prefix": "*"
        }
    }
}
```

# crac.db

```db

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

    db_connection = sqlite3.connect("./memo.db")
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

def add_history(user_id: int, guild_id: int, command: str, arguments: list[str] = ["none"]) -> bool:
    """Uses SQLite to add user command to history of commands ran

    ### Params:
        `user_id`  `int`   The user id of the person who ran the command.
        `guild_id`  `int`   The guild id of the server that the user ran the command in.
        `command`  `str`   The name of the command that the user ran.
        `arguments`  `list[str]`   The arguments passed in to the command, defaults to ["none"].

    ### Return:
        Returns a bool (True on success)
    """
    args_json = json.dumps(arguments)
    datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
    
    db_connection = sqlite3.connect("./memo.db")
    db_cursor = db_connection.cursor()
    
    try:
        db_cursor.execute(
            "INSERT INTO history (user_id, guild_id, command, arguments, datetime) VALUES (?, ?, ?, ?, ?)",
            (user_id, guild_id, command, args_json, datetime_value)
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

DB_PATH = "./memo.db"


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

# help_heart.webp

This is a binary file of the type: Image

# launcher.py

```py
import click
from rich import print as rich_print


@click.command()
@click.option("--token", help="Discord bot token", required=True)
def main(token: str):
    if not token.strip():
        rich_print("[bold red]ERROR:[/bold red] Invalid token provided.")
        rich_print("Usage: python3 ./launcher.py --token <token>")
        raise click.Abort()

    from src.bot import Memo

    try:
        Memo.run(token)
    except Exception as e:
        rich_print(f"[red]{e}[/red]")
        click.Abort()


if __name__ == "__main__":
    main()

# python ./launcher.py --token "MTI4OTkyMTQ3NjYxNDU1MzY3Mg.GNo3VX.kjVPN-1ri34TtfuWZ-ADqhSeW56fARaLu7pMnk"
```

# LICENSE

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2024 Iona M.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

# memo.db

This is a binary file of the type: Binary

# README.md

```md
# Memo Bot

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Commands](#commands)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Project Structure](#project-structure)
8. [Dependencies](#dependencies)
9. [Development](#development)
10. [Contributing](#contributing)
11. [License](#license)
12. [Support](#support)
13. [Creator](#creator)

## Introduction

Memo Bot is a versatile, all-purpose Discord bot designed to enhance server management and user interaction. Currently in active development, Memo Bot offers a wide range of features from moderation tools to fun commands, making it a valuable addition to any Discord server.

## Features

1. **Server Moderation**
   - Kick users
   - Ban and unban users
   - Timeout users
   - Nickname management

2. **User Interaction**
   - Character information lookup
   - Text-to-speech functionality
   - Music playback from YouTube
   - User profile display

3. **Bot Management**
   - Customizable bot status
   - Start/shutdown commands
   - Feedback system

4. **Message Handling**
   - Logging of message edits and deletions
   - Inappropriate word detection and filtering

5. **Voice Channel Integration**
   - Join and leave voice channels
   - Play audio in voice channels

6. **Customization**
   - Configurable command prefix
   - Guild-specific settings

## Commands

Here's a detailed list of available commands:

1. `?help`: Displays a help message with all available commands and their usage.

2. `?kick @user [reason]`: Kicks the mentioned user from the server. Requires kick permissions.
   
3. `?ban @user [reason]`: Bans the mentioned user from the server. Requires ban permissions.
   
4. `?unban @user`: Unbans the specified user from the server. Requires ban permissions.
   
5. `?timeout @user <duration> <unit> [reason]`: Timeouts the mentioned user for the specified duration. Requires moderate members permission.
   
6. `?shutdown`: Shuts down the bot. Requires administrator permissions.
   
7. `?start`: Starts the bot if it's offline. Requires administrator permissions.
   
8. `?charinfo [character]`: Provides detailed information about the specified character, including Unicode data.
   
9. `?tts [message]`: Converts the given text to speech and plays it in the user's current voice channel.
   
10. `?play [youtube_url]`: Plays audio from the specified YouTube video in the user's current voice channel.
    
11. `?join`: Makes the bot join the user's current voice channel.
    
12. `?leave`: Makes the bot leave the current voice channel.
    
13. `?profile @user`: Displays detailed profile information about the mentioned user.
    
14. `?nick @user [new_nickname]`: Changes the nickname of the mentioned user. Requires manage nicknames permission.
    
15. `?feedback [message]`: Allows users to submit feedback about the bot, which is stored in a database.

## Installation

1. Clone the repository:
   \`\`\`
   git clone https://github.com/your-username/Memo-bot.git
   \`\`\`

2. Navigate to the project directory:
   \`\`\`
   cd Memo-bot
   \`\`\`

3. Install the required dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. Set up your Discord bot token:
   - Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a bot for your application and copy the bot token
   - Create a `config.json` file in the project root and add your token:
     \`\`\`json
     {
         "token": "YOUR_BOT_TOKEN_HERE"
     }
     \`\`\`

5. Set up the SQLite database:
   \`\`\`
   python setup/create_feedback_table.py
   python setup/create_history_table.py
   python setup/create_usage_table.py
   \`\`\`

## Usage

1. Run the bot:
   \`\`\`
   python launcher.py
   \`\`\`

2. Invite the bot to your Discord server:
   - Go to the OAuth2 URL generator in your Discord Developer Portal
   - Select the "bot" scope and the necessary permissions
   - Use the generated URL to invite the bot to your server

3. Once the bot is in your server, use `?help` to see all available commands.

## Configuration

The `config.json` file contains important settings for the bot:

\`\`\`json
{
    "defaults": {
        "prefix": "?"
    },
    "bot_version": "0.4.5",
    "bot_name": "Memo",
    "tts_mode": "fast",
    "guilds": {
        "1288144110880030795": {
            "prefix": "*"
        }
    }
}
\`\`\`

- `defaults.prefix`: The default command prefix for the bot.
- `bot_version`: The current version of the bot.
- `bot_name`: The name of the bot.
- `tts_mode`: The mode for text-to-speech functionality ("fast" or "slow").
- `guilds`: Guild-specific settings, including custom prefixes.

## Project Structure

- `main/bot.py`: The main bot file containing command implementations and event handlers.
- `launcher.py`: The entry point for running the bot.
- `db_manager/`: Directory containing database management modules.
- `setup/`: Directory containing database setup scripts.
- `temp/audio/`: Directory for temporary audio files used by the TTS feature.
- `website/`: Directory containing HTML files for the bot's website.

## Dependencies

Memo Bot relies on several Python libraries:

- discord.py: The core library for interacting with the Discord API.
- Pillow: Used for image manipulation in the `charinfo` command.
- gTTS: Google Text-to-Speech library for the TTS feature.
- yt_dlp: YouTube downloader used for the music playback feature.
- rich: Used for console output formatting and logging.
- langdetect: Used for language detection in the TTS feature.

For a complete list of dependencies, refer to the `requirements.txt` file.

## Development

Memo Bot is under active development with nearly daily updates. The development process includes:

- Regular feature additions and improvements
- Bug fixes and performance optimizations
- Refactoring for better code organization and maintainability
- Implementation of user feedback and feature requests

Future development plans include:
- Implementing a music queue system
- Adding more fun and interactive commands
- Improving error handling and user feedback
- Enhancing the configuration system for more granular control

## Contributing

We welcome contributions to Memo Bot! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive commit messages
4. Push your changes to your fork
5. Submit a pull request to the main repository

Please ensure your code adheres to the existing style conventions and includes appropriate tests.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for the full license text.

## Support

If you need help or want to report a bug, you can:

1. Open an issue on this GitHub repository
2. Join our support Discord server (link to be added)
3. Contact us via email at Memo@nerd-bear.org

## Creator

Memo Bot is created and maintained by Nerd Bear. For more information about the creator and other projects, visit [nerd-bear.org](https://nerd-bear.org).

---

Memo Bot © 2024 by Nerd Bear. All rights reserved.
```

# setup\clear_feedback_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE feedback")
db_cursor.execute("CREATE TABLE feedback(used_id, message, datetime)")
db_connection.commit()
```

# setup\clear_history_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE history")
db_cursor.execute("CREATE TABLE history(user_id, guild_id, command, arguments, datetime)")
db_connection.commit()
```

# setup\clear_usage_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE usage")
db_cursor.execute("CREATE TABLE usage(command_name, arguments, level)")
db_connection.commit()
```

# setup\create_feedback_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE feedback(used_id, message, datetime)")
db_connection.commit()
```

# setup\create_history_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE history(user_id, guild_id, command, arguments, datetime)")
db_connection.commit()
```

# setup\create_usage_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./memo.db")
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

import disnake
from disnake.ext import commands
from disnake.ui import Button, Select, Modal, TextInput, View

from rich import print as richPrint
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from deep_translator import GoogleTranslator

import yt_dlp

from db_manager import history, feedback
from src.utils.helper import *

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

BOT_PREFIX = config["defaults"].get("prefix", "?")
log_info("Loaded bot prefix", True)
BOT_NAME = config.get("bot_name", "Memo Bot")
log_info("Loaded bot name", True)
BOT_VERSION = config.get("bot_version", "1.0.0")
log_info("Loaded bot version", True)

TTS_MODE = config.get("tts_mode", "normal")
log_info("Loaded tts mode", True)

LOGGING_CHANNEL_ID = int(config.get("log_channel_id", 0))
log_info("Loaded logging channel id", True)

intents = disnake.Intents.all()
log_info("Initialized intents", True)
Memo = commands.Bot(command_prefix="/", intents=intents)
log_info("Initialized bot", True)
console = Console()
log_info("Initialized console", True)

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
    Prefix: {BOT_PREFIX}
    Initialization complete.
    """


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


@Memo.event
async def on_ready() -> None:
    markdown = Markdown(f"# Discord {BOT_NAME} version {BOT_VERSION}")
    console.print(markdown)

    info_text = await get_info_text()
    panel = Panel(
        info_text, title=f"{BOT_NAME} v{BOT_VERSION} Initialization Info", expand=False
    )

    console.print(panel)

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

    await Memo.change_presence(
        activity=disnake.Game(name=f"Run {BOT_PREFIX}help for help")
    )


@Memo.event
async def on_message(message: disnake.Message) -> None:
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

    if not message.content.startswith(BOT_PREFIX):
        if bot_active == False:
            return
        content = message.content.lower()
        if any(word in content for word in ["nigger", "nigga", "negro", "nigro"]):
            await handle_inappropriate_word(message)
        if Memo.user in message.mentions:
            await message.channel.send(
                f"Hello {message.author.mention}! You mentioned me. How can I help you?"
            )
        return

    if message.content.startswith("?") and len(message.content.strip()) <= 1:
        return

    if not bot_active and message.content != f"{BOT_PREFIX}start":
        embed = disnake.Embed(
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

    history.add_history(
        SHA3.hash_256(str(message.author.id)),
        SHA3.hash_256(str(message.guild)),
        command,
        args,
    )

    match command:
        case "help":
            await help_command(message)

        case "timeout":
            await timeout_command(message)

        case "kick":
            await kick_command(message)

        case "ban":
            await ban_command(message)

        case "unban":
            await unban_command(message)

        case "shutdown":
            await shutdown_command(message)

        case "start":
            await start_command(message)

        case "charinfo":
            await charinfo_command(message)

        case "join":
            await join_vc_command(message)

        case "leave":
            await leave_vc_command(message)

        case "tts":
            await tts_command(message)

        case "play":
            await play_command(message)

        case "profile":
            await profile_command(message)

        case "nick":
            await nick_command(message)

        case "feedback":
            await feedback_command(message)

        case "restart":
            await restart_command(message)

        case "translate":
            await translate_command(message)

        case "ping":
            await ping_command(message)

        case "server":
            await server_command(message)

        case "joke":
            await joke_command(message)

        case "coin":
            await coin_command(message)

        case "quote":
            await quote_command(message)

        case "mute":
            await vc_mute_command(message)

        case "unmute":
            await vc_unmute_command(message)

        case "deafen":
            await vc_deafen_command(message)

        case "undeafen":
            await vc_undeafen_command(message)

        case _:
            embed = disnake.Embed(
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


async def handle_inappropriate_word(message: disnake.Message) -> None:
    user = message.author
    channel = message.channel

    dm_embed = disnake.Embed(
        title="Inappropriate Word Detected",
        description=f"{BOT_NAME} has detected an inappropriate word! Please do not send racist words in our server! Moderators have been informed!",
        color=0xFF697A,
    )
    dm_embed.add_field(
        name="Rules",
        value="Please read our rules before sending such messages!",
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
        color=0xFF697A,
    )
    channel_embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=channel_embed)


async def help_command(message: disnake.Message) -> None:
    embed = fetch_help_embed(
        color_manager, BOT_NAME, BOT_VERSION, BOT_PREFIX, FOOTER_TEXT, FOOTER_ICON
    )
    await message.channel.send(embed=embed)


async def kick_command(message: disnake.Message) -> None:
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
            embed=disnake.Embed(
                title="You've wBeen Kicked",
                description=f"You were kicked from {message.guild.name}.\nReason: {reason}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.kick(reason=reason)
    embed = disnake.Embed(
        title="User Kicked",
        description=f"{member.mention} has been kicked.\nReason: {reason}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def ban_command(message: disnake.Message) -> None:
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
            description=f"Please mention a user to ban. Usage: {BOT_PREFIX}ban @user [reason]",
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
            description=f"Please mention a user to ban. Usage: {BOT_PREFIX}ban @user [reason]",
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
                description=f"You were banned from {message.guild.name}.\nReason: {reason}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.ban(reason=reason)
    embed = disnake.Embed(
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
async def shutdown_command(message: disnake.Message) -> None:
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
async def start_command(message: disnake.Message) -> None:
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
        activity=disnake.Game(name=f"Run {BOT_PREFIX}help for help"),
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


async def charinfo_command(message: disnake.Message) -> None:

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


async def unban_command(message: disnake.Message) -> None:
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

    if len(message.content.strip().split) < 2:
        embed = disnake.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to unban. Usage: {BOT_PREFIX}unban [user_id]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.guild.get_member(int(message.content.strip().split()[1]))

    if member is None:
        embed = disnake.Embed(
            title="Member Not Found",
            description=f"Please mention a user to unban. Usage: {BOT_PREFIX}unban [user_id]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    invite = message.channel.create_invite(reason="Invite unbanned user")

    try:
        await member.send(
            embed=disnake.Embed(
                title="You've Been unbanned",
                description=f"You were unbanned from {message.guild.name}",
                color=color_manager.get_color("Blue"),
            ).add_field(name="Invite link", value=invite)
        )
    except:
        pass

    try:
        await message.guild.unban(user=member)

    except disnake.errors.Forbidden as e:
        embed = disnake.Embed(
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

    except disnake.errors.NotFound as e:
        embed = disnake.Embed(
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

    except disnake.errors.HTTPException as e:
        embed = disnake.Embed(
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

    embed = disnake.Embed(
        title="User Unbanned",
        description=f"{member.mention} has been unbanned.",
        color=color_manager.get_color("Red"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def timeout_command(message: disnake.Message) -> None:
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
        await member.timeout(time_delta, reason=reason)
        embed = disnake.Embed(
            title="User Timed Out",
            description=f"{member.mention} has been timed out for {duration}{unit}.\nReason: {reason}",
            color=color_manager.get_color("Blue"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

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

    try:
        await member.timeout(time_delta, reason=reason)
        embed = disnake.Embed(
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


async def join_vc_command(message: disnake.Message) -> None:
    try:
        channel = Memo.get_channel(message.author.voice.channel.id)
        await channel.connect()
    except Exception as e:
        richPrint(e)


async def leave_vc_command(message: disnake.Message) -> None:
    try:
        await message.guild.voice_client.disconnect()
    except Exception as e:
        pass


async def tts_command(message: disnake.Message) -> None:
    text = " ".join(message.content.split()[1:])

    if not text:
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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


async def play_command(message: disnake.Message) -> None:
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
        embed = disnake.Embed(
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
    except disnake.ClientException:
        vc = message.guild.voice_client

    if vc.is_playing():
        vc.stop()

    try:
        with yt_dlp.YoutubeDL({"format": "bestaudio", "noplaylist": "True"}) as ydl:
            info = ydl.extract_info(query, download=False)
            URL = info["url"]
            title = info["title"]
    except Exception as e:
        embed = disnake.Embed(
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
        disnake.FFmpegPCMAudio(
            URL,
            **{
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn",
            },
        )
    )

    embed = disnake.Embed(
        title="Now Playing",
        description=f"Now playing: {title}",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def profile_command(message: disnake.Message) -> None:
    if len(message.mentions) < 1:
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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
        fetched_user = await Memo.fetch_user(user.id)

    except disnake.errors.NotFound as e:
        embed = disnake.Embed(
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

    except disnake.errors.HTTPException as e:
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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


async def nick_command(message: disnake.Message) -> None:
    if (
        not message.author.guild_permissions.administrator
        | message.author.guild_permissions.administrator
    ):
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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
        embed = disnake.Embed(
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


async def feedback_command(message: disnake.Message) -> None:
    args = message.content.split()[1:]
    feedback_text = " ".join(args)

    if len(args) < 1:
        embed = disnake.Embed(
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
async def restart_command(message: disnake.Message) -> None:
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

    for vc in Memo.voice_clients:
        await vc.disconnect(force=True)

    if hasattr(Memo.http, "_client_session") and Memo.http._client_session:
        await Memo.http._client_session.close()
        await asyncio.sleep(0.5)

    try:
        await Memo.close()
    except:
        pass

    os.execv(sys.executable, ["python"] + sys.argv)


async def translate_command(message: disnake.Message) -> None:
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


async def ping_command(message: disnake.Message) -> None:
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


async def server_command(message: disnake.Message) -> None:
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


async def joke_command(message: disnake.Message) -> None:
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


async def coin_command(message: disnake.Message) -> None:
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


async def quote_command(message: disnake.Message) -> None:
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


async def vc_mute_command(message: disnake.Message) -> None:
    if len(message.mentions) < 1:
        await message.channel.send("Please mention a valid member.")
        return

    member = message.guild.get_member(message.mentions[0].id)

    if not member:
        await message.channel.send("Please mention a valid member.")
        return

    if not member.voice:
        await message.channel.send("That user is not in a voice channel.")
        return

    member.edit(mute=True)


async def vc_unmute_command(message: disnake.Message) -> None:
    if len(message.mentions) < 1:
        await message.channel.send("Please mention a valid member.")
        return

    member = message.guild.get_member(message.mentions[0].id)

    if not member:
        await message.channel.send("Please mention a valid member.")
        return

    member.edit(mute=False)


async def vc_deafen_command(message: disnake.Message) -> None:
    if len(message.mentions) < 1:
        await message.channel.send("Please mention a valid member.")
        return

    member = message.guild.get_member(message.mentions[0].id)

    if not member:
        await message.channel.send("Please mention a valid member.")
        return

    member.edit(deafen=True)


async def vc_undeafen_command(message: disnake.Message) -> None:
    if len(message.mentions) < 1:
        await message.channel.send("Please mention a valid member.")
        return

    member = message.guild.get_member(message.mentions[0].id)

    if not member:
        await message.channel.send("Please mention a valid member.")
        return

    member.edit(deafen=False)


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


@Memo.event
async def on_member_join(member: disnake.Member):
    channel = member.guild.text_channels[0]

    if not channel:
        return

    embed = disnake.Embed(
        title=f"Welcome to the server {member.mention}!",
        color=color_manager.get_color("Green"),
        timestamp=datetime.datetime.utcnow(),
    )

    embed.add_field(
        name="Account Created At", value=f"<t:{int(member.created_at.timestamp())}:F>"
    )
    embed.set_thumbnail(member.avatar.url)
    embed.set_footer(FOOTER_TEXT, FOOTER_ICON)
    await channel.send(embed=embed)


@Memo.event
async def on_member_remove(member: disnake.Member):
    channel = member.guild.text_channels[0]

    if not channel:
        return

    embed = disnake.Embed(
        title=f"Goodbye {member.mention}!",
        color=color_manager.get_color("Red"),
        timestamp=datetime.datetime.utcnow(),
    )

    embed.set_thumbnail(member.avatar.url)
    embed.set_footer(FOOTER_TEXT, FOOTER_ICON)
    await channel.send(embed=embed)


@commands.slash_command(name="help", description="Shows the command help embed")
async def slash_help(interaction: disnake.ApplicationCommandInteraction):
    embed = fetch_help_embed(
        color_manager, BOT_NAME, BOT_VERSION, BOT_PREFIX, FOOTER_TEXT, FOOTER_ICON
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@commands.slash_command(
    name="info", description="Shows important information about the bot."
)
async def slash_info(interaction: disnake.ApplicationCommandInteraction):
    embed = fetch_info_embed(
        color_manager, BOT_NAME, BOT_VERSION, BOT_PREFIX, FOOTER_TEXT, FOOTER_ICON
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)
```

# src\utils\helper.py

```py
from typing import Optional, Tuple, List, Dict, Any, Union
from rich import print as richPrint
import json
import datetime
import disnake
import aiohttp
import requests
import ssl
import os
import urllib3
from disnake.ext import commands
import tempfile
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
from gtts import gTTS
import hashlib


class SHA3:
    @staticmethod
    def salt_hash(
        input_str: str, salt: Optional[bytes] = None
    ) -> Tuple[Union[str, bytes], bytes]:
        """
        Generate a salted hash of the input string using PBKDF2 HMAC-SHA256.
        """
        if salt is None:
            salt = SHA3.generate_salt(size=32, hex=True)
        encoded_str = input_str.encode("utf-8")
        hashed = hashlib.pbkdf2_hmac("sha256", encoded_str, salt, 100000)
        return salt, hashed

    @staticmethod
    def hash_256(input_str: str) -> str:
        """
        Generate a SHA-256 hash of the input string.
        """
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_256(encoded_str).hexdigest()

    @staticmethod
    def hash_384(input_str: str) -> str:
        """
        Generate a SHA-384 hash of the input string.
        """
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_384(encoded_str).hexdigest()

    @staticmethod
    def hash_512(input_str: str) -> str:
        """
        Generate a SHA-512 hash of the input string.
        """
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_512(encoded_str).hexdigest()

    @staticmethod
    def hash_224(input_str: str) -> str:
        """
        Generate a SHA-224 hash of the input string.
        """
        encoded_str = input_str.encode("utf-8")
        return hashlib.sha3_224(encoded_str).hexdigest()

    @staticmethod
    def generate_salt(size: int = 32, hex: bool = True) -> Union[str, bytes]:
        """
        Generate a random salt of the specified size.
        """
        salt = os.urandom(size).hex() if hex else os.urandom(size)
        return salt

    @staticmethod
    def compare_hash_to_salted(
        stored_salt: bytes, salted_and_hashed: bytes, hashed: str
    ) -> bool:
        """
        Compare a salted hash to a stored salted hash.
        """
        _, new_hash = SHA3.salt_hash(hashed, stored_salt)
        return new_hash == salted_and_hashed


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
        richPrint(f"ERROR_LOG ~ Text-to-speech conversion failed: {e}")


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load the configuration from a JSON file.
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


def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """
    Save the configuration to a JSON file.
    """
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        richPrint(f"ERROR: Failed to save config to {config_path}: {e}")


def log_info(value: str = "None", startup_log: bool = False) -> None:
    """
    Log an information message with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp, end=" ")
    richPrint(
        f"[bold][blue]INFO[/blue][/bold]     {"[purple]startup.[/purple]" if startup_log else ""}{value}"
    )


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
        richPrint(f"ERROR: Failed to generate character image: {e}")
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
        richPrint(f"ERROR: Language detection failed: {e}")
        return "unknown"


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
            "usage": f"{bot_prefix}unban [user_id]",
        },
    }

    for cmd, info in commands.items():
        help_embed.add_field(
            name=f"{bot_prefix}{cmd}",
            value=f"{info['desc']}\nUsage: `{info['usage']}`",
            inline=False,
        )

    return help_embed


def fetch_info_embed(
    color_manager: "ColorManager", bot_name: str, bot_version: str, bot_prefix: str
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
            richPrint(f"ERROR: Failed to create color embed: {e}")
            return disnake.Embed(title=title, description=description)
```

# website\404.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found | Memo Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
    
    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
</head>
<body class="bg-gray-100 text-gray-800 flex flex-col min-h-screen">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>
    
    <main class="flex-grow flex items-center justify-center px-4">
        <div class="text-center">
            <h1 class="text-6xl font-bold text-blue-600 mb-4">404</h1>
            <p class="text-2xl mb-8">Oops! Page not found</p>
            <p class="text-xl mb-8">It seems like Memo Bot couldn't find the page you're looking for.</p>
            <div class="flex justify-center space-x-4">
                <a href="https://Memo.nerd-bear.org/" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-150 ease-in-out transform hover:scale-105">
                    Return to Homepage
                </a>
                <button onclick="location.reload()" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-150 ease-in-out transform hover:scale-105">
                    Reload Page
                </button>
            </div>
        </div>
    </main>
    
    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('h1', {duration: 1, y: -50, opacity: 0, ease: 'bounce'});
            gsap.from('p', {duration: 1, y: 50, opacity: 0, stagger: 0.2});
            gsap.from('a, button', {duration: 1, opacity: 100, y: 20, delay: 1, stagger: 0.2});
        });
    </script>
</body>
</html>
```

# website\articles\add-feedback.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Feedback Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Feedback Guide">
    <meta property="og:description" content="Learn how to submit feedback for Memo Bot using the feedback command. Your input helps improve the bot!">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/support/article/add-feedback">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">Submitting Feedback for Memo Bot</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">Memo Bot Developer</p>
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
                    <p class="mb-4">Your feedback is crucial for the continuous improvement of Memo Bot. Whether you've encountered a bug, have a feature request, or simply want to share your thoughts, we want to hear from you! The feedback command makes it easy to submit your input directly through Discord.</p>

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
                        <li>Your input may influence future updates and improvements to Memo Bot.</li>
                        <li>For urgent issues, consider also reaching out through our support channels.</li>
                    </ol>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Best Practices for Submitting Feedback</h3>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li>Be specific: Provide as much detail as possible about your experience or suggestion.</li>
                        <li>One idea per submission: If you have multiple suggestions, submit them separately for easier processing.</li>
                        <li>Be constructive: Explain not just what you dislike, but how you think it could be improved.</li>
                        <li>Include context: Mention your server size, the command you were using, or any relevant settings.</li>
                    </ul>

                    <p class="text-lg font-semibold mt-8">Your feedback plays a vital role in shaping the future of Memo Bot. We appreciate every submission and take your input seriously in our development process.</p>

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
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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

# website\articles\articles.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Articles</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Articles">
    <meta property="og:description" content="Explore all articles about Memo Bot, including guides on commands, configuration, and feedback submission.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/articles">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/articles" class="hover:text-blue-600 transition">Articles</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <h2 class="text-4xl font-bold mb-8 text-center">Memo Bot Articles</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Config Guide Article -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Configuration Guide</h3>
                    <p class="text-gray-600 mb-4">Learn how to configure Memo Bot for your server's needs.</p>
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
                    <p class="text-gray-600 mb-4">Learn how to submit feedback to help improve Memo Bot.</p>
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
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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

# website\articles\commands-guide.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Commands Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Commands Guide">
    <meta property="og:description" content="Learn how to use Memo Bot's commands effectively for server management and user interaction.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/support/article/commands-guide">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">Memo Bot Commands Guide</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">Memo Bot Developer</p>
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
                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Getting Started with Memo Bot Commands</h3>
                    <p class="mb-4">Memo Bot comes packed with a variety of commands to help you manage your server and engage with your community. In this guide, we'll walk you through the most important commands and how to use them effectively.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Basic Command Structure</h4>
                    <p class="mb-4">All Memo Bot commands start with a prefix. By default, this prefix is set to "?", but it can be customized in the config file. Here's the basic structure of a command:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?commandName [argument1] [argument2] ...</pre>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Essential Commands</h3>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">1. Help Command</h4>
                    <p class="mb-4">The help command is your go-to for information about all available commands:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?help</pre>
                    <p>This will display a list of all available commands along with a brief description of each.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">2. Moderation Commands</h4>
                    <p class="mb-4">Memo Bot offers several moderation commands to help you manage your server:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>Kick:</strong> ?kick @user [reason]</li>
                        <li><strong>Ban:</strong> ?ban @user [reason]</li>
                        <li><strong>Unban:</strong> ?unban @user</li>
                        <li><strong>Timeout:</strong> ?timeout @user &lt;duration&gt; &lt;unit&gt; [reason]</li>
                    </ul>
                    <p>Remember, you need the appropriate permissions to use these commands.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">3. Fun and Utility Commands</h4>
                    <p class="mb-4">Memo Bot also includes commands for entertainment and utility:</p>
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
                    <p class="mb-4">Here are some tips to help you get the most out of Memo Bot:</p>
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

                    <p class="text-lg font-semibold mt-8">Remember, the key to effectively using Memo Bot is experimentation. Don't be afraid to try out different commands and see how they can benefit your server!</p>

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
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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

# website\articles\config-guide.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Config Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
    
    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Config Guide">
    <meta property="og:description" content="Learn how to change and use the config file for Memo Bot, a versatile Discord bot for server management and user interaction.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/support/article/config-guide">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">Memo Bot Config Guide</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">Memo Bot Developer</p>
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
                    <p class="mb-4">The config file for Memo Bot is a JSON file named <code class="bg-gray-100 p-1 rounded">config.json</code>. It contains various settings that control the bot's behavior. Let's dive into its structure and how you can customize it to suit your needs.</p>

                    <pre class="bg-gray-100 p-4 rounded-md mb-4 overflow-x-auto">
{
    "defaults": {
        "prefix": "?",
        "footer_text": "This bot is created and hosted by Nerd bear",
        "footer_icon": "https://as2.ftcdn.net/v2/jpg/01/17/00/87/1000_F_117008730_0Dg5yniuxPQLz3shrJvLIeBsPfPRBSE1.jpg"
    },
    "bot_version": "0.4.6",
    "bot_name": "Memo",
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
                    <p class="mb-4">Customizing your Memo Bot installation is straightforward. Follow these steps to modify the config file:</p>
                    <ol class="list-decimal list-inside mb-4 space-y-2">
                        <li>Locate the <code class="bg-gray-100 p-1 rounded">config.json</code> file in your bot's root directory.</li>
                        <li>Open the file with a text editor (e.g., Notepad++, Visual Studio Code).</li>
                        <li>Make your desired changes, ensuring to maintain the correct JSON format.</li>
                        <li>Save the file after making changes.</li>
                        <li>Restart the bot for the changes to take effect.</li>
                    </ol>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Common Modifications</h3>
                    <p class="mb-4">Let's explore some common modifications you might want to make to your Memo Bot configuration:</p>

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

                    <p class="text-lg font-semibold mt-8">Remember, customizing your Memo Bot is all about making it work best for your server and community. Don't be afraid to experiment with different settings to find what works best for you!</p>

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
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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

# website\commands\ban\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Ban Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Ban Command">
    <meta property="og:description" content="Learn how to use the ban command in Memo Bot to moderate your server.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/ban">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Ban Command</h1>
            <p class="text-xl text-gray-600">Permanently remove a user from your server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?ban @user [reason]
                    </div>
                    <p class="mb-4">The ban command allows moderators to permanently remove a user from the server. The user cannot rejoin unless unbanned.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to ban (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional: Reason for the ban</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic ban:</p>
                            <pre class="bg-gray-50 rounded p-4">?ban @UserName</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Ban with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?ban @UserName 7 Repeated violations of server rules</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Banned</p>
                                    <p class="text-gray-600">@UserName has been banned.</p>
                                    <p class="text-gray-600">Reason: Repeated violations of server rules</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Ban Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/unban" class="text-blue-600 hover:text-blue-800">?unban</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>The bot must have a role higher than the banned user</li>
                        <li>Banned users cannot rejoin with invites</li>
                        <li>The bot will attempt to DM the user the reason for their ban</li>
                        <li>Server owner cannot be banned</li>
                        <li>Ban is logged in the server's audit log</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\charinfo\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Character Info Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Character Info Command">
    <meta property="og:description" content="Get detailed information about any character using Memo Bot's charinfo command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/charinfo">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Character Info Command</h1>
            <p class="text-xl text-gray-600">Get detailed Unicode information about any character</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?charinfo [character]
                    </div>
                    <p class="mb-4">The charinfo command provides detailed Unicode information about any character, including emojis, special characters, and letters.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">character</code> - The character you want to analyze</li>
                        </ul>
                    </div>
                </section>

                <!-- Information Provided Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Information Provided</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Basic Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Original character</li>
                                <li>Character name</li>
                                <li>Character category</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Unicode Data:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Unicode value (U+XXXX)</li>
                                <li>Unicode escape sequence</li>
                                <li>Full Unicode escape</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Additional Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Python escape sequence</li>
                                <li>Character preview</li>
                                <li>Visual representation</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Get info about an emoji:</p>
                            <pre class="bg-gray-50 rounded p-4">?charinfo 😀</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Get info about a special character:</p>
                            <pre class="bg-gray-50 rounded p-4">?charinfo ♠</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Get info about a letter:</p>
                            <pre class="bg-gray-50 rounded p-4">?charinfo A</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Character info</p>
                                    <p class="text-gray-600">Information on character: A</p>
                                    <p class="text-gray-600">Original character: A</p>
                                    <p class="text-gray-600">Character name: LATIN CAPITAL LETTER A</p>
                                    <p class="text-gray-600">Character category: Lu</p>
                                    <p class="text-gray-600">Unicode value: U+0041</p>
                                    <p class="text-gray-600">Unicode escape: \u0041</p>
                                    <p class="text-gray-600">Full Unicode escape: \U00000041</p>
                                    <p class="text-gray-600">Python escape: 'A'</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">ERROR</p>
                                    <p class="text-red-600">Please provide a character to get information about.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Supported Characters</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Standard letters</li>
                        <li>Numbers</li>
                        <li>Emojis</li>
                        <li>Special symbols</li>
                        <li>Unicode characters</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Uses</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Finding Unicode values</li>
                        <li>Getting character names</li>
                        <li>Learning character categories</li>
                        <li>Getting escape sequences</li>
                        <li>Character analysis</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\coin\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Coin Flip Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Coin Flip Command">
    <meta property="og:description" content="Flip a virtual coin using Memo Bot's coin command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/coin">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Coin Flip Command</h1>
            <p class="text-xl text-gray-600">Flip a virtual coin and get heads or tails</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?coin
                    </div>
                    <p class="mb-4">The coin command flips a virtual coin and displays the result. The bot will first announce it's flipping the coin, then show whether it landed on heads or tails.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?coin</li>
                        </ul>
                    </div>
                </section>

                <!-- How It Works Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">How It Works</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-medium mb-4">The coin flip happens in two steps:</p>
                            <ol class="list-decimal list-inside space-y-2">
                                <li class="p-2">Bot announces "Flipping a coin..."</li>
                                <li class="p-2">Result is shown: "The coin landed on heads/tails!"</li>
                            </ol>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Flip a coin:</p>
                            <pre class="bg-gray-50 rounded p-4">?coin</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="text-gray-600">Flipping a coin...</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">The coin landed on heads! 🪙</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Possible Results</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Heads</li>
                        <li>Tails</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Best Used For</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Making random decisions</li>
                        <li>Settling debates</li>
                        <li>Simple games</li>
                        <li>Quick choices</li>
                        <li>Team selection</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Results are random</li>
                        <li>50/50 probability</li>
                        <li>Shows flipping animation</li>
                        <li>Works in any channel</li>
                        <li>Instant results</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\feedback\index.html

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Memo Bot - Feedback Command</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

        <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
        
        <meta property="og:title" content="Memo Bot | Feedback Command">
        <meta property="og:description" content="Learn how to submit feedback to help improve Memo Bot.">
        <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
        <meta property="og:url" content="https://Memo.nerd-bear.org/commands/feedback">
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
                    <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
                </h1>
                <ul class="flex space-x-6">
                    <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                    <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                    <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                    <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
                </ul>
            </div>
        </nav>

        <main class="container mx-auto mt-12 p-6">
            <!-- Command Header -->
            <div class="mb-8">
                <div class="flex items-center gap-4 mb-4">
                    <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                    <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                </div>
                <h1 class="text-4xl font-bold mb-2">Feedback Command</h1>
                <p class="text-xl text-gray-600">Submit feedback to help improve Memo Bot</p>
            </div>

            <!-- Command Card Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Main Content -->
                <div class="md:col-span-2 space-y-8">
                    <!-- Usage Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Usage</h2>
                        <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                            ?feedback [message]
                        </div>
                        <p class="mb-4">The feedback command allows you to submit suggestions, bug reports, or general feedback about Memo Bot. All feedback is stored and reviewed regularly by the development team.</p>
                        <div class="space-y-2">
                            <p><strong>Arguments:</strong></p>
                            <ul class="list-disc list-inside pl-4">
                                <li><code class="bg-gray-100 px-1 rounded">message</code> - Your feedback message</li>
                            </ul>
                        </div>
                    </section>

                    <!-- Best Practices Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Feedback Best Practices</h2>
                        <div class="space-y-4">
                            <div class="p-4 bg-gray-50 rounded">
                                <p class="font-bold mb-2">Good Feedback Examples:</p>
                                <ul class="list-disc list-inside text-gray-600">
                                    <li>Bug reports with steps to reproduce</li>
                                    <li>Specific feature requests</li>
                                    <li>Detailed improvement suggestions</li>
                                    <li>Command enhancement ideas</li>
                                </ul>
                            </div>
                            <div class="p-4 bg-yellow-50 rounded">
                                <p class="font-bold text-yellow-800 mb-2">Avoid:</p>
                                <ul class="list-disc list-inside text-yellow-700">
                                    <li>Abuse or harassment</li>
                                    <li>Spam submissions</li>
                                    <li>Very short/vague feedback</li>
                                    <li>Support requests (use ?help instead)</li>
                                </ul>
                            </div>
                        </div>
                    </section>

                    <!-- Examples Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Examples</h2>
                        <div class="space-y-4">
                            <div>
                                <p class="font-medium mb-2">Bug report:</p>
                                <pre class="bg-gray-50 rounded p-4">?feedback The ?play command sometimes fails to join voice channels in servers with over 1000 members</pre>
                            </div>
                            <div>
                                <p class="font-medium mb-2">Feature request:</p>
                                <pre class="bg-gray-50 rounded p-4">?feedback Would be great to have a queue system for the music commands</pre>
                            </div>
                            <div>
                                <p class="font-medium mb-2">General feedback:</p>
                                <pre class="bg-gray-50 rounded p-4">?feedback Love the profile command! Maybe add an option to show favorite channels?</pre>
                            </div>
                        </div>
                    </section>

                    <!-- Response Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                        <div class="space-y-4">
                            <div class="border rounded p-4">
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                    <span class="font-medium">Memo Bot</span>
                                </div>
                                <div class="pl-10">
                                    <div class="bg-gray-50 rounded p-4">
                                        <p class="font-medium">Feedback Received</p>
                                        <p class="text-gray-600">Thank you for your feedback! Your message has been stored and will be reviewed by our team.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="border rounded p-4 border-red-200">
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                    <span class="font-medium">Memo Bot</span>
                                </div>
                                <div class="pl-10">
                                    <div class="bg-red-50 rounded p-4">
                                        <p class="font-medium text-red-800">Error</p>
                                        <p class="text-red-600">Please provide a feedback message. Usage: ?feedback [message]</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>

                <!-- Sidebar -->
                <div class="space-y-6">
                    <!-- Required Permissions -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                        <ul class="space-y-2 text-gray-600">
                            <li class="flex items-center gap-2">
                                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                None required
                            </li>
                        </ul>
                    </section>

                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                        <p class="text-gray-600">No cooldown</p>
                    </section>

                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">What Happens Next?</h3>
                        <ul class="space-y-2 text-gray-600 list-disc list-inside">
                            <li>Feedback is securely stored</li>
                            <li>Reviewed by development team</li>
                            <li>Used to guide improvements</li>
                            <li>May influence future updates</li>
                        </ul>
                    </section>

                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">Tips for Good Feedback</h3>
                        <ul class="space-y-2 text-gray-600 list-disc list-inside">
                            <li>Be specific and detailed</li>
                            <li>One idea per submission</li>
                            <li>Include examples if possible</li>
                            <li>Explain why it matters</li>
                            <li>Be constructive</li>
                        </ul>
                    </section>
                </div>
            </div>
        </main>

        <footer class="bg-gray-100 mt-24 py-8">
            <div class="container mx-auto text-center text-gray-600">
                <p>&copy; 2024 Memo Bot. All rights reserved.</p>
                <div class="mt-4">
                    <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                    <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                    <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
                </div>
            </div>
        </footer>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
                gsap.from('main > *', {
                    duration: 0.5,
                    opacity: 0,
                    y: 20,
                    stagger: 0.1,
                    ease: 'power2.out'
                });
            });
        </script>
    </body>
    </html>
```

# website\commands\help\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Help Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Help Command">
    <meta property="og:description" content="Learn how to use the help command in Memo Bot to learn more about the commands you can use.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/help">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Help Command</h1>
            <p class="text-xl text-gray-600">Display a list of all available commands.</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?help
                    </div>
                    <p class="mb-4">The help command shows you a large embed of all the commands that you can run in the guild along with their short description.</p>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Help:</p>
                            <pre class="bg-gray-50 rounded p-4">?help</pre>
                        </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Memo Help Information</p>
                                    <p class="text-gray-600">?tts</p>
                                    <p class="text-gray-600 font-bold">Join the vc you are in and uses Text-to-Speech to say your text<br/><code>Usage: ?tts [input_text]</code></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/profile" class="text-blue-600 hover:text-blue-800">?profile</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/server" class="text-blue-600 hover:text-blue-800">?server</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/charinfo" class="text-blue-600 hover:text-blue-800">?charinfo</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>There are some commands that are marked as secret/easter egg commands and are not documented.</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Commands</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <meta property="og:title" content="Memo Bot | Commands">
    <meta property="og:description" content="Explore all available commands for Memo Bot, including moderation, music, utility, and fun features.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands">
    <meta property="og:type" content="website">

    <style>
        .command-card {
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .command-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://Memo.nerd-bear.org/" class="mb-8">
                <img src="https://Memo.nerd-bear.org/pfp-5.png" alt="Memo Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-center text-gray-900">Command List</h2>
            <p class="text-xl text-gray-600 mb-8 text-center">Explore all available commands for Memo Bot</p>
        </div>

        <div class="mb-8">
            <div class="flex flex-col md:flex-row gap-4">
                <input type="text" id="search-input" placeholder="Search commands..." class="flex-grow p-2 border border-gray-300 rounded-md">
                <select id="category-filter" class="p-2 border border-gray-300 rounded-md">
                    <option value="all">All Categories</option>
                    <option value="moderation">Moderation</option>
                    <option value="music">Music</option>
                    <option value="utility">Utility</option>
                    <option value="fun">Fun</option>
                </select>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="commands-grid">
            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?kick</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Kick a user from the server with an optional reason.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/kick" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?ban</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Ban a user from the server with an optional reason.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/ban" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?unban</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Unban a previously banned user.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/unban" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?timeout</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Timeout a user for a specified duration.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/timeout" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?nick</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Change a user's nickname.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/nick" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="music">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?play</h3>
                        <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
                    </div>
                    <p class="text-gray-600 text-sm">Play a song from YouTube in your voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/play" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="music">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?join</h3>
                        <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
                    </div>
                    <p class="text-gray-600 text-sm">Make the bot join your voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/join" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="music">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?leave</h3>
                        <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
                    </div>
                    <p class="text-gray-600 text-sm">Make the bot leave the voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/leave" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?help</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Display a list of all available commands.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/help" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?profile</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">View detailed information about a user's profile.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/profile" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?feedback</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Submit feedback about the bot.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/feedback" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?translate</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Translate text to English from any language.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/translate" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?ping</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Check the bot's current latency.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/ping" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?server</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">View detailed information about the server.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/server" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?charinfo</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Get detailed information about a character or emoji.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/charinfo" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?tts</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Convert text to speech in a voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/tts" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?joke</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Get a random dad joke.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/joke" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?coin</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Flip a coin and get heads or tails.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/coin" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?quote</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Get the quote of the day.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/quote" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-2">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.getElementById('search-input');
            const categoryFilter = document.getElementById('category-filter');
            const commandCards = document.querySelectorAll('.command-card');

            function filterCommands() {
                const searchTerm = searchInput.value.toLowerCase();
                const selectedCategory = categoryFilter.value;

                commandCards.forEach(card => {
                    const commandText = card.textContent.toLowerCase();
                    const cardCategory = card.dataset.category;
                    const matchesSearch = commandText.includes(searchTerm);
                    const matchesCategory = selectedCategory === 'all' || cardCategory === selectedCategory;

                    if (matchesSearch && matchesCategory) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }

            searchInput.addEventListener('input', filterCommands);
            categoryFilter.addEventListener('change', filterCommands);

            gsap.from('.command-card', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>

</html>
```

# website\commands\join\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Join Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Join Command">
    <meta property="og:description" content="Learn how to make Memo Bot join your voice channel using the join command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/join">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Join Command</h1>
            <p class="text-xl text-gray-600">Make the bot join your current voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?join
                    </div>
                    <p class="mb-4">The join command makes Memo Bot join your current voice channel. You must be in a voice channel for this command to work.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Bot joins your current voice channel</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic usage:</p>
                            <pre class="bg-gray-50 rounded p-4">?join</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Joined Voice Channel</p>
                                    <p class="text-gray-600">Successfully joined General</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">You must be in a voice channel to use this command.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Voice Channel Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Voice Channel Requirements</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">For the command to work:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>You must be in a voice channel</li>
                                <li>The voice channel must be visible to the bot</li>
                                <li>The bot must have permission to join the channel</li>
                                <li>The voice channel must not be at capacity</li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Connect
                        </li>
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            View Channel
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/leave" class="text-blue-600 hover:text-blue-800">?leave</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/play" class="text-blue-600 hover:text-blue-800">?play</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>User not in a voice channel</li>
                        <li>Bot missing permissions</li>
                        <li>Voice channel at capacity</li>
                        <li>Region voice server issues</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot stays in channel until disconnected</li>
                        <li>Will automatically disconnect after inactivity</li>
                        <li>Can be used before playing music</li>
                        <li>Works in any accessible voice channel</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\joke\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Joke Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Joke Command">
    <meta property="og:description" content="Get a random dad joke using Memo Bot's joke command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/joke">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Joke Command</h1>
            <p class="text-xl text-gray-600">Get a random dad joke to lighten the mood</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?joke
                    </div>
                    <p class="mb-4">The joke command returns a random dad joke. Each time you use the command, you'll get a different joke!</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?joke</li>
                        </ul>
                    </div>
                </section>

                <!-- Example Jokes Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example Jokes</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-medium mb-2">Sample Responses:</p>
                            <ul class="space-y-4 text-gray-600">
                                <li class="p-2 bg-white rounded shadow-sm">"Why don't eggs tell jokes? They'd Memok up!"</li>
                                <li class="p-2 bg-white rounded shadow-sm">"What do you call a fake noodle? An impasta!"</li>
                                <li class="p-2 bg-white rounded shadow-sm">"Why did the scarecrow win an award? He was outstanding in his field!"</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Get a random joke:</p>
                            <pre class="bg-gray-50 rounded p-4">?joke</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Dad Joke Time! 😄</p>
                                    <p class="text-gray-600">Why don't eggs tell jokes?</p>
                                    <p class="text-gray-600">They'd Memok up!</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Features</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Random selection</li>
                        <li>Family-friendly content</li>
                        <li>Classic dad humor</li>
                        <li>Different joke every time</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Best Used For</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Breaking the ice</li>
                        <li>Lightening the mood</li>
                        <li>Starting conversations</li>
                        <li>Having a quick laugh</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>All jokes are dad jokes</li>
                        <li>Content is always clean</li>
                        <li>Jokes may repeat eventually</li>
                        <li>Works in any channel</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\kick\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Kick Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Kick Command">
    <meta property="og:description" content="Learn how to use the kick command in Memo Bot to moderate your server.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/kick">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Kick Command</h1>
            <p class="text-xl text-gray-600">Remove a user from your server temporarily</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?kick @user [reason]
                    </div>
                    <p class="mb-4">The kick command allows moderators to remove a user from the server. The user can rejoin with a new invite.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to kick (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional reason for the kick</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic kick:</p>
                            <pre class="bg-gray-50 rounded p-4">?kick @UserName</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Kick with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?kick @UserName Spamming in general chat</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Kicked</p>
                                    <p class="text-gray-600">@UserName has been kicked.</p>
                                    <p class="text-gray-600">Reason: Spamming in general chat</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Kick Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/unban" class="text-blue-600 hover:text-blue-800">?unban</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>The bot must have a role higher than the kicked user</li>
                        <li>Kicked users can rejoin with a new invite</li>
                        <li>The bot will attempt to DM the user the reason for their kick</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\leave\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Leave Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Leave Command">
    <meta property="og:description" content="Learn how to make Memo Bot leave your voice channel using the leave command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/leave">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Leave Command</h1>
            <p class="text-xl text-gray-600">Make the bot leave its current voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?leave
                    </div>
                    <p class="mb-4">The leave command makes Memo Bot leave the voice channel it's currently in. The bot must be in a voice channel for this command to work.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Bot leaves its current voice channel</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic usage:</p>
                            <pre class="bg-gray-50 rounded p-4">?leave</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Left Voice Channel</p>
                                    <p class="text-gray-600">Successfully left General</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">I'm not in a voice channel.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Command Behavior Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Command Behavior</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">When using this command:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Bot will stop any currently playing audio</li>
                                <li>Bot will immediately disconnect from the voice channel</li>
                                <li>Command can be used by any member</li>
                                <li>No need to be in the same voice channel as the bot</li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/join" class="text-blue-600 hover:text-blue-800">?join</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/play" class="text-blue-600 hover:text-blue-800">?play</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot not in any voice channel</li>
                        <li>Bot temporarily unresponsive</li>
                        <li>Network connectivity issues</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Stops any playing audio</li>
                        <li>Can be used from any channel</li>
                        <li>Immediate disconnection</li>
                        <li>No confirmation needed</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\nick\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Nickname Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Nickname Command">
    <meta property="og:description" content="Learn how to use the nickname command in Memo Bot to change user nicknames.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/nick">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Nickname Command</h1>
            <p class="text-xl text-gray-600">Change a user's nickname in the server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?nick @user [new_nickname]
                    </div>
                    <p class="mb-4">The nickname command allows moderators to change a user's display name in the server. If no new nickname is provided, it will reset to their original username.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to rename (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">new_nickname</code> - Optional: New nickname for the user (omit to reset)</li>
                        </ul>
                    </div>
                </section>

                <!-- Nickname Rules Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Nickname Rules</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Length Requirements:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Minimum: 1 character</li>
                                <li>Maximum: 32 characters</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-yellow-50 rounded">
                            <p class="font-bold text-yellow-800 mb-2">Restrictions:</p>
                            <ul class="list-disc list-inside text-yellow-700">
                                <li>Cannot contain Discord's blocked words</li>
                                <li>Cannot contain server-specific blocked words</li>
                                <li>Cannot impersonate other users</li>
                                <li>Cannot use certain special characters</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Set new nickname:</p>
                            <pre class="bg-gray-50 rounded p-4">?nick @UserName Cool Person</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Reset nickname:</p>
                            <pre class="bg-gray-50 rounded p-4">?nick @UserName</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Nickname Changed</p>
                                    <p class="text-gray-600">Changed nickname for @UserName to "Cool Person"</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">Cannot change nickname: Missing permissions or nickname invalid.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Manage Nicknames
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot must have a role higher than the user</li>
                        <li>Cannot change server owner's nickname</li>
                        <li>Changes are logged in the audit log</li>
                        <li>Users with "Change Nickname" permission can change their own nickname</li>
                        <li>Nickname changes are immediate</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Nickname too long (>32 characters)</li>
                        <li>Contains blocked words or characters</li>
                        <li>Bot role hierarchy insufficient</li>
                        <li>User has higher roles than bot</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\ping\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Ping Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Ping Command">
    <meta property="og:description" content="Check Memo Bot's response time using the ping command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/ping">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Ping Command</h1>
            <p class="text-xl text-gray-600">Check the bot's current response time</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?ping
                    </div>
                    <p class="mb-4">The ping command shows the bot's current latency (response time) in milliseconds. This can help you check if the bot is experiencing any delays or connection issues.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?ping</li>
                        </ul>
                    </div>
                </section>

                <!-- Understanding Latency Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Understanding Latency</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-green-50 rounded">
                            <p class="font-bold text-green-800 mb-2">Good Latency:</p>
                            <p class="text-green-700">50-150ms</p>
                        </div>
                        <div class="p-4 bg-yellow-50 rounded">
                            <p class="font-bold text-yellow-800 mb-2">Moderate Latency:</p>
                            <p class="text-yellow-700">150-300ms</p>
                        </div>
                        <div class="p-4 bg-red-50 rounded">
                            <p class="font-bold text-red-800 mb-2">High Latency:</p>
                            <p class="text-red-700">300ms+</p>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Check bot latency:</p>
                            <pre class="bg-gray-50 rounded p-4">?ping</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">🏓 Pong!</p>
                                    <p class="text-gray-600">Bot Latency: 87ms</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">When to Use</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot seems unresponsive</li>
                        <li>Commands are delayed</li>
                        <li>Checking connection quality</li>
                        <li>Troubleshooting issues</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Latency varies by region</li>
                        <li>Results may fluctuate</li>
                        <li>Lower is better</li>
                        <li>Simple health check tool</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\play\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Play Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Play Command">
    <meta property="og:description" content="Learn how to use the play command in Memo Bot to play music from YouTube in your voice channel.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/play">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Play Command</h1>
            <p class="text-xl text-gray-600">Play music from YouTube in your voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?play youtube_url
                    </div>
                    <p class="mb-4">The play command allows you to play audio from a YouTube video in your current voice channel.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">youtube_url</code> - The full URL of a YouTube video</li>
                        </ul>
                    </div>
                </section>

                <!-- URL Requirements Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">URL Requirements</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Accepted URL Formats:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Standard YouTube URLs (youtube.com/watch?v=...)</li>
                                <li>Short YouTube URLs (youtu.be/...)</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-yellow-50 rounded">
                            <p class="font-bold text-yellow-800 mb-2">Not Supported:</p>
                            <ul class="list-disc list-inside text-yellow-700">
                                <li>YouTube playlists</li>
                                <li>Non-YouTube URLs</li>
                                <li>YouTube Shorts</li>
                                <li>Live streams</li>
                                <li>Age-restricted videos</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Play with standard URL:</p>
                            <pre class="bg-gray-50 rounded p-4">?play https://www.youtube.com/watch?v=dQw4w9WgXcQ</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Play with short URL:</p>
                            <pre class="bg-gray-50 rounded p-4">?play https://youtu.be/dQw4w9WgXcQ</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Now Playing</p>
                                    <p class="text-gray-600">Title: Never Gonna Give You Up</p>
                                    <p class="text-gray-600">Channel: Rick Astley</p>
                                    <p class="text-gray-600">Duration: 3:32</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">Invalid YouTube URL or video unavailable.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Connect
                        </li>
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Speak
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/join" class="text-blue-600 hover:text-blue-800">?join</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/leave" class="text-blue-600 hover:text-blue-800">?leave</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Current Limitations</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>No queue system</li>
                        <li>Cannot pause/resume</li>
                        <li>No volume control</li>
                        <li>No skip function</li>
                        <li>One song at a time</li>
                        <li>Must wait for current song to finish</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Requirements</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Must be in a voice channel</li>
                        <li>Bot must have permission to join</li>
                        <li>Video must be public</li>
                        <li>Video must be available in your region</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\profile\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Profile Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Profile Command">
    <meta property="og:description" content="View detailed Discord profile information using Memo Bot's profile command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/profile">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Profile Command</h1>
            <p class="text-xl text-gray-600">View detailed information about a user's Discord profile</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?profile @user
                    </div>
                    <p class="mb-4">The profile command displays comprehensive information about a user's Discord profile, including their roles, status, badges, and more.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to look up (mention required)</li>
                        </ul>
                    </div>
                </section>

                <!-- Profile Information Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Displayed Information</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Basic Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Display Name</li>
                                <li>Username</li>
                                <li>User ID</li>
                                <li>Account Creation Date</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Status & Roles:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Current Status (Online/Offline/DND/Idle)</li>
                                <li>Top Role</li>
                                <li>All Roles List</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Visual Elements:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Profile Picture</li>
                                <li>Banner (if available)</li>
                                <li>Discord Badges</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Look up user profile:</p>
                            <pre class="bg-gray-50 rounded p-4">?profile @UserName</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">UserName's Profile</p>
                                    <p class="text-gray-600">Display Name: UserName</p>
                                    <p class="text-gray-600">Username: User#1234</p>
                                    <p class="text-gray-600">User ID: 123456789012345678</p>
                                    <p class="text-gray-600">Creation Time: 17/10/24 12:34:56</p>
                                    <p class="text-gray-600">Status: 🟢 Online</p>
                                    <p class="text-gray-600">Top Role: @Admin</p>
                                    <p class="text-gray-600">Roles: @Admin, @Moderator, @Member</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Invalid Usage</p>
                                    <p class="text-red-600">Usage: ?profile @user</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>User not mentioned</li>
                        <li>User not in server</li>
                        <li>Invalid user mention</li>
                        <li>User account deleted</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Status Indicators</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>🟢 Online</li>
                        <li>⛔ Do Not Disturb</li>
                        <li>🟡 Idle</li>
                        <li>⚫ Offline</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Shows all available badges</li>
                        <li>Banner shown if available</li>
                        <li>Shows creation timestamp</li>
                        <li>Lists all user roles</li>
                        <li>Default avatar used if none set</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\quote\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Quote Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Quote Command">
    <meta property="og:description" content="Get a random famous quote using Memo Bot's quote command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/quote">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Quote Command</h1>
            <p class="text-xl text-gray-600">Get an inspiring quote from a famous person</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?quote
                    </div>
                    <p class="mb-4">The quote command returns a random famous quote. Each use of the command provides a different quote from history's most notable figures.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?quote</li>
                        </ul>
                    </div>
                </section>

                <!-- Example Quotes Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example Quotes</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-medium mb-2">Sample Responses:</p>
                            <ul class="space-y-4 text-gray-600">
                                <li class="p-4 bg-white rounded shadow-sm italic">
                                    "Be the change you wish to see in the world."
                                    <div class="text-right font-bold mt-2">- Mahatma Gandhi</div>
                                </li>
                                <li class="p-4 bg-white rounded shadow-sm italic">
                                    "I have not failed. I've just found 10,000 ways that won't work."
                                    <div class="text-right font-bold mt-2">- Thomas A. Edison</div>
                                </li>
                                <li class="p-4 bg-white rounded shadow-sm italic">
                                    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
                                    <div class="text-right font-bold mt-2">- Albert Einstein</div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Get a random quote:</p>
                            <pre class="bg-gray-50 rounded p-4">?quote</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Quote of the Moment ✨</p>
                                    <p class="text-gray-600 italic mt-2">"Success is not final, failure is not fatal: it is the courage to continue that counts."</p>
                                    <p class="text-gray-600 font-bold text-right mt-2">- Winston Churchill</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Quote Categories</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Inspirational</li>
                        <li>Historical</li>
                        <li>Scientific</li>
                        <li>Literary</li>
                        <li>Philosophical</li>
                        <li>Leadership</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Best Used For</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Daily inspiration</li>
                        <li>Starting discussions</li>
                        <li>Channel messages</li>
                        <li>Server greetings</li>
                        <li>Educational content</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Quotes from verified sources</li>
                        <li>Attribution included</li>
                        <li>Family-friendly content</li>
                        <li>Works in any channel</li>
                        <li>Random selection each time</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\server\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Server Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Server Command">
    <meta property="og:description" content="View detailed server statistics using Memo Bot's server command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/server">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Server Command</h1>
            <p class="text-xl text-gray-600">View detailed statistics about the current Discord server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?server
                    </div>
                    <p class="mb-4">The server command displays comprehensive statistics and information about the current Discord server, including member counts, boost status, and more.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Shows information for current server</li>
                        </ul>
                    </div>
                </section>

                <!-- Server Information Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Displayed Information</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Basic Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Server Name</li>
                                <li>Server ID</li>
                                <li>Owner</li>
                                <li>Creation Date</li>
                                <li>Description (if set)</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Member Stats:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Total Members</li>
                                <li>Bot Count</li>
                                <li>Total Channels</li>
                                <li>Role Count</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Boost Information:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Boost Level</li>
                                <li>Total Boosts</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Visual Elements:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Server Icon</li>
                                <li>Server Banner (if set)</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">View server stats:</p>
                            <pre class="bg-gray-50 rounded p-4">?server</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Server Name Server Stats</p>
                                    <p class="text-gray-600">Server ID: 123456789012345678</p>
                                    <p class="text-gray-600">Owner: @ServerOwner</p>
                                    <p class="text-gray-600">Created At: October 17, 2024 12:34:56 PM UTC</p>
                                    <p class="text-gray-600">Boost Level: Level 2</p>
                                    <p class="text-gray-600">Boost Count: 7</p>
                                    <p class="text-gray-600">Members: 1500</p>
                                    <p class="text-gray-600">Bots: 5</p>
                                    <p class="text-gray-600">Total Channels: 20</p>
                                    <p class="text-gray-600">Roles: 15</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Failed to fetch all members</li>
                        <li>HTTP connection errors</li>
                        <li>Permission errors</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Shows server banner if available</li>
                        <li>Displays server icon if set</li>
                        <li>Includes timestamp of check</li>
                        <li>Shows server description if set</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\timeout\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Timeout Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Timeout Command">
    <meta property="og:description" content="Learn how to use the timeout command in Memo Bot to temporarily restrict users.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/timeout">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Timeout Command</h1>
            <p class="text-xl text-gray-600">Temporarily restrict a user's ability to interact with the server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?timeout @user [duration] [unit] [reason]
                    </div>
                    <p class="mb-4">The timeout command temporarily prevents a user from sending messages, reacting to messages, or joining voice channels.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to timeout (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">duration</code> - Number value for the timeout duration</li>
                            <li><code class="bg-gray-100 px-1 rounded">unit</code> - Time unit (s = seconds, m = minutes, h = hours, d = days)</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional: Reason for the timeout</li>
                        </ul>
                    </div>
                </section>

                <!-- Time Units Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Time Units</h2>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">s (Seconds)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 30 s</code></p>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">m (Minutes)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 5 m</code></p>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">h (Hours)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 2 h</code></p>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">d (Days)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 1 d</code></p>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic timeout (1 hour):</p>
                            <pre class="bg-gray-50 rounded p-4">?timeout @UserName 1 h</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Timeout with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?timeout @UserName 1 d Spamming in general chat</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Short timeout (5 minutes):</p>
                            <pre class="bg-gray-50 rounded p-4">?timeout @UserName 5 m Cool down period</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Timed Out</p>
                                    <p class="text-gray-600">@UserName has been timed out for 1 day.</p>
                                    <p class="text-gray-600">Reason: Spamming in general chat</p>
                                    <p class="text-gray-600">Timeout will expire: [timestamp]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Timeout Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/unban" class="text-blue-600 hover:text-blue-800">?unban</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Maximum timeout duration is 28 days</li>
                        <li>Bot must have a role higher than the user</li>
                        <li>Server owner cannot be timed out</li>
                        <li>The bot will attempt to DM the user</li>
                        <li>Timeouts are logged in the audit log</li>
                        <li>Users keep their roles during timeout</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Limitations</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Cannot combine time units</li>
                        <li>Time must be a whole number</li>
                        <li>Timed out users can still read messages</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\translate\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Translate Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Translate Command">
    <meta property="og:description" content="Learn how to translate text to English using Memo Bot's translate command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/translate">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Translate Command</h1>
            <p class="text-xl text-gray-600">Translate text from any language to English</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?translate [text]
                    </div>
                    <p class="mb-4">The translate command automatically detects the language of the input text and translates it to English.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">text</code> - The text you want to translate to English</li>
                        </ul>
                    </div>
                </section>

                <!-- Language Support Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Language Support</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Features:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Automatic language detection</li>
                                <li>Translation to English only</li>
                                <li>Support for most world languages</li>
                                <li>Handles special characters</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Spanish to English:</p>
                            <pre class="bg-gray-50 rounded p-4">?translate Hola, ¿cómo estás?</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">French to English:</p>
                            <pre class="bg-gray-50 rounded p-4">?translate Bonjour, comment allez-vous?</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">German to English:</p>
                            <pre class="bg-gray-50 rounded p-4">?translate Guten Tag, wie geht es dir?</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Translation</p>
                                    <p class="text-gray-600">Original (Spanish): Hola, ¿cómo estás?</p>
                                    <p class="text-gray-600">English: Hello, how are you?</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">Please provide text to translate. Usage: ?translate [text]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>No text provided</li>
                        <li>Text too long</li>
                        <li>Unsupported characters</li>
                        <li>Connection errors</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Limitations</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>English output only</li>
                        <li>Text-only translation</li>
                        <li>No image translation</li>
                        <li>No custom language selection</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Tips</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Keep text concise for best results</li>
                        <li>Proper punctuation helps accuracy</li>
                        <li>Use complete sentences when possible</li>
                        <li>Original text is shown for reference</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\tts\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Text-to-Speech Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Text-to-Speech Command">
    <meta property="og:description" content="Convert text to speech using Memo Bot's TTS command.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/tts">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Text-to-Speech Command</h1>
            <p class="text-xl text-gray-600">Convert text to speech and play it in a voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?tts [message]
                    </div>
                    <p class="mb-4">The TTS command converts your text message into speech and plays it in your current voice channel.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">message</code> - The text you want to convert to speech</li>
                        </ul>
                    </div>
                </section>

                <!-- Requirements Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Requirements</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-blue-50 rounded">
                            <p class="font-bold mb-2">Before Using:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>You must be in a voice channel</li>
                                <li>Bot needs permission to join voice channels</li>
                                <li>Bot needs permission to speak</li>
                                <li>Text must not be empty</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic message:</p>
                            <pre class="bg-gray-50 rounded p-4">?tts Hello everyone!</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Longer message:</p>
                            <pre class="bg-gray-50 rounded p-4">?tts Welcome to our Discord server. Hope you enjoy your stay!</pre>
                        </div>
                    </div>
                </section>

                <!-- Behavior Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Command Behavior</h2>
                    <div class="space-y-4">
                        <ol class="list-decimal list-inside space-y-2">
                            <li>Bot joins your voice channel</li>
                            <li>Converts text to speech</li>
                            <li>Plays the audio</li>
                            <li>Automatically disconnects after playing</li>
                            <li>Cleans up temporary audio files</li>
                        </ol>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Ended TTS</p>
                                    <p class="text-gray-600">Successfully generated and played TTS file. Disconnecting from #General</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Join voice channel</p>
                                    <p class="text-red-600">Please join a voice channel to use this command! Usage: ?tts [message]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Connect
                        </li>
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Speak
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/join" class="text-blue-600 hover:text-blue-800">?join</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/leave" class="text-blue-600 hover:text-blue-800">?leave</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Not in a voice channel</li>
                        <li>Missing message text</li>
                        <li>Bot lacks permissions</li>
                        <li>Channel at capacity</li>
                        <li>TTS generation fails</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Auto-disconnects after playing</li>
                        <li>Stops current audio if playing</li>
                        <li>Works in any voice channel</li>
                        <li>Temporary files are cleaned up</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\commands\unban\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Unban Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Unban Command">
    <meta property="og:description" content="Learn how to use the unban command in Memo Bot to remove bans from users.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/commands/unban">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://Memo.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Unban Command</h1>
            <p class="text-xl text-gray-600">Remove a user's ban and allow them to rejoin the server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?unban user_id [reason]
                    </div>
                    <p class="mb-4">The unban command allows moderators to remove a ban from a user, allowing them to rejoin the server with a new invite.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">user_id</code> - The ID of the user to unban</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional: Reason for the unban</li>
                        </ul>
                    </div>
                </section>

                <!-- Finding User ID Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Finding a User's ID</h2>
                    <p class="mb-4">To unban a user, you'll need their User ID. Here's how to find it:</p>
                    <ol class="list-decimal list-inside space-y-2 mb-4">
                        <li>Enable Developer Mode in Discord (User Settings > App Settings > Advanced > Developer Mode)</li>
                        <li>Check the server's ban list (Server Settings > Bans)</li>
                        <li>Right-click on the user and select "Copy ID"</li>
                    </ol>
                    <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4">
                        <p class="text-yellow-700">
                            <strong>Note:</strong> User IDs are long numbers, like "123456789012345678"
                        </p>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic unban:</p>
                            <pre class="bg-gray-50 rounded p-4">?unban 123456789012345678</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Unban with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?unban 123456789012345678 Appeal approved</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Unbanned</p>
                                    <p class="text-gray-600">Successfully unbanned User#1234 (123456789012345678)</p>
                                    <p class="text-gray-600">Reason: Appeal approved</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">Memo Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">User is not banned or ID is invalid.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Ban Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://Memo.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://Memo.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>You must use the user's ID, not their username</li>
                        <li>The action is logged in the server's audit log</li>
                        <li>Users must be re-invited after being unbanned</li>
                        <li>The command works even if the user has left the server</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\donate.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Support Development</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="Memo Bot | Support Development">
    <meta property="og:description" content="Support Memo Bot's development and get exclusive perks. Every donation helps keep the bot running and improving.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/donate">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        .donate-btn {
            transition: all 0.3s ease;
        }
        .donate-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        .tier-card {
            transition: transform 0.3s ease;
        }
        .tier-card:hover {
            transform: translateY(-5px);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Header Section -->
        <div class="text-center mb-16">
            <h1 class="text-5xl font-bold mb-4">Support Memo Bot</h1>
            <p class="text-xl text-gray-600 mb-8">Help keep Memo Bot running and improving</p>
            <a href="https://Memo.nerd-bear.org/donate/paypal" 
               target="_blank" 
               rel="noopener noreferrer" 
               class="donate-btn inline-block bg-blue-500 text-white font-bold py-4 px-8 rounded-full text-xl hover:bg-blue-600 transition">
                Donate with PayPal
            </a>
        </div>

        <!-- Why Donate Section -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold text-center mb-8">Why Support Us?</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <div class="text-4xl mb-4">🚀</div>
                    <h3 class="text-xl font-bold mb-2">Keep Memo Bot Running</h3>
                    <p class="text-gray-600">Your support helps cover hosting costs and ensures Memo Bot stays online 24/7.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <div class="text-4xl mb-4">⭐</div>
                    <h3 class="text-xl font-bold mb-2">Enable New Features</h3>
                    <p class="text-gray-600">Donations help us develop new features and improve existing ones.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <div class="text-4xl mb-4">💙</div>
                    <h3 class="text-xl font-bold mb-2">Support Development</h3>
                    <p class="text-gray-600">Show your appreciation and help motivate continued development.</p>
                </div>
            </div>
        </section>

        <!-- Donation Tiers -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold text-center mb-8">Donation Tiers</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Basic Tier -->
                <div class="tier-card bg-white rounded-lg shadow-md overflow-hidden">
                    <div class="p-6">
                        <h3 class="text-2xl font-bold mb-2">Basic Supporter</h3>
                        <div class="text-4xl font-bold text-blue-600 mb-4">$5</div>
                        <ul class="space-y-2 mb-6">
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                Supporter role in our Discord Server
                            </li>
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                Name in bot credits
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Premium Tier -->
                <div class="tier-card bg-white rounded-lg shadow-md overflow-hidden border-2 border-blue-500">
                    <div class="bg-blue-500 text-white text-center py-2">MOST POPULAR</div>
                    <div class="p-6">
                        <h3 class="text-2xl font-bold mb-2">Premium Supporter</h3>
                        <div class="text-4xl font-bold text-blue-600 mb-4">$10</div>
                        <ul class="space-y-2 mb-6">
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                All Basic benefits
                            </li>
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                Early access to features
                            </li>
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                Priority support
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Elite Tier -->
                <div class="tier-card bg-white rounded-lg shadow-md overflow-hidden">
                    <div class="p-6">
                        <h3 class="text-2xl font-bold mb-2">Elite Supporter</h3>
                        <div class="text-4xl font-bold text-blue-600 mb-4">$20</div>
                        <ul class="space-y-2 mb-6">
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                All Premium benefits
                            </li>
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                Custom role color
                            </li>
                            <li class="flex items-center">
                                <svg class="w-5 h-5 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                Feature request priority
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ Section -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold text-center mb-8">Frequently Asked Questions</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-2">How do I claim my rewards?</h3>
                    <p class="text-gray-600">After donating, join our Discord server and open a ticket. Provide your PayPal transaction ID, and we'll set up your rewards within 24 hours.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-2">Is my donation recurring?</h3>
                    <p class="text-gray-600">No, all donations are one-time payments. You can choose to donate again anytime you want to support us further.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-2">How long do rewards last?</h3>
                    <p class="text-gray-600">Rewards are permanent! Once you receive your perks, they'll stay with your account indefinitely.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-bold mb-2">Can I donate a custom amount?</h3>
                    <p class="text-gray-600">Yes! You can modify the donation amount on PayPal. You'll receive the tier rewards for the nearest tier below your donation amount.</p>
                </div>
            </div>
        </section>

        <!-- Final CTA -->
        <section class="text-center mb-16">
            <h2 class="text-3xl font-bold mb-4">Ready to Support Memo Bot?</h2>
            <p class="text-xl text-gray-600 mb-8">Your support helps keep Memo Bot free for everyone!</p>
            <a href="https://Memo.nerd-bear.org/donate/paypal" 
               target="_blank" 
               rel="noopener noreferrer" 
               class="donate-btn inline-block bg-blue-500 text-white font-bold py-4 px-8 rounded-full text-xl hover:bg-blue-600 transition">
                Support Development
            </a>
        </section>
    </main>

    <footer class="bg-gray-100 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# website\home.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo - Discord Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Home">
    <meta property="og:description" content="A versatile Discord bot for server management and user interaction. Features include moderation tools, customizable status, character info lookup, and message logging. Actively developed with frequent updates. Created by Nerd Bear for enhancing Discord communities.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6 items-center">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
                <li>
                    <a href="https://Memo.nerd-bear.org/donate" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full transition shadow-md">
                        Donate
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center">
            <a href="https://Memo.nerd-bear.org/" class="mb-8">
                <img src="https://Memo.nerd-bear.org/pfp-5.png" alt="Memo Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-5xl font-bold mb-4 text-gray-900"><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Welcome to Memo Bot</a></h2>
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
                <p class="text-gray-600">Tailor Memo to fit your server's unique needs.</p>
            </div>
        </div>
    </section>

    <div class="bg-blue-100 py-3 px-6 mt-12">
        <div class="container mx-auto text-center">
            <p class="text-blue-800">
                Recent changes to our <a href="https://Memo.nerd-bear.org/privacy-policy" class="font-semibold underline hover:text-blue-600 transition">Privacy Policy</a>. Please review.
            </p>
        </div>
    </div>

    <footer class="bg-gray-200 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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
        <title>Memo - Discord Bot | Privacy Policy</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

        <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

        <!-- Open Graph Meta Tags (for Discord and other platforms) -->
        <meta property="og:title" content="Memo Bot | Privacy Policy">
        <meta property="og:description" content="Privacy Policy for Memo Bot - Learn how we collect, use, and protect your data when you use our Discord bot.">
        <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
        <meta property="og:url" content="https://Memo.nerd-bear.org/privacy">
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
                    <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
                </h1>
                <ul class="flex space-x-6">
                    <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                    <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                    <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                    <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
                </ul>
            </div>
        </nav>

        <main class="container mx-auto mt-24 p-6">
            <div class="flex flex-col items-center mb-12">
                <a href="https://Memo.nerd-bear.org/" class="mb-8">
                    <img src="https://Memo.nerd-bear.org/pfp-5.png" alt="Memo Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
                </a>
                <h2 class="text-4xl font-bold mb-4 text-gray-900">
                    <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Privacy Policy</a>
                </h2>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h3 class="text-2xl font-bold mb-4 text-blue-600">1. Information We Collect</h3>
                <We class="mb-6">When you use Memo Bot, we may collect certain information such as your Discord user ID, server ID, message content when using bot commands, and other relevant data necessary for the bot's functionality. We also have a Database of all the commands that users ran, and the hashed user ID. This is needed when moderators of a guild want to check what commands a user ran.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">2. How We Use Your Information</h3>
                <p class="mb-6">We use the collected information to provide and improve Memo Bot's services, including command execution, server management, and user interaction. We do not sell or share your personal information with third parties.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">3. Data Storage and Security</h3>
                <p class="mb-6">We take reasonable measures to protect your data from unauthorized access or disclosure. However, no method of transmission over the internet or electronic storage is 100% secure.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">4. Your Rights</h3>
                <p class="mb-6">You have the right to access, correct, or delete your personal information. To exercise these rights, please contact us using the information provided in the "Contact Us" section.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">5. Changes to This Privacy Policy</h3>
                <p class="mb-6">We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">6. Compliance with Discord's Policies</h3>
                <p class="mb-6">Memo Bot complies with Discord's Developer Terms of Service and Developer Policy. We do not collect or use any data beyond what is necessary for the bot's functionality and what is allowed by Discord's policies.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">7. Children's Privacy</h3>
                <p class="mb-6">Memo Bot is not intended for use by children under the age of 13. We do not knowingly collect personal information from children under 13. If you are a parent or guardian and you are aware that your child has provided us with personal information,
                    please contact us.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">8. Contact Us</h3>
                <p>If you have any questions about this Privacy Policy, please contact us at Memo@nerd-bear.org.</p>
            </div>
        </main>

        <footer class="bg-gray-100 mt-24 py-8">
            <div class="container mx-auto text-center text-gray-600">
                <p>&copy; 2024 Memo Bot. All rights reserved.</p>
                <div class="mt-4">
                    <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                    <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                    <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
                </div>
            </div>
        </footer>
    </body>
</html>
```

# website\support.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo Bot - Support</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Support">
    <meta property="og:description" content="Get help with Memo Bot through our support articles or by contacting our support team.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/support">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://Memo.nerd-bear.org/" class="mb-8">
                <img src="https://Memo.nerd-bear.org/pfp-5.png" alt="Memo Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">Support Center</h2>
            <p class="text-xl text-gray-600 mb-8">Get help with Memo Bot</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
            <!-- Help Articles Section -->
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h3 class="text-2xl font-bold text-blue-600 mb-6">Help Articles</h3>
                <p class="text-gray-600 mb-6">Browse our collection of help articles to find answers to common questions:</p>
                <ul class="space-y-4">
                    <li>
                        <a href="https://Memo.nerd-bear.org/support/article/commands-guide" class="flex items-center text-blue-600 hover:text-blue-800">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                            Commands Guide
                        </a>
                    </li>
                    <li>
                        <a href="https://Memo.nerd-bear.org/support/article/config-guide" class="flex items-center text-blue-600 hover:text-blue-800">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                            Configuration Guide
                        </a>
                    </li>
                    <li>
                        <a href="https://Memo.nerd-bear.org/support/article/add-feedback" class="flex items-center text-blue-600 hover:text-blue-800">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                            How to Submit Feedback
                        </a>
                    </li>
                </ul>
                <a href="https://Memo.nerd-bear.org/articles" class="inline-block mt-6 text-blue-600 hover:text-blue-800">
                    View all articles →
                </a>
            </div>

            <!-- Contact Support Section -->
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h3 class="text-2xl font-bold text-blue-600 mb-6">Contact Support</h3>
                <p class="text-gray-600 mb-6">Can't find what you're looking for? Our support team is here to help!</p>
                
                <div class="space-y-4">
                    <div class="flex items-center">
                        <svg class="w-6 h-6 mr-3 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                        </svg>
                        <a href="mailto:support@nerd-bear.org" class="text-blue-600 hover:text-blue-800">support@nerd-bear.org</a>
                    </div>
                    
                    <p class="text-gray-600 mt-6">Response Time: Within 24 hours</p>
                </div>

                <div class="mt-8 p-4 bg-blue-50 rounded-md">
                    <p class="text-sm text-blue-800">
                        <strong>Tip:</strong> For faster support, please include your server ID and a detailed description of your issue in your email.
                    </p>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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

# website\terms-of-use.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memo - Discord Bot | Terms of Use</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Terms of Use">
    <meta property="og:description" content="Terms of Use for Memo Bot - A versatile Discord bot for server management and user interaction. Please read these terms carefully before using Memo Bot.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/terms">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://Memo.nerd-bear.org/" class="mb-8">
                <img src="https://Memo.nerd-bear.org/pfp-5.png" alt="Memo Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Terms of Use</a>
            </h2>
        </div>

        <div class="bg-white p-8 rounded-lg shadow-md">
            <h3 class="text-2xl font-bold mb-4 text-blue-600">1. Acceptance of Terms</h3>
            <p class="mb-6">By using Memo Bot, you agree to these Terms of Use. If you disagree with any part of these terms, please do not use our bot.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">2. Use of the Bot</h3>
            <p class="mb-6">Memo Bot is provided for Discord server management and entertainment purposes. You agree to use it only for its intended purposes and in compliance with Discord's Terms of Service.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">3. User Responsibilities</h3>
            <p class="mb-6">You are responsible for all activities that occur under your Discord account while using Memo Bot. Do not use the bot for any illegal or unauthorized purpose.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">4. Modifications to Bot or Terms</h3>
            <p class="mb-6">We reserve the right to modify or discontinue Memo Bot at any time. We may also revise these Terms of Use at our discretion. Continued use of the bot after any changes constitutes acceptance of those changes.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">5. Limitation of Liability</h3>
            <p class="mb-6">Memo Bot is provided "as is" without warranties of any kind. We are not liable for any damages or losses related to your use of the bot.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">6. Privacy</h3>
            <p class="mb-6">Our use and collection of your information is governed by our Privacy Policy. By using Memo Bot, you consent to our data practices as described in that policy.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">7. Termination</h3>
            <p class="mb-6">We may terminate or suspend your access to Memo Bot immediately, without prior notice, for conduct that we believe violates these Terms of Use or is harmful to other users of the bot, us, or third parties, or for any other reason.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">8. Governing Law</h3>
            <p class="mb-6">These Terms shall be governed by and construed in accordance with the laws of United States of America and the United Kingdom, without regard to its conflict of law provisions.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">9. Contact Us</h3>
            <p>If you have any questions about these Terms, please contact us at Memo@nerd-bear.org.</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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
    <title>Memo Bot - Version History</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="Memo Bot | Version History">
    <meta property="og:description" content="Explore the version history of Memo Bot, a versatile Discord bot for server management and user interaction. See the latest updates, features, and improvements.">
    <meta property="og:image" content="https://Memo.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://Memo.nerd-bear.org/versions">
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
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-800 transition">Memo Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://Memo.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://Memo.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://Memo.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://Memo.nerd-bear.org/" class="mb-8">
                <img src="https://Memo.nerd-bear.org/pfp-5.png" alt="Memo Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">
                <a href="https://Memo.nerd-bear.org/" class="hover:text-blue-600 transition">Memo Bot Version History</a>
            </h2>
        </div>
        
        <div class="mb-8">
            <input type="text" id="search-input" placeholder="Search versions..." class="w-full p-2 border border-gray-300 rounded-md">
        </div>

        <div class="mb-8" id="toc">
            <h3 class="text-2xl font-bold mb-4">Table of Contents</h3>
            <ul class="space-y-2">
                <li><a href="#v0-4-4" class="text-blue-600 hover:underline">Memo 0.4.4 Beta pre-release</a></li>
                <li><a href="#v0-4-3" class="text-blue-600 hover:underline">Memo 0.4.3 Beta pre-release</a></li>
                <li><a href="#v0-4-2" class="text-blue-600 hover:underline">Memo 0.4.2 Beta pre-release</a></li>
                <li><a href="#v0-4-1" class="text-blue-600 hover:underline">Memo 0.4.1 Beta pre-release</a></li>
            </ul>
        </div>
        
        <div class="space-y-12" id="versions-container">
            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-4">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">Memo 0.4.4 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.04 MB (~43.1 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 05/10/2024 2:45 AM BST</p>
                <a href="https://github.com/nerd-bear/Memo/releases/tag/0.4.4" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.4</a>
                
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
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of Memo is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-3">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">Memo 0.4.3 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.03 MB (~30.8 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 04/10/2024 2:17 AM BST</p>
                <a href="https://github.com/nerd-bear/Memo/releases/tag/0.4.3" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.3</a>
                
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
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of Memo is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-2">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">Memo 0.4.2 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.02 MB (~18.3 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 03/10/2024 3:39 AM BST</p>
                <a href="https://github.com/nerd-bear/Memo/releases/tag/0.4.2" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.2</a>
                
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
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of Memo is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-1">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">Memo 0.4.1 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.02 MB (~18.3 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 02/10/2024 4:09 AM BST</p>
                <a href="https://github.com/nerd-bear/Memo/releases/tag/0.4.1" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.1</a>
                
                <p class="mb-4">This is a simple beta testing release with around 10 simple commands, the commands are: help, charinfo, kick, ban, shutdown, start, stream, play, watch and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behaviour, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>May include hard-coded paths to files that may not exist or path formats meant for another OS</li>
                    <li>More unknown issues may exist</li>
                </ul>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of Memo is open source and under the apache2 license)</p>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 Memo Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://Memo.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://Memo.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://Memo.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
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

