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