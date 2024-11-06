import disnake
from disnake.ext import commands

TOKEN = "your_token"

WALLE2 = commands.Bot(command_prefix='!', intents=disnake.Intents.all())

@WALLE2.event
async def on_ready():
    print(f"Logged in as {WALLE2.user.name}")
    print("Bot is ready!")
    print(f"Connected to {len(WALLE2.guilds)} servers")
    await WALLE2.change_presence(activity=disnake.Game(name="with your friends"))

@WALLE2.slash_command(
    name="ping",
    description="Check if WALLE2 is alive",
)
async def ping(ctx):
    await ctx.send(f"Pong! {round(WALLE2.latency * 1000)}ms")

WALLE2.run(TOKEN)