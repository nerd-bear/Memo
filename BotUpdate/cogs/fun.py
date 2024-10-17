import discord
from discord.ext import commands
from utils.config_manager import ColorManager, load_config
from utils.db_manager import add_history
from utils.helper import get_char_image
import unicodedata
import os

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.color_manager = ColorManager(self.config)

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):
        add_history(ctx.author.id, "charinfo", [characters])
        if len(characters) > 1:
            await ctx.send("Please provide only one character for information.")
            return

        char = characters[0]
        unicode_value = ord(char)
        char_name = unicodedata.name(char, "Could not find name!")
        char_category = unicodedata.category(char)

        unicode_escape = f"\\u{unicode_value:04x}"
        unicode_escape_full = f"\\U{unicode_value:08x}"
        python_escape = repr(char)

        embed = discord.Embed(
            color=self.color_manager.get_color("Blue"),
            title="Character info",
            description=f"Information on character: {char}"
        )

        embed.add_field(name="Original character", value=char, inline=True)
        embed.add_field(name="Character name", value=char_name, inline=True)
        embed.add_field(name="Character category", value=char_category, inline=True)
        embed.add_field(name="Unicode value", value=f"U+{unicode_value:04X}", inline=True)
        embed.add_field(name="Unicode escape", value=unicode_escape, inline=True)
        embed.add_field(name="Full Unicode escape", value=unicode_escape_full, inline=True)
        embed.add_field(name="Python escape", value=python_escape, inline=True)

        embed.set_footer(
            text=self.config["defaults"]["footer_text"],
            icon_url=self.config["defaults"]["footer_icon"]
        )

        image_path = get_char_image(char)

        if image_path:
            file = discord.File(image_path, filename="character.png")
            embed.set_thumbnail(url="attachment://character.png")
            await ctx.send(embed=embed, file=file)
            os.remove(image_path)
        else:
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))