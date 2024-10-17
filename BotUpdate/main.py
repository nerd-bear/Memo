import os
import discord
from discord.ext import commands
import json
import logging
from utils.config_manager import load_config

intents = discord.Intents.all()
config = load_config()

bot = commands.Bot(command_prefix=config['defaults']['prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded cog: {filename[:-3]}')
            except Exception as e:
                print(f'Failed to load cog {filename[:-3]}: {str(e)}')

async def main():
    logging.basicConfig(filename='logs/bot.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    
    await load_cogs()
    await bot.start(config['token'])

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())