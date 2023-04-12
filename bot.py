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
        # await message.channel.send('Hello! ' + f'{message.author}')
        await message.channel.send(f'Hello, {message.author}', reference=message)

    elif message.content.lower().startswith('how are you'):
        # await message.channel.send('I am fine...Thanks for asking!')
        await message.channel.send('I am fine...Thanks for asking!', reference=message)

    elif message.content.lower().startswith('inspire'):
        quote = get_quote()
        # await message.channel.send(quote)
        await message.channel.send(quote, reference=message)

    elif message.content.lower().find("joke")!=-1:
        joke = get_joke()
        # await message.channel.send(joke)
        await message.channel.send(joke, reference=message)

    else:
        print(message.author)
        await message.channel.send('generating...')
        content = chat_gpt_get(message.content, debub=True)
        await message.channel.send(content, reference=message)



client.run(os.getenv('TOKEN'))
