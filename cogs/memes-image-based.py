from discord.ext import commands
from cogs.utils import path_finder

import discord
import random


class ImageBasedMemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="doge")
    async def _doge(self, ctx):
        all_path = path_finder.file_paths("cogs\\memes\\image-memes\\doge")
        channel = ctx.channel

        doge = random.choice(all_path)
        await channel.send(file=discord.File(doge))

    @commands.command(name="pokememe")
    async def _pokememe(self, ctx):
        all_path = path_finder.file_paths("cogs\\memes\\image-memes\\pokememe")
        channel = ctx.channel

        pokememe = random.choice(all_path)
        await channel.send(file=discord.File(pokememe))


def setup(bot):
    bot.add_cog(ImageBasedMemes(bot))