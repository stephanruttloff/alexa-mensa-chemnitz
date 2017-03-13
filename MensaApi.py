import xmltodict

from urllib.request import urlopen
from string import Template
from Canteen import Canteen
from Meal import Meal
from Constants import *

CANTEENS = [
    ID_MENSA_REICHENHAIN,
    ID_MENSA_STRANA,
    ID_CAFETERIA_REICHENHAIN,
    ID_CAFETERIA_STRANA
]

TEMPLATE_API_ENDPOINT =\
    "https://www.swcz.de/bilderspeiseplan/xml.php" +\
    "?plan=${mensa_id}" +\
    "&jahr=${year}" +\
    "&monat=${month}" +\
    "&tag=${day}"


def getCanteenMeals(date, ids):
    canteens = ids
    if len(ids) == 0:
        canteens = CANTEENS
    for canteen_id in canteens:
        url = Template(TEMPLATE_API_ENDPOINT).substitute({
            'mensa_id': "%d" % canteen_id,
            'year': "%d" % date.year,
            'month': "%d" % date.month,
            'day': "%d" % date.day
        })

        endpoint = urlopen(url)
        data = endpoint.read()
        endpoint.close()
        data = xmltodict.parse(data)

        if "essen" in data["speiseplan"]:
            meals = [Meal(m) for m in data["speiseplan"]["essen"]]
            yield Canteen(canteen_id, meals)
        else:
            yield Canteen(canteen_id, [])
