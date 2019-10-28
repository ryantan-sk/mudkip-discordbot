import json
import discord
import random

from discord.ext import commands
from utils.colour import ColourCode
from pokegame import PokeGame

TOKEN = 'NjM2MDczMjY2NzI0ODY0MDE1.Xa6UVA.wE-VZTMkYZV075oK2lO0ritu4BY'

bot = commands.Bot(command_prefix="!", self_bot=False)


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'''Greetings {member.name}. Welcome to the Bot Test Server!
I am Mudkip! An evil minion.!
Congratulations! You have been assigned the role of peasant!'''
    )

    welcome = f"Welcoming our new peasant, {member.mention}! \U0001F60E"
    channel = discord.utils.get(member.guild.channels, name="general")
    await channel.send(welcome)

    with open("database.json", "r") as file:
        data = json.load(file)

    newcomer_role = discord.utils.get(member.guild.roles, name=data['newcomer'])
    await member.add_roles(newcomer_role)


@bot.command(name='role')
async def role(ctx, name, color):
    colour_code = ColourCode(color)
    colour_value = discord.Colour(colour_code)

    perms = discord.Permissions.none()
    perms.update(read_message=True,
                 send_message=True,
                 attach_files=True,
                 speak=True)

    await ctx.guild.create_role(name=name, colour=colour_value, permissions=perms, hoist=True)


@bot.command(name='mod')
async def mod(ctx, member: discord.Member, reason=None):
    mod_role = discord.utils.get(member.guild.roles, name="Secret Service")
    await member.add_roles(mod_role, reason=reason)


@bot.command(name='kick')
async def _kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@bot.command(name='ban')
async def _ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)





@bot.command(name='mute')
async def mute(ctx, member: discord.Member, *, reason=None):
    all_role = member.roles
    for i in range(1, len(all_role)):
        await member.remove_roles(all_role[i])


@bot.command(name='unmute')
async def _unmute(ctx, member: discord.Member, *, reason=None):
    newcomer = discord.utils.get(ctx.guild.roles, name='Peasant')
    await member.add_roles(newcomer, reason=reason)

# ==================================================================


@bot.command()
async def inspire(message):
    channel = message.channel
    await channel.send(
        f"@{message.author.name}, you are stronger than you think."
    )


@bot.command()
async def dice(ctx):
    channel = ctx.channel
    roll = random.randint(1, 6)
    await channel.send(
        f"{ctx.author.name} rolled a {roll}"
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


bot.run(TOKEN)
