import urllib
import json
import os
from dotenv import load_dotenv
import discord
from datetime import date

load_dotenv()
token = os.getenv('WEATHER_TOKEN')

def retrieveWeather(zipcode):
    with urllib.request.urlopen("http://api.weatherapi.com/v1/forecast.json?key="+token+"&q="+zipcode+"&days=1&aqi=no&alerts=no") as url:
        data = json.loads(url.read().decode())
    propData = data['forecast']['forecastday'][0]['day']
    today = propData
    #today = next(iter(propData))
    final_string = "**High**: " + str(today['maxtemp_f']) + "°F\r\n**Low**: " + str(today['mintemp_f']) + "°F\r\n" + "**Chance of Rain**: " + today['daily_chance_of_rain'] + "%\r\n**Condition**: " + today['condition']['text']
    return final_string

def compileWeather():
    current=date.today()
    embedVar = discord.Embed(title="Local Weather", description="Weather for everyone", color=0x008FFF)
    embedVar.set_thumbnail(url="http://cdn.weatherapi.com/weather/64x64/day/116.png")
    embedVar.add_field(name="__Grand Rapids, MI__", value=retrieveWeather("49534"), inline=False)
    embedVar.add_field(name='\u200B', value='\u200B', inline=False)
    embedVar.add_field(name="__Commerce Township, MI__", value=retrieveWeather("48382"), inline=False)
    embedVar.add_field(name='\u200B', value='\u200B', inline=False)
    embedVar.add_field(name="__Minneapolis, MN__", value=retrieveWeather("55414"), inline=False)
    embedVar.set_footer(text="Date ran: " + current.strftime('%m/%d/%Y') + ". Dev: Hunter & Greg")
    return embedVar
    """
    loc1 = retrieveWeather("49534")
    loc2 = retrieveWeather("48382")
    loc3 = retrieveWeather("55414")
    return loc1 + "\r\n" +loc2 + "\r\n" + loc3
    """