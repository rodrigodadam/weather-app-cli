import requests
import os
import re
from datetime import datetime
if os.path.exists("env.py"):
    import env


def get_weather():
    """
    Get the today's weather forecast for determined city
    """
    while True:
        print("Please Enter the City Name and Country Code.")
        print("The city must be a real city, following the correct country code.")
        print("Example: City -> London, Country -> GB")

        city = input("Enter the city name: ")
        country = input("Enter the country CODE: ")

        if input_validation(city, country):
            data = api_request(city, country)
            if validate_city(data, country, city):
                break
    render(data)


def validate_city(data, country, city):
    """
    Validate the City name
    If the city name are not inside the API db get a error and try again
    Else, give all weather info to client
    """
    if data['cod'] == '404':
        print("***********************************************")
        print(f"Invalid City or Country: {city},{country}.")
        print("Please check the city name and country code provided")
        print("Please insert a valid Country CODE with 2 letters")
        print("The country code and city need match")
        print("Example: DUBLIN - IE for city Dublin and country Ireland")
        print("***********************************************")
        return False
    return True


def input_validation(city, country):
    """
    Validate the input data before send the api_request()
    to avoid code injection.
    """
    if not re.search("^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", city):
        print("***********************************************")
        print("Please DO NOT use special characters or numbers")
        print("***********************************************")
        return False

    if not re.search("^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", country):
        print("***********************************************")
        print("Please DO NOT use special characters or numbers")
        print("***********************************************")
        return False
    return True


def api_request(city, country):
    """
    Prepares the endpoint so that the API request is made and
    return the request in JSON.
    """
    KEY = os.environ.get('API_KEY')
    endpoint = (
            'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'
            .format(city, country, KEY))
    result = requests.get(endpoint)
    return result.json()


def render(data):
    """
    Create variables to store data from API and
    render all weather status.
    """
    temp = ((data['main']['temp']) - 273.15)
    feels_like = ((data['main']['feels_like']) - 273.15)
    temp_min = ((data['main']['temp_min']) - 273.15)
    temp_max = ((data['main']['temp_max']) - 273.15)
    weather_description = data['weather'][0]['description']
    air_humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    country = data['sys']['country']
    date_time = datetime.now().strftime("%d %b %Y")

    print("*****************************************************")
    print(f"* Weather Status for {data['name']} - Today {date_time} *")
    print("*****************************************************")
    print(f"Current Temperature is -------> {temp:.2f} degrees Celsius")
    print(f"Feels Like -------------------> {feels_like:.2f} degrees Celsius")
    print(f"Max Temperature for Today is -> {temp_max:.2f} degrees Celsius")
    print(f"Min Temperature for Today is -> {temp_min:.2f} degrees Celsius")
    print(f"Current Weather Description --> {weather_description.title()}")
    print(f"Current Humidity -------------> {air_humidity}%")
    print(f"Current Wind Speed------------> {wind_speed} kmph")


print("Check the today's weather in your city")
get_weather()
