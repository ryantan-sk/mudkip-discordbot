from discord.ext import commands

TOKEN = 'Enter your bot token here'


def get_prefix(bot, message):
    bot_id = bot.user.id
    prefix = [f"<@{bot_id}> ", "!"]
    return prefix


bot = commands.Bot(command_prefix=get_prefix)

cogs = (
    "cogs.general",
    "cogs.moderator",
    "cogs.memes-text-based",
    "cogs.memes-image-based",
    "cogs.games-pokemon-guess",
    "cogs.games-tictactoe",
    "cogs.economy",
    "cogs.error_handler"
)

if __name__ == '__main__':
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as error:
            print(f'{cog} failed to load. Error occurred: {error}')

    bot.run(TOKEN)
