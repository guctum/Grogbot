import os
import random
import requests
import scraper
import weather
import exercise
import re
import spotifyPlaylist

import discord

from discord.ext import tasks
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

    if message.content == '!chuck':
        url = "https://api.chucknorris.io/jokes/random"
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json().get('value')
        await message.channel.send(response)

    if message.content == '!help':
        await message.channel.send("!joke - get a random dad joke" + "\r\n" +
                                   "!chuck - get a random Chuck Norris fact" + "\r\n" +
                                   "!action - display popular action games" + "\r\n" +
                                   "!rpg - display popular rpg games" + "\r\n" +
                                   "!mp - display popular multiplayer games" + "\r\n" +
                                   "!sale - retrieve steam sale games" + "\r\n" +
                                   "!actsale - display action games on sale" + "\r\n" +
                                   "!indiesale - display indie games on steam" + "\r\n" +
                                   "!mpsale - display multiplayer games on sale")

    if message.content == '!action':
        await message.channel.send(scraper.retrieveTopGames('action'))

    if message.content == '!rpg':
        await message.channel.send(scraper.retrieveTopGames("rpg"))

    if message.content == '!mp':
        await message.channel.send(scraper.retrieveTopGames("multiplayer"))

    if message.content == '!sale':
        await message.channel.send(scraper.retrieveTopGames("sale"))

    if message.content == '!actsale':
        await message.channel.send(scraper.retrieveTopGames("actsale"))

    if message.content == '!indiesale':
        await message.channel.send(scraper.retrieveTopGames("indiesale"))

    if message.content == '!mpsale':
        await message.channel.send("Work in progress." + "\r\n" +
                                   scraper.retrieveTopGames("mpsale"))

    if message.content == '!new':
        await message.channel.send(scraper.retrieveTopGames("new"))

    if message.content == '!indie':
        await message.channel.send(scraper.retrieveTopGames("indie"))

    if message.content == '!weather':
        await message.channel.send(embed=weather.compileWeather())

    # if "-play" in message.content:
    #     url = re.search('https:\W.+', message.content)[0]
    #     if "track" in url:
    #         spotifyPlaylist.checkTrackExists(url)

    # if "!exercise" in message.content:
    #    command = ""
    #    try:
    #        command = re.search('-\w+', message.content)[0]
    #    except:
    #        command = "-h"
    #    await message.channel.send(embed=exercise.getExercise(command))
    #    await message.channel.send(exercise.pullInWorkouts("Arms"))

    if message.content == '!start':
        mytask.start()


@tasks.loop(seconds=86400)  # 1 day
async def mytask():
    channelId = os.getenv('BOT_CHANNEL')
    channel = client.get_channel(int(channelId))
    await channel.send(embed=weather.compileWeather())

client.run(TOKEN)
