from discord.ext import commands
from cogs.utils import path_finder

import discord
import random
import json


# noinspection SpellCheckingInspection


class PokeGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game_instance = False
        self.question_paths = path_finder.file_paths("cogs\\library\\games-files\\pokegame\\pokegame_questions")
        self.answer_paths = path_finder.file_paths("cogs\\library\\games-files\\pokegame\\pokegame_answers")
        self.pokedex = get_pokedex()
        self.identity = 0

    @commands.command(name="pokegame")
    async def pokegame_start(self, ctx):
        if not self.game_instance:
            self.game_instance = True
            i = random.randint(0, len(self.question_paths) - 1)

            self.identity = i
            await ctx.send("Who's that pokemon?"
                            "\n!guess to guess the pokemon"
                            "\n!repeat to repeat the question", file=discord.File(self.question_paths[i]))

        else:
            await ctx.send("Game is currently in session. Please wait for the next round.")

    @commands.command(name="repeat")
    async def pokegame_repeat(self, ctx):
        if self.game_instance:
            question = discord.File(self.question_paths[self.identity])
            await ctx.send("Who's that pokemon?"
                                   "\n!guess to guess the pokemon"
                                   "\n!repeat to repeat the question", file=question)
        else:
            await ctx.send("There is no on-going game session right now.")

    @commands.command(name="guess")
    async def pokegame_guess(self, ctx, message):
        answer_lower = message.lower()
        if self.game_instance:
            pokedex_number = path_finder.file_name(self.answer_paths[self.identity])
            answer = self.pokedex[pokedex_number]

            answer_file = discord.File(self.answer_paths[self.identity])

            if answer_lower == answer:
                self.game_instance = False
                await ctx.send(f"Congratulations {ctx.author.mention}! It was {answer.title()}",
                                   file=answer_file)
        else:
            pass


def get_pokedex():
    with open("cogs\\library\\games-files\\pokegame\\pokedex.json") as file:
        pokedex = json.load(file)
    return pokedex


def setup(bot):
    bot.add_cog(PokeGame(bot))
