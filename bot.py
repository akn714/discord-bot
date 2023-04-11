#!/usr/bin/env python3

# author: Adarsh Kumar (https://github.com/adarshkumar714)

import discord
from discord.ext import commands
import os
from utils import *

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())


@client.event
async def on_ready():
    print('we have logged in as %s'%client.user)


@client.event
async def on_message(message):

    if str(message.channel)!="chat-with-bot" or message.author == client.user:
        return

    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi'):
        await message.channel.send('Hello! ' + f'{message.author}')

    elif message.content.lower().startswith('how are you'):
        await message.channel.send('I am fine...Thanks for asking!')

    elif message.content.lower().startswith('inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    elif message.content.lower().find("joke")!=-1:
        joke = get_joke()
        await message.channel.send(joke)

    else:
        print(message.author)
        await message.channel.send('generating...')
        await message.channel.send(chat_gpt_get(message.content))


client.run(os.getenv('TOKEN'))
