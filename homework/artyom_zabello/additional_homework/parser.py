import re
import argparse
import requests
from bs4 import BeautifulSoup as BS
# from datetime import datetime
from colorama import init, Fore
init()


parser = argparse.ArgumentParser()
parser.add_argument("url", help="File's url")
parser.add_argument("date", help="date for search")
parser.add_argument("full", help="Full log or short")
args = parser.parse_args()


r = requests.get(args.url)
PAGE = str(BS(r.text, 'html.parser'))

with open("logs", "w+", encoding="utf-8") as file:
    file.write(PAGE)

with open("logs", "r", encoding="utf-8") as file:
    TEXT = str(file.read())
    times = list(re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}", TEXT))
    res = re.split(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}", TEXT)
result = dict(zip(times, res))
# lst = []
# for _, t in enumerate(times):
#     t1 = datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f")
#     lst.append(t1)
# result2 = dict(zip(lst, res))


def find_log(date, full):
    for i in result.keys():
        if i in date:
            if full == "Y":
                print(result.items())
            if full == "N":
                print(Fore.GREEN+str(result.items())[0:600].replace("dict_items(", ""))


find_log(args.date, args.full)
