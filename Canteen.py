from Constants import *


class Canteen(object):
    "represents a canteen"

    def __init__(self, id, meals):
        self.meals = meals

        if id == ID_MENSA_REICHENHAIN:
            self.name = "Mensa Reichenhainer Strasse"
        elif id == ID_MENSA_STRANA:
            self.name = "Mensa Strasse der Nationen"
        elif id == ID_CAFETERIA_REICHENHAIN:
            self.name = "Cafeteria Reichenhainer Strasse"
        elif id == ID_CAFETERIA_STRANA:
            self.name = "Cafeteria Strasse der Nationen"
