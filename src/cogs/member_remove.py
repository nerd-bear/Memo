import disnake
import datetime
from disnake.ext import commands


class MemberLeaveEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: disnake.Member):
        for guild_channel in member.guild.text_channels:
            if guild_channel.permissions_for(member.guild.me).send_messages:
                channel = guild_channel
                break

        if not channel:
            return

        embed = disnake.Embed(
            title="Goodbye!",
            description=f"Sad to see you leave... {member.mention}!",
            color=disnake.Color.red(),
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_thumbnail(url=member.avatar.url) 
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MemberLeaveEvents(bot))
