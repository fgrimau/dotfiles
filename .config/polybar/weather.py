import requests
import json
import os

API_KEY = os.environ.get("OPENWEATHER_KEY", None)

if API_KEY is None:
    print("No key found")
    exit(0)

API_URL = "https://api.openweathermap.org/data/2.5/weather?q=brussels&appid={}".format(API_KEY)

r = requests.get(API_URL)
data = json.loads(r.content)

weather_icons = {
    "01": "",
    "02": "",
    "03": "",
    "04": "",
    "O9": "",
    "10": "",
    "11": "",
    "13": "",
    "50": "",
}

weather_id = data["weather"][0]['id']
weather_icon = data["weather"][0]['icon'][:-1]
weather_desc = data["weather"][0]['description']
temperature = data["main"]['temp'] - 273.15


print("T° : {}  -  {}  {}".format(round(temperature, 2), weather_icons[weather_icon], weather_desc))
