import requests
import os
from datetime import datetime
if os.path.exists("env.py"):
    import env

KEY = os.environ.get('API_KEY')


def get_weather():
    """
    Get the today's weather forecast for determined city
    """
    print("Please Enter the City Name.")
    print("City should be a real city.")
    print("Exemple: Dublin")

    city = input("Enter the city name here: ")
    # print(f"This is your provided city: {city}")
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, KEY)
    r = requests.get(api_url)
    return r.json()


print(get_weather())