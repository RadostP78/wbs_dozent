import requests 
from pprint import pprint
import datetime

import os
import json
from pathlib import Path 
os.chdir(Path(__file__).parent)

with open("./config.json", mode = "r", encoding = "UTF-8") as file:
    config = json.load(file)

LAT = 52.53
LON = 13.38
APIKEY = config["apikey"]
CITIES = config["cities"]

CITYNAME = "Berlin"

url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={LAT}&lon={LON}&appid={APIKEY}"



for city in CITIES:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}&units=metric"
    print(url)

    # 1. Send the request
    response = requests.get(url)

    # 2. Print the response
    # print(response) # OK 200

    data = response.json()

    # pprint(data)



    # 3. Parse the required fields from the response
    temperature = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]

    sunrise = data["sys"]["sunrise"]  # 1671779752  -> UNIX Format
    sunrise = datetime.datetime.utcfromtimestamp(sunrise) #  2022-12-23 07:15:52


    sunset = data["sys"]["sunset"]  # 1671779752  -> UNIX Format
    sunset = datetime.datetime.utcfromtimestamp(sunset) #  2022-12-23 14:54:43



    # Print the Fields
    print(f"City: {city}")
    print("~" * 10)
    print(f"Temp: {temperature}")
    print(f"wind Speed: {wind_speed}")
    print(f"sunrise: {sunrise}")
    print(f"sunset: {sunset}")
    print()

