import logging
import MensaApi

from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from datetime import datetime

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launch():
  welcome_msg = render_template('welcome')
  return statement(welcome_msg)

@ask.intent('AMAZON.StopIntent')
def stop():
  rendered = render_template('exit')
  return statement(rendered)

@ask.intent('GetMenu')
def getMeals():
  date = datetime.now()
  canteens = MensaApi.getCanteenMeals(date)
  responses = []
  for canteen in canteens:
    if len(canteen.meals) == 0:
      rendered = render_template('meals_today_none', canteen=canteen.name)
      responses.append("<p>" + rendered + "</p>")
    else:
      meals_string = "<break strength='medium'/>oder<break strength='medium'/>".join([m.description for m in canteen.meals]).strip()
      rendered = render_template('meals_today', canteen=canteen.name, meals=meals_string)
      responses.append("<p>" + rendered + "</p>")
  response = "".join(responses)
  response = "<speak>" + response + "</speak>"
  return statement(response)

if __name__ == '__main__':
  app.run(debug=True)