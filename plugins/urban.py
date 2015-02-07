"""!urban <query> queries urban dictionary"""

import re
from urllib import quote


def urban(q):
    query = quote(q)

    return "http://www.urbandictionary.com/define.php?term={0}".format(query)


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!urban (.*)", text)
    if not match: return

    return urban(match[0])
