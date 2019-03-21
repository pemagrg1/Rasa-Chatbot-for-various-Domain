from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		import requests
		import json

		url = "{API LINK}"

		p = requests.get(url)
		data_json = json.loads(p.text)
		data = data_json["data"]

		country = "Nepal"
		city = data["10"]["cityName"]
		loc = city
		condition = data["10"]["weatherMain"]
		temperature_c = data["10"]["temp"]
		humidity = data["10"]["humidity"]
		wind_mph = data["10"]["windSpeed"]

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

