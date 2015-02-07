"""!xkcd displays the latest xkcd"""

import re
from bs4 import BeautifulSoup
import requests


def xkcd():
    try:
        url = "http://xkcd.com/"
        soup = BeautifulSoup(requests.get(url).text)

        comic_div = soup.find("div", attrs={"id": "comic"})

        children = comic_div.findChildren()

        for child in children:
            return child['src']
    except Exception as e:
        return "Computer says no: " + e.message


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!xkcd", text)
    if not match: return

    return xkcd()