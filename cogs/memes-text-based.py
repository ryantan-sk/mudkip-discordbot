from cogs.utils import path_finder
from discord.ext import commands
from cogs.library.memes.text import lenny

import json
import random


class TextBasedMemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.all_paths = path_finder.file_paths("cogs\\library\\memes\\text")
        self.cost = 100

    @commands.command(name="inspire")
    async def _inspire(self, ctx):
        economy = self.bot.get_cog("Economy")
        author = ctx.author

        if economy.get_balance(author) > 0:
            await economy.withdraw(author, self.cost)
            quote = load_meme(self.all_paths, 0)
            await ctx.send(f"{quote}")
        else:
            await ctx.send(f"{author.mention} you have insufficient funds.")

    @commands.command(name="lenny")
    async def _lenny(self, ctx):
        economy = self.bot.get_cog("Economy")
        author = ctx.author

        if economy.get_balance(author) > 0:
            await economy.withdraw(author, self.cost)
            lenny_choice = random.choice(lenny.lenny_emojis)
            await ctx.send(f"{lenny_choice}")
        else:
            await ctx.send(f"{author.mention} you have insufficient funds.")

    @commands.command(name="pun")
    async def _pun(self, ctx):
        economy = self.bot.get_cog("Economy")
        author = ctx.author

        if economy.get_balance(author) > 0:
            await economy.withdraw(author, self.cost)
            pun = load_meme(self.all_paths, 2)
            await ctx.send(f"{pun}")
        else:
            await ctx.send(f"{author.mention} you have insufficient funds.")


def load_meme(path_list, meme_type):
    with open(path_list[meme_type], 'r') as file:
        meme_list = json.load(file)

    choice = str(random.randint(1, len(meme_list)))
    meme_lines = []

    for i in meme_list[choice]:
        meme_lines.append(meme_list[choice][i])

    meme = "\n".join(meme_lines)
    return meme


def setup(bot):
    bot.add_cog(TextBasedMemes(bot))






