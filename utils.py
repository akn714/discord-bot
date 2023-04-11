import openai
import requests
import json
import os

openai.api_key = os.getenv('OPENAI_KEY')


def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + ' -' + json_data[0]['a']
        return quote
    except:
        print("[!] random quotes api is not working, need to fix it")
        return "SORRY NO QUOTE AVAILABLE !"

def get_joke():
    try:
        joke = requests.get('https://jokes-api.gamhcrew.repl.co/')
        return joke.text
    except:
        print("[!] random joke api is not working, need to fix it")
        return "SORRY NO JOKE AVAILABLE !"

def chat_gpt_get(content):
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [ 
                {"role": "user", "content": content}
            ]
        )["choices"][0]["message"]["content"] 
        return response
    except Exception as e:
        print("[!] Failed to get Chat-GPT reponse, need to fix it")
        print(e)
        return "SORRY SOME INTERNAL ERROR !"
