import urllib
import json
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('WEATHER_TOKEN')

def retrieveWeather(zipcode):
    with urllib.request.urlopen("http://api.weatherapi.com/v1/forecast.json?key="+token+"&q="+zipcode+"&days=1&aqi=no&alerts=no") as url:
        data = json.loads(url.read().decode())
    propData = data['forecast']['forecastday'][0]['day']
    today = propData
    #today = next(iter(propData))
    final_string = "------------------------------------------------------------ \r\n" + "| Today in "+ data['location']['name'] +" | \r\n" + "High: " + str(today['maxtemp_f']) + "°F\r\nLow: " + str(today['mintemp_f']) + "°F\r\n" + "Chance of Rain: " + today['daily_chance_of_rain'] + "\r\nCondition: " + today['condition']['text'] + "\r\n------------------------------------------------------------"
    #final_string = final_string
    return final_string

def compileWeather():
    loc1 = retrieveWeather("49534")
    loc2 = retrieveWeather("48382")
    loc3 = retrieveWeather("55414")
    return loc1 + "\r\n" +loc2 + "\r\n" + loc3