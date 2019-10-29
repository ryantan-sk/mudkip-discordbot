from discord.ext import commands
from cogs.utils import path_finder

import discord
import random


class TextBasedMemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.all_paths = path_finder.file_paths("library\\text")

    #Mudkip tells a dark joke or story
    @commands.command(name="dark")
    async def _dark(self, ctx):
        with open( self.all_paths[0], 'r') as file:
            dark_list = file.readlines()

        joke = random.choice(dark_list)
        await ctx.channel.send(f"{ctx.author.mention} here'"
                               f"{joke}")


    #Mudkip sends an inspirational message
    @commands.command(name="inspire")


    # Mudkip sends a lenny
    @commands.command(name="lenny")




    #Mudkip tells a your mama joke
    @commands.command(name="mama")

    #Mudkip tells a roast joke
    @commands.command(name="roast")

