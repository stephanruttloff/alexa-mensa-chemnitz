import re

from pprint import pprint
import json

class Meal(object):
  "contains information for one meal"

  def __init__(self, api_response):
    self.id = api_response["@id"]
    self.category = api_response["@kategorie"]
    self.rating = api_response["@bewertung"]
    self.has_img = api_response["@img"] == "true"
    self.with_pig = api_response["@schwein"] == "true"
    self.with_beef = api_response["@rind"] == "true"
    self.with_alcohol = api_response["@alkohol"] == "true"
    self.vegetarian = api_response["@vegetarisch"] == "true"
    self.description = api_response["deutsch"].strip()

    if self.has_img:
      self.img_small = api_response["@img_small"]
      self.img_large = api_response["@img_big"]

    if isinstance(api_response["pr"], list):
      # multiple rates
      for rate in [] + api_response["pr"]:
        if "@gruppe" in rate:
          if rate["@gruppe"] == "S":
            self.rate_s = rate["#text"]
          elif rate["@gruppe"] == "M":
            self.rate_m = rate["#text"]
          elif rate["@gruppe"] == "G":
            self.rate_g = rate["#text"]
          else:
            self.rate_s = rate["#text"]
            self.rate_m = rate["#text"]
            self.rate_g = rate["#text"]
    else:
      rate = api_response["pr"]["#text"]
      self.rate_s = rate
      self.rate_m = rate
      self.rate_g = rate

    # strip incredient codes from description
    self.description = re.sub(r"(\([\d,\s]+\))", r"", self.description)
    # strip multiple whitespaces from description
    self.description = re.sub(r"\s+", r" ", self.description)
