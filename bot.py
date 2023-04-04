import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('we have logged in as %s'%client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('how are you'):
        await message.channel.send('I am fine...Thanks for asking!')


client.run(os.getenv('TOKEN'))
