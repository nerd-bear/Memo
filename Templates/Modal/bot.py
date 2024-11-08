import disnake
from disnake.ext import commands
from disnake import TextInputStyle

TOKEN = "your_token"

BOT = commands.Bot(command_prefix='!', intents=disnake.Intents.all())

@BOT.event
async def on_ready():
    print(f"Logged in as {BOT.user.name}")
    print("Bot is ready!")
    print(f"Connected to {len(BOT.guilds)} servers")
    await BOT.change_presence(activity=disnake.Game(name="with your friends"))


class TextModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Email Address",
                style=TextInputStyle.short,
                custom_id="Email",
                required=True,
            ),
            disnake.ui.TextInput(
                label="Message",
                style=TextInputStyle.long,
                placeholder="Type your message here",
                custom_id="Message",
            ),
        ]
        super().__init__(title="Text Modal", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        embed = disnake.Embed(
            title="Modal Interaction",
        )
        for key, value in interaction.text_values.items():
            embed.add_field(name=key.capitalize(), value=value[:1000], inline=False)

        await interaction.response.send_message(embed=embed)


@BOT.slash_command(
    name="modal",
    description="Basic Test Modal",
)
async def ping(inter: disnake.AppCmdInter):
    await inter.response.send_modal(modal=TextModal())
    return


BOT.run(TOKEN)