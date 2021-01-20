import os
import random
import requests
import scraper

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

scraper = scraper

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '!99':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        # TODO: look into hitting a Brooklyn 99 quotes API

    if message.content == '!joke':
        url = "https://icanhazdadjoke.com"
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json().get('joke')
        await message.channel.send(response)

    if message.content == '!action':
        await message.channel.send(scraper.retrieveTopGames('action'))

    if message.content == '!rpg':
        await message.channel.send(scraper.retrieveTopGames("rpg"))

    if message.content == '!mp':
        await message.channel.send(scraper.retrieveTopGames("multiplayer"))

client.run(TOKEN)
