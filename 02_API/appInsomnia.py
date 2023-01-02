import requests

url = "https://api.openweathermap.org/data/2.5/weather"

querystring = {"q":"Berlin","appid":"API_Key","units":"metric"}

payload = ""
headers = {"Authorization": "Basic Og=="}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)