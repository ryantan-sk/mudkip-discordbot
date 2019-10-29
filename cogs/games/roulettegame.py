from discord.ext import commands

import discord
import random
import math


class RussianRoulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.game_instance = False
        self.player_list = []
        self.bullet = []
        self.chambers = 0
        self.member_turn = 0

    @commands.command(name="FFA", ignore_extra=True)
    async def start_game(self, ctx, *members: discord.Member):
        channel = ctx.channel
        member_list = []
        if self.game_instance:
            await channel.send("An FFA game is currently in session.")
        else:
            self.game_instance = True

            for member in members:
                if str(member.status) is not "online":
                    await channel.send(f"{member.mention} is unavailable. I can't start an RR game if you're offline "
                                       f"dude.")
                    self.game_instance = False
                    break

                else:
                    self.player_list.append(member.id)
                    member_list.append(member)

            num_bullet = math.floor(len(self.player_list) // 2)
            self.chambers = (len(self.player_list) * 2) + 2

            for i in range(0, num_bullet):
                bullet_number = random.randint(1, self.chambers)
                self.bullet.append(bullet_number)

            member_string = "\n".join(member_list)
            await channel.send(
                f"The following players started a game of Russian Roulette:"
                f"{member_string}"
            )

    @commands.command(name="roll")
    async def _roll(self, ctx):
        channel = ctx.channel
        author = ctx.author

        if not self.game_instance:
            await channel.send("No game in session right now.")

        else:
            current_player_id = self.player_list[self.member_turn]

            if current_player_id != author.id:
                await channel.send(f"Hey, {ctx.author.mention}! It is not your turn right now. "
                                   f"Don't be in a hurry to get kicked.")

            else:
                shot = random.randint(1, len(self.chambers))

                if shot in self.bullet:
                    self.game_instance = False
                    self.bullet = []
                    self.player_list = []
                    self.member_turn = 0
                    self.chambers = 0

                    await channel.send(f"{author.mention} bit the dust")
                    try:
                        await author.kick()
                    except PermissionError:
                        await channel.send(f"But {author.mention} is too strong! He's immortal!")

                else:
                    await channel.send(f"Phew! {author.mention} lives to see another day.")
                    self.member_turn += 1
