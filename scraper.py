import requests
from bs4 import BeautifulSoup
from itertools import islice
from typing import Any

def get_action_games():
    print("Retrieving action games")

    url = 'https://store.steampowered.com/search/?filter=topsellers&tags=19'
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

    n_items: list[Any] = list(islice(res.items(), 10))

    return n_items.__str__()
