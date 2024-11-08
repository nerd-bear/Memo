import disnake
from disnake.ext import commands

TOKEN = "your_token"

BOT = commands.Bot(command_prefix='!', intents=disnake.Intents.all())

@BOT.event
async def on_ready():
    print(f"Logged in as {BOT.user.name}")
    print("Bot is ready!")
    print(f"Connected to {len(BOT.guilds)} servers")
    await BOT.change_presence(activity=disnake.Game(name="with your friends"))

@BOT.event
async def on_message(message):
    message.channel.send(f"Username: {BOT.user.name}\nMessage: {message.content}")

BOT.run(TOKEN)