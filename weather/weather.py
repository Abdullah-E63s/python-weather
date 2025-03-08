from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city='London'):
    # check for empty strings or string with only spaces
    if not city or not city.strip():
        city = 'London'
        
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API-KEY')}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":

    print('\n*** Get weather conditions ***\n')
    city = input("\n please enter a city name")
    weather_data = get_current_weather(city)

    # check for empty strings or string with only spaces

    print('\n')
    pprint(weather_data)

