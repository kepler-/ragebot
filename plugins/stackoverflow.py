from urllib import quote, unquote
from bs4 import BeautifulSoup
import re
import requests


def so(q):
    query = quote(q)
    # url = "https://encrypted.google.com/search?q={0}".format(query)
    url = "https://encrypted.google.com/search?q=stackoverflow+{0}".format(query)
    soup = BeautifulSoup(requests.get(url).text)

    answers = soup.findAll("h3", attrs={"class": "r"})
    if not answers:
        return ":crying_cat_face: Sorry, stackoverflow doesn't have an answer for you :crying_cat_face:"

    # results =

    res1 = unquote(re.findall(r"q=(.*?)&", str(answers[0]))[0])
    res2 = unquote(re.findall(r"q=(.*?)&", str(answers[1]))[0])

    # return unquote(re.findall(r"q=(.*?)&", str(answer[0]))[0])
    return res1 + "\n" + res2


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!so (.*)", text)
    if not match: return

    return so(match[0])
