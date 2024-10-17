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