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
    while True:
        print("Please Enter the City Name and Country Code.")
        print("City should be a real city follow correct Country CODE.")
        print("Example: City -> London, Country -> GB")

        city = input("Enter the city name here: ")
        country = input("Enter the country CODE: ")

        api_url = (
            'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'
            .format(city, country, KEY))
        result = requests.get(api_url)
        data = result.json()

        if validate_city(data, country, city):
            break

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
    print(f"* Weather Status for {city} - Today {date_time} *")
    print("*****************************************************")
    print(f"Current Temperature is -------> {temp:.2f} degrees Celsius")
    print(f"Feels Like -------------------> {feels_like:.2f} degrees Celsius")
    print(f"Max Temperature for Today is -> {temp_max:.2f} degrees Celsius")
    print(f"Min Temperature for Today is -> {temp_min:.2f} degrees Celsius")
    print(f"Current Weather Description --> {weather_description.title()}")
    print(f"Current Humidity -------------> {air_humidity}%")
    print(f"Current Wind Speed------------> {wind_speed} kmph")


def validate_city(data, country, city):
    """
    Validate the City name
    If the city name are not inside the API db get a error and try again
    Else, give all info to client
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
    else:
        return True


get_weather()
