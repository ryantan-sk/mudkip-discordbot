import discord
import random

from discord.ext import commands
from cogs.games.pokegame import PokeGame
from cogs.games.roulettegame import RussianRoulette

TOKEN = 'NjM2MDczMjY2NzI0ODY0MDE1.Xa6UVA.wE-VZTMkYZV075oK2lO0ritu4BY'

bot = commands.Bot(command_prefix="!", self_bot=False)



@bot.command()
async def inspire(message):
    channel = message.channel
    await channel.send(
        f"@{message.author.name}, you are stronger than you think."
    )


@bot.command()
async def lenny(ctx):
    lenny = (
        "( ͡° ͜ʖ ͡°)",
        "(☭ ͜ʖ ☭)",
        "(ᴗ ͜ʖ ᴗ)",
        "'¯\\_( ͡° ͜ʖ ͡°)_/¯",
        '(ノಠ益ಠ)ノ彡┻━┻',
        " ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿  ",
        "┬──┬ ノ( ゜-゜ノ)",
        "(｡◕‿◕｡)",
        "ヾ(⌐■_■)ノ♪",
        "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)",
        "༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽",
        "☜(˚▽˚)☞",
        "(ง°ل͜°)ง }",
    )

    await ctx.channel.send(random.choice(lenny))

@bot.command(name='roast')
async def _roast(ctx, member: discord.Member):
    roasts = (
f'''
Hey {member.mention}, yo mama so old, when I told her to act her age, she died. \U0001F60E 
''',

f'''
Hey {member.mention}, yo mama so fat, Thanos had to CLAP! \U0001F44F \U0001F44F \U0001F44F
''',

f'''
Hey {member.mention}, yo mama so fat, she takes selfies with a satellite. \U0001F4E1
''')

    await ctx.channel.send(random.choice(roasts))


@bot.command(name="test")
async def _test(ctx):
    channel = ctx.channel
    await channel.send(file=discord.File("images\pokememe\meme_1.png"))

tester = PokeGame(bot)
bot.add_cog(tester)

RR = RussianRoulette(bot)
bot.add_cog(RR)


bot.run(TOKEN)
