import discord
from discord.ext import commands
import openai
import os
import requests
import json

openai.api_importkey = os.getenv('OPENAI_KEY')

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('we have logged in as %s'%client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi'):
        await message.channel.send('Hello! ' + f'{message.author}')
    elif message.content.lower().startswith('how are you'):
        await message.channel.send('I am fine...Thanks for asking!')
    elif message.content.startswith('inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    else:
        print(message.author)
        await message.channel.send('generating...')


        await message.channel.send(openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messagess=[
                {"role": "user", "content": message.content}
                ])["choices"][0]["message"]["content"])

client.run(os.getenv('TOKEN'))