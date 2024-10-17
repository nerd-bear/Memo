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