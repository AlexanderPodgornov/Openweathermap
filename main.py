import json
import requests

api_key = 'ef7c6bbae06bcb0011a29f84a8f05c0c'

with open("current.city.list.json", 'r', encoding="utf-8") as f:
    data = json.load(f)

print("Введите население:")
population = int(input())

filtered_cities = [city for city in data if city["stat"]["population"] > population]

for city in filtered_cities:
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city['name'], api_key)
    response = requests.get(url)
    weather_data = response.json()
    if (int(weather_data["main"]["temp"] - 273.0) < 0) or (weather_data["weather"][0]["main"] == "Rain") or \
            (weather_data["weather"][0]["main"] == "Snow") or (weather_data["weather"][0]["main"] == "Clouds"):
        print(city["name"], int(weather_data["main"]["temp"] - 273.0))