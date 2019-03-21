from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        data = {
            "Paris":
                {
                    "cityName": "Paris",
                    "weatherMain": "Cloudy",
                    "temp": 20,
                    "humidity": 13,
                    "windSpeed": 1.5,
                },
            "London":
                {
                    "cityName": "London",
                    "weatherMain": "Cloudy",
                    "temp": 20,
                    "humidity": 13,
                    "windSpeed": 1.5,
                },
            "Italy":
                {
                    "cityName": "Italy",
                    "weatherMain": "Cloudy",
                    "temp": 20,
                    "humidity": 13,
                    "windSpeed": 1.5,
                }

        }

        city = data["Paris"]["cityName"]
        loc = city
        condition = data["Paris"]["weatherMain"]
        temperature_c = data["Paris"]["temp"]
        humidity = data["Paris"]["humidity"]
        wind_mph = data["Paris"]["windSpeed"]

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]

