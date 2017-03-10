class Canteen(object):
  "represents a canteen"

  def __init__(self, id, meals):
    self.meals = meals;

    if id == 1479835489:
      self.name = "Mensa Reichenhainer Strasse"
    elif id == 773823070:
      self.name = "Mensa Strasse der Nationen"
    elif id == 7:
      self.name = "Cafeteria Reichenhainer Strasse"
    elif id == 6:
      self.name = "Cafeteria Strasse der Nationen"