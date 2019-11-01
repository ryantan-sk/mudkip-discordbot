from cogs.utils import path_finder
from discord.ext import commands
from cogs.memes.text import lenny

import json
import random


class TextBasedMemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.all_paths = path_finder.file_paths("cogs\\memes\\text")

    @commands.command(name="inspire")
    async def _inspire(self, ctx):
        channel = ctx.channel

        quote = load_meme(self.all_paths, 0)
        await channel.send(f"{quote}")

    @commands.command(name="lenny")
    async def _lenny(self, ctx):
        channel = ctx.channel

        lenny_choice = random.choice(lenny.lenny_emojis)
        await channel.send(f"{lenny_choice}")

    @commands.command(name="pun")
    async def _joke(self, ctx):
        channel = ctx.channel

        joke = load_meme(self.all_paths, 2)
        await channel.send(f"{joke}")


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






