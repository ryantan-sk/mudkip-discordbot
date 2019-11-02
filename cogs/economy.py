from discord.ext import commands

import discord
import json


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.path = ""

    def withdraw(self, member, amount):
        with open(self.path) as file:
            data = json.load(file)

        member_id = str(member.id)
        current_amount = float(data[member_id])
        data["member_id"] = str(current_amount - amount)

        with open(self.path) as file:
            json.dump(data, file, indent=2, sort_keys=True)

    def deposit(self, member, amount):
        with open(self.path) as file:
            data = json.load(file)

        member_id = str(member.id)
        current_amount = float(data[member_id])
        data["member_id"] = str(current_amount + amount)

        with open(self.path) as file:
            json.dump(data, file, indent=2, sort_keys=True)

    def new_user(self, member: discord.User.id):
        with open(self.path) as file:
            data = json.load(file)

        if member in data:
            pass

        else:
            data[member] = "1000"
            with open(self.path) as file:
                json.dump(data, file, indent=2, sort_keys=True)

    @commands.command(name="balance")
    async def _balance(self, ctx ):
        channel = ctx.channel
        author = ctx.author

        with open(self.path) as file:
            data = json.load(file)

        member_id = str(author.id)
        current_amount = data[member_id]

        await channel.send(f"{author.mention}, your balance is ${current_amount}")


def setup(bot):
    bot.add_cog(Economy(bot))