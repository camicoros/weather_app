from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Samara"):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}" \
                  f"&units=metric&lang=ru"
    weather_data = requests.get(weather_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Current weather ***\n")
    city = input("\nPlease enter a city name: ")
    # empty or spaces
    if not city.strip():
        city = "Moscow"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)