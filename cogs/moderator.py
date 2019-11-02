from discord.ext import commands
from cogs.library.misc.colour import ColourCode

import discord


class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='role')      #Creates a simple general role for the guild
    async def _role(self, ctx, name, color):
        colour_code = ColourCode(color)
        colour_value = discord.Colour(colour_code)

        perms = discord.Permissions.none()
        perms.update(read_message=True,
                     send_message=True,
                     attach_files=True,
                     speak=True)

        await ctx.guild.create_role(name=name, colour=colour_value, permissions=perms, hoist=True)

    @commands.command(name='mod')
    async def _mod(self, ctx, member:discord.Member, reason=None):
        mod_role = discord.utils.get(member.guild.roles, name="Secret Service")
        await member.add_roles(mod_role, reason=reason)

    @commands.command(name='kick')
    async def _kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command(name='ban')
    async def _ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command(name='mute')
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        all_role = member.roles
        for i in range(1, len(all_role)):
            await member.remove_roles(all_role[i], reason=reason)

    @commands.command(name='unmute')
    async def _unmute(self, ctx, member: discord.Member, *, reason=None):
        newcomer = discord.utils.get(ctx.guild.roles, name='Peasant')
        await member.add_roles(newcomer, reason=reason)


def setup(bot):
    bot.add_cog(ModCommands(bot))