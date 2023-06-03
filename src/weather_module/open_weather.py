import requests
import os


API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    weather_data =  response.json()

    if weather_data['cod'] == 200:
        return weather_data
    else:
        raise Exception(weather_data['message'])