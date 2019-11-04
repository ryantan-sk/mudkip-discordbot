from discord.ext import commands

import discord


class GeneralFunctions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot ready.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'''Greetings {member.name}. Welcome to the Bot Test Server!
    I am Mudkip, an evil minion.!
    Congratulations! You have been assigned the role of peasant!'''
        )

        welcome = f"Welcoming our new peasant, {member.mention}! \U0001F60E"
        channel = discord.utils.get(member.guild.channels, name="general")
        await channel.send(welcome)

        newcomer_role = discord.utils.get(member.guild.roles, name='Peasant')
        await member.add_roles(newcomer_role)

        economy = self.bot.get_cog("Economy")
        await economy.new_user(member)

    @commands.command()
    async def load(self, cog):
        try:
            self.bot.load_extension(cog)
            print(f'Loaded {cog}')
        except Exception as error:
            print(f'{cog} failed to load. Error occurred: {error}')

    @commands.command()
    async def unload(self, cog):
        try:
            self.bot.unload_extension(cog)
            print(f'Unloaded {cog}')
        except Exception as error:
            print(f'{cog} failed to unload. Error occurred: {error}')


def setup(bot):
    bot.add_cog(GeneralFunctions(bot))
