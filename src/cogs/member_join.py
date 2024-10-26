import disnake
import datetime
from disnake.ext import commands

class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        channel = member.guild.text_channels[0]

        if not channel:
            return

        embed = disnake.Embed(
            title="Welcome to the server!",
            description=f"Hey there {member.mention} are welcome to the guild!",
            color=disnake.Color.green(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.add_field(
            name="Account Created At", 
            value=f"<t:{int(member.created_at.timestamp())}:F>"
        )
        embed.set_thumbnail(url=member.avatar.url)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(MemberEvents(bot))