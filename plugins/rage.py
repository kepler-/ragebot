import re
from bs4 import BeautifulSoup
import requests


def rage(text):
    if text == "ot":
        url = "http://www.rage3d.com/board/forumdisplay.php?f=2"
        soup = BeautifulSoup(requests.get(url).text)
        thread_title_links = soup.find_all("a", attrs={"id": re.compile('thread_title_.*')})

        thread_texts = ""
        current = 1
        max = 5
        for thread_title_link in thread_title_links:
            if current <= max:
                thread_texts += thread_title_link.text + ": http://www.rage3d.com/board/" + thread_title_link['href'] + "\n"
                current += 1

        return thread_texts


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!rage (.*)", text)
    if not match: return

    term = match[0]
    return rage(term)
