from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_cerrent_weather(city="Vladivostok City"):

    requests_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}"
    weather_data = requests.get(requests_url).json()
    return weather_data

if __name__ == "__main__":

    print('\n*** Get Current Weather Conditions ***\n')

    city = input("Enter a city: ")

    #Check for empty strings or sting with only spaces
    if not bool(city.strip()):
        city = "Vladivostok City"

    weather_data = get_cerrent_weather(city)

    print("\n")
    pprint(weather_data)