import requests
import os
from datetime import datetime
from creds import API_KEY

api_key = os.environ['API_KEY']
location = input("Enter the city name:")