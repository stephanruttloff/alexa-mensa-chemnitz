import logging
import MensaApi

from flask import Flask, render_template
from flask_ask import Ask, statement, question
from datetime import datetime

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launch():
  welcome_msg = render_template('welcome')
  return question(welcome_msg).reprompt(render_template('reprompt'))

@ask.intent('AMAZON.HelpIntent')
def help():
  rendered = render_template('help')
  return question(rendered).reprompt(render_template('reprompt'))

@ask.intent('AMAZON.StopIntent')
def stop():
  rendered = render_template('stop')
  return statement(rendered)

@ask.intent('GetMenu')
def getMeals():
  date = datetime.now()
  return getMealsDate(date)

@ask.intent('GetMenuDate', convert={'date': 'date'})
def getMealsDate(date):
  date = datetime.combine(date, datetime.min.time())
  canteens = list(MensaApi.getCanteenMeals(date))
  return respond(date, canteens)

def renderMeals(canteen):
  return "<break strength='medium'/>oder<break strength='medium'/>".join([m.description for m in canteen.meals]).strip()

def renderDate(date):
  return "<say-as interpret-as='date'>" + date.strftime("????%m%d") + "</say-as>"

def respond(date, canteens):
  meals = [meal for canteen in canteens for meal in canteen.meals]

  if len(meals) == 0:
    return statement("<speak>" + render_template('meals_none', date=renderDate(date)) + "</speak>")
  else:
    first_canteen = canteens.pop(0)
    remaining_canteens = canteens
    remaining_rendered = []

    for canteen in remaining_canteens:
      print("remaining", canteen.name)
      if len(canteen.meals) == 0:
        print("none")
        rendered = render_template('meals_remaining_none', canteen=canteen.name)
        remaining_rendered.append("<p>" + rendered + "</p>")
      else:
        print("not none")
        meals_string = renderMeals(canteen)
        rendered = render_template('meals_remaining', canteen=canteen.name, meals=meals_string)
        remaining_rendered.append("<p>" + rendered + "</p>")

    remaining = "".join(remaining_rendered)
    first = render_template('meals_first', date=renderDate(date), canteen=first_canteen.name, meals=renderMeals(first_canteen))
    return statement("<speak>" + first + remaining + "</speak>")

if __name__ == '__main__':
  app.run(debug=True)
