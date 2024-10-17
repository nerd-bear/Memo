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