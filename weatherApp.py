import urllib.request
import json

from tkinter import *

from pprint import pprint
root = Tk()

norm_font = ("Consolas", 20)
bold_font = ("Consolas", 20, "bold")

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

        photo = PhotoImage(file="logo.png")
        w = Label(parent, image=photo)
        w.photo = photo
        w.grid(row = 1, column = 1, columnspan = 1)

        self.current_weather_icon = Label(root, text = query, font = bold_font)
        self.current_weather_icon.grid(row = 2, column = 1, columnspan = 1)

        temp = json_data['main']['temp']
        
        self.current_weather_icon = Label(root, text = query, font = bold_font)
        self.current_weather_icon.grid(row = 2, column = 1, columnspan = 1)

        self.current_weather_icon = Label(root, text = str(temp) + " °C", font = norm_font)
        self.current_weather_icon.grid(row = 3, column = 1, columnspan = 1)
        

cityObj = CityPage(root, query);
