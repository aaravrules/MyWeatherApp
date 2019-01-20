import urllib.request
import json

from tkinter import *

from pprint import pprint

key = "503ed57b27900c47536cbec6009d5475"
query = "New York"

url = "http://api.openweathermap.org/data/2.5/weather?q=" + query + "&units=imperial&appid=" + key

request = urllib.request.urlopen(url)
response = request.read().decode()
json_data = json.loads(response)

pprint(json_data)


class WeatherApp(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent


class CityPage(Frame):
    def __init__(self, parent, city):
        Frame.__init__(self, parent)
        self.parent = parent
        self.city = city

        self.current_weather_icon = Label()
