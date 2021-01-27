import requests
import re
from bs4 import BeautifulSoup
from itertools import islice
from typing import Any

def convertTuple(tup):
    str =  ' '.join(tup)
    return str

def retrieveTopGames(category):
    url = ""
    if category == "action":
        url = 'https://store.steampowered.com/search/?filter=topsellers&tags=19'
        print("Retrieving action games.")
    elif category == "rpg":
        url = 'https://store.steampowered.com/search/?filter=topsellers&tags=122'
        print("Retrieving RPG games.")
    elif category == "multiplayer":
        url = 'https://store.steampowered.com/search/?tags=19%2C3859&filter=topsellers'
        print("Retrieving multiplayer games.")
    elif category == "sale":
        url = 'https://store.steampowered.com/search/?filter=topsellers&specials=1'
        print('Retrieving games on sale.')
    elif category == "actsale":
        url = 'https://store.steampowered.com/search/?tags=19%2C122&specials=1&filter=topsellers'
        print('Retrieving top action sale games')
    elif category == "indiesale":
        url = 'https://store.steampowered.com/search/?tags=492&specials=1&filter=topsellers'
        print('Retrieving indie games on sale')
    elif category == "mpsale":
        url = 'https://store.steampowered.com/search/?tags=3859%2C19&specials=1&filter=topsellers'
        print('Retrieving multiplayer games on sale')
    elif category == "new":
        url = 'https://store.steampowered.com/search/?filter=topsellers&specials=1'
        print('Retrieving new games from Steam.')
    elif category == "indie":
        url = 'https://store.steampowered.com/search/?tags=492&specials=1&filter=topsellers'
        print('Retrieving top indie games.')
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.content, 'html.parser')
    names = []
    for x in soup.find_all("span", {"class": "title"}):
        names.append(x.get_text())
    prices = []
    for y in soup.find_all("div", {"class": "search_price"}):
        prices.append((y.get_text()).replace("\r\n", "").strip())
    res = {}
    for name in names:
        for price in prices:
            res[name] = price
            prices.remove(price)
            break

    result = ""
    n_items: list[Any] = list(islice(res.items(), 10))
    for key in n_items:
        result += convertTuple(key)
        result += "\n"
    r1 = re.findall(r"[$]\d{0,2}.\d{0,2}[$]\d{0,2}.\d{0,2}", result)
    for price in r1:
        result = result.replace(price, price[6:len(price)])
    return result