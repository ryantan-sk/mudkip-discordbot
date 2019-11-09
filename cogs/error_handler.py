from discord.ext import commands

import traceback
import sys


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Passes on any errors that are being handled locally in their respective cogs
        if hasattr(ctx.command, 'on_error'):
            return

        # Tuple ignoring wrong user input or unknown commands
        ignored = (commands.UserInputError, commands.CommandNotFound)
        permission = (commands.MissingAnyRole, commands.MissingPermissions, commands.MissingRole)

        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, permission):
            return await ctx.send(f"You do not have the right role/sufficient permission to invoke this command.")

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} has been temporarily disabled. Please notify admin.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} does not support private messages')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            return await ctx.send(f'Argument you have entered into {ctx.command} is most likely invalid.')

        elif isinstance(error, commands.TooManyArguments):
            return await ctx.send(f"Too many arguments for {ctx.command}")

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))