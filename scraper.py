import requests
from bs4 import BeautifulSoup
from itertools import islice

url = 'https://store.steampowered.com/search/?filter=topsellers&tags=19'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}
response = requests.get(url, headers=header)

def get_action_games():
    print("Retrieving action games")
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

    n_items = list(islice(res.items(), 10))

    print(n_items)
