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