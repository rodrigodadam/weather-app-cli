import requests
import os
from datetime import datetime

API_KEY = os.environ.get('API_KEY')


def get_weather():
    """
    Get the today's weather forecast for determined city
    """
    print("Please Enter the City Name.")
    print("City should be a real city.")
    print("Exemple: Dublin")

    city = input("Enter the city name here: ")
    print(f"This is your provided city: {city}")


get_weather()