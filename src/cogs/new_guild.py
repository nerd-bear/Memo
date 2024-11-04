import disnake
from disnake.ext import commands

class GuildJoinEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: disnake.Guild):
        channel = None
        for guild_channel in guild.text_channels:
            if guild_channel.permissions_for(guild.me).send_messages:
                channel = guild_channel
                break

        if not channel:
            print(f"No channel found to send join message in {guild.name}")
            return

        embed = disnake.Embed(
            color=0xb3e2eb,
            title="Thanks for adding Memo to your server!",
            description="Use `?help` to see all the commands! \n\n"
                        "**If you have any other questions or need help, join our support server**\n\n"
                        "Any further information can be found at https://memo.nerd-bear.org/\n\n"
                        "Report any bugs or suggestions using `?feedback`"
        )

        button = disnake.ui.Button(
            style=disnake.ButtonStyle.link,
            label="Visit Website",
            url="https://memo.nerd-bear.org/"
        )

        action_row = disnake.ui.ActionRow(button)

        await channel.send(content="https://discord.gg/vaUkpsfa4b")
        await channel.send(embed=embed, components=[action_row])

def setup(bot):
    bot.add_cog(GuildJoinEvents(bot))