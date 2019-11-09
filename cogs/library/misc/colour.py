import discord

def ColourCode(colour):
    code = {
        "teal": discord.Color.teal(),
        "dark_teal": discord.Color.dark_teal(),
        "green": discord.Color.green(),
        "dark_green": discord.Color.dark_green(),
        "blue": discord.Color.blue(),
        "dark_blue": discord.Color.dark_blue(),
        "purple": discord.Color.purple(),
        "dark_purple": discord.Color.dark_purple(),
        "magneta": discord.Color.magenta(),
        "dark_magneta": discord.Color.dark_magenta(),
        "gold": discord.Color.gold(),
        "dark_gold": discord.Color.dark_gold(),
        "orange": discord.Color.orange(),
        "dark_orange": discord.Color.dark_orange(),
        "red": discord.Color.red(),
        "dark_red": discord.Color.dark_red(),
        "lighter_grey": discord.Color.lighter_grey(),
        "dark_grey": discord.Color.dark_grey(),
        "blurple": discord.Color.blurple(),
        "greyple": discord.Color.greyple()
    }
    return code[f'{colour}']
