import disnake
from disnake.ext import commands

TOKEN = "your_token"

BOT = commands.Bot(command_prefix="!", intents=disnake.Intents.all())


@BOT.event
async def on_ready():
    print(f"Logged in as {BOT.user.name}")
    print("Bot is ready!")
    print(f"Connected to {len(BOT.guilds)} servers")
    await BOT.change_presence(activity=disnake.Game(name="with your friends"))


@BOT.slash_command(
    name="embed",
    description="Send a basic embed",
)
async def embed_command(ctx):
    embed = disnake.Embed(
        title="Embed Example",
        description="This is an example of an embed",
        color=0x00FF00,
    )
    embed.add_field(name="Field 1", value="This is field 1", inline=False)
    embed.add_field(name="Field 2", value="This is field 2", inline=True)
    await ctx.send(embed=embed)


BOT.run(TOKEN)
