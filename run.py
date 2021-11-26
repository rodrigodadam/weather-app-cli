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
    result = requests.get(api_url)
    data = result.json()
    validate_city(data)
    


def validate_city(data):
    """
    Validate the City name
    If the city name are not inside the API db get a error and try again
    Else, give all info to client
    """
    if data['cod'] == '404':
        print("Invalid City: {}, Please check your city name")
    else:
        return print(data)





get_weather()