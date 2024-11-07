import disnake
import datetime
from disnake.ext import commands

class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        channel = None
        for guild_channel in member.guild.text_channels:
            if guild_channel.permissions_for(member.guild.me).send_messages:
                channel = guild_channel
                break

        if not channel:
            print(f"No channel found to send join message for {member.name} in {member.guild.name}")
            return

        embed = disnake.Embed(
            title="Welcome to the server!",
            description=f"Hey there {member.mention} and welcome to the guild!",
            color=disnake.Color.green(),
            timestamp=datetime.datetime.utcnow(),
        )

        embed.add_field(
            name="Account Created At",
            value=f"<t:{int(member.created_at.timestamp())}:F>",
        )

        embed.add_field(
            name="Member number",
            value=f"You are the {member.guild.member_count}th member",
            inline=False,
        )

        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)

        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(MemberEvents(bot))