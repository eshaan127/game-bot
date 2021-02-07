# Created by Eshaan Kumar on 9/22/2020
# Last updated 9/22/2020 by Eshaan Kumar

# Import modules
import discord
from discord.ext import commands
import asyncio
import random
import os

# Set prefix
client = commands.Bot(command_prefix = 'g ')

# Set g help as game played by bot
@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name='g help'))

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

# Error message
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'''Error: {error}
Fix: Try the command "g help" to see possible commands''')

# Help command
# Remove original help command
client.remove_command('help')
# Add new help command
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed.set_author(name='Help: list of commands available')
    embed.add_field(name='g ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name='g info', value='Shows bot information', inline=False)
    embed.add_field(name='g quote', value='Returns a random quote, if u want a quote in this command DM an admin', inline=False)
    embed.add_field(name='g joke', value='Returns a random joke, if u want a joke in this command DM an admin', inline=False)
    embed.add_field(name='g rules', value='Returns server rules', inline=False)
    await ctx.send(embed=embed)

# Quote command
@client.command()
async def quote(ctx):
    responses = open('D:\Coding\PythonIsCool\game-bot\quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

# Joke command
@client.command()
async def joke(ctx):
    responses = open('D:\Coding\PythonIsCool\game-bot\jokes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

# Info command (This code made by Ethan Zhao)
@client.command()
async def info(ctx):
    embed = discord.Embed(title="game-bot Info", description="Bot by Frostt#1324")
    embed.add_field(name="**Bot version**", value="`v.1.1.4                 `", inline=True)
    embed.add_field(name="**Built with**", value="`Python3.8                `", inline=True)
    embed.add_field(name="**Contributors**", value="`NIHԀ˥Op#2625, christopher.lower()#4085`")
    embed.add_field(name="**This bot was made on**", value="`September 23rd, 2020     `", inline=False)
    embed.add_field(name="**Check out our github repo:**", value="`https://github.com/frostt127/game-bot     `", inline=False)
    await ctx.send(embed=embed)

# Rules Command
@client.command()
async def rules(ctx):
    await ctx.send(f'''1. BE RESPECTFUL.
Refrain from any content that are:
‣ Political, abusive, threatening.
‣ Obscene, defamatory, libellous.
‣ Racially, sexually, religiously.
‣ NSFW comments or pictures.
‣ Or otherwise objectionable or offensive.

2. TERM OF SERVICES.
‣ Discord Terms of Service
‣ Discussing or encouraging illegal, ToS violating content/behaviour or posting people personal information is prohibited.
‣ Posting links to torrent sites, encouraging hacking/DDOSing, or advocating other illegal activity is prohibited.

3. NO SPAMMING.
‣ The channel names and descriptions are pretty explanatory for what they are. Stay on topic.
‣ Voice channels are not meant for screaming, yelling, excessively swearing, or intentionally disrupting other peoples’ conversations.
‣ Do not tag roles or mention people for unnecessary reasons.
‣ Do not advertise or trade anything we do not permit.

4. MAINTAIN OUR SERVER.
‣ Do not invite any chat bots, use self-bots, and/or attempt to modify the server.
‣ Do not abuse the bots - this includes bypassing the filters, using unauthorized commands, and/or spam commands.
‣ Do not impersonate as someone else.
‣ Have appropriate usernames and nicknames in the server. Refer to Rule 1.

Ignorance will not be tolerated as an excuse.

If you accept this and still break any rule you are subject to any repercussions the staff deems appropriate.
Use the command !ilikecurry in access-request to gain access to the rest of the server, using this command means you have read and acknowledge the rules of our server.
5 or more infractions is a temp kick (length is determined by the seriousness of your action)
10 serious infractions will get you banned
Use the command !infractions in mee6 to see your infractions''')

# Run token
client.run('')
