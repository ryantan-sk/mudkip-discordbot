from discord.ext import commands
from cogs.utils import path_finder

import discord
import random



class ImageBasedMemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cost = 100

    @commands.command(name="doge")
    async def _doge(self, ctx):
        economy = self.bot.get_cog("Economy")
        author = ctx.author

        if economy.get_balance(author) > 0:
            await economy.withdraw(author, self.cost)
            all_path = path_finder.file_paths("cogs\\library\\memes\\image-memes\\doge")
            doge = random.choice(all_path)
            await ctx.send(file=discord.File(doge))
        else:
            await ctx.send(f"{author.mention}, you have insufficient funds.")

    @commands.command(name="pokememe")
    async def _pokememe(self, ctx):
        economy = self.bot.get_cog("Economy")
        author = ctx.author

        if economy.get_balance(author) > 0:
            await economy.withdraw(author, self.cost)
            all_path = path_finder.file_paths("cogs\\library\\memes\\image-memes\\pokememe")
            pokememe = random.choice(all_path)
            await ctx.send(file=discord.File(pokememe))
        else:
            await ctx.send(f"{author.mention}, you have insufficient funds.")


def setup(bot):
    bot.add_cog(ImageBasedMemes(bot))