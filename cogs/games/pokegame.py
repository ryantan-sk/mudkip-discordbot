from discord.ext import commands
from cogs.utils import path_finder
from cogs.utils import pokedex

import discord
import random


class PokeGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game_instance = False
        self.question_paths = path_finder.file_paths("images\\pokegame_questions")
        self.answer_paths = path_finder.file_paths("images\\pokegame_answers")

        self.identity = 0

    @commands.command(name="pokegame")
    async def pokegame_start(self, ctx):
        if not self.game_instance:
            self.game_instance = True
            i = random.randint(0, len(self.question_paths))

            self.identity = i
            await ctx.channel.send("Who's that pokemon?", file=discord.File(self.question_paths[i]))

        else:
            await ctx.channel.send("Game is currently in session. Please wait for the next round.")

    @commands.command(name="repeat")
    async def pokegame_repeat(self, ctx):
        if self.game_instance:
            question = discord.File(self.question_paths[self.identity])
            await ctx.channel.send("Who's that pokemon?", file=question)
        else:
            await ctx.channel.send("There is no on-going game session right now.")

    @commands.command(name="guess")
    async def pokegame_guess(self, ctx, message):
        channel = ctx.channel
        answer_lower = message.lower()
        if self.game_instance:
            pokedex_number = path_finder.file_name(self.answer_paths[self.identity])
            answer = pokedex.pokedex_dict[pokedex_number]
            answer_file = discord.File(self.answer_paths[self.identity])

            if answer_lower == answer:
                self.game_instance = False
                await channel.send(f"Congratulations {ctx.author.mention}! It was {answer.title()}",
                                   file = answer_file)

            else:
                await channel.send(f"Wrong answer! {ctx.author.mention} is a noob.")

        else:
            await channel.send("There is no on-going game session right now.")