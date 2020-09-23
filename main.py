# Created by Eshaan Kumar on 9/22/2020
# Help from Ethan Zhao and Miheer Purandare
# Last updated 9/22/2020 by Eshaan Kumar

# Import modules
import discord
from discord.ext import commands
import asyncio
import random
import os

# Set prefix
client = commands.Bot(command_prefix = 'g ')

# Set help as game played
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
    await ctx.send(f'Error, Try "g help" command ({error})')

# Help command
# Remove original help command
client.remove_command('help')
# Add new help command
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='g ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name='g quote', value='Returns a random quote, if u want a quote in this command DM an OG', inline=False)
    embed.add_field(name='g joke', value='Returns a random joke, if u want a joke in this command DM an OG', inline=False)
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

# Run token
client.run('')
