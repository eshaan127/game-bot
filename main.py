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
client = commands.Bot(command_prefix = 'game ')

# Set help as game played
@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(name='game help'))

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

# Error message
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error, Try "game help" command ({error})')

# Help command
# Remove original help command
client.remove_command('help')
# Add new help command
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='game ping', value='Returns bot respond time in milliseconds', inline=False)
    await ctx.send(embed=embed)

# Run token
client.run('')
