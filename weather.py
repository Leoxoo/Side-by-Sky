import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    name: str
    main: str
    description: str
    icon: str
    temperature: int
    humidity: int

def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}'
    ).json()

    if not resp:  # If resp is empty or None
        return None, None
    
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

def get_current_weather(city_name, lat, lon, API_key):
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric'
    ).json()

    print(f"API Response for {city_name}: {resp}")  # Debugging API response

    if 'weather' not in resp or 'main' not in resp:
        print(f"Invalid data for {city_name}. Check API response.")
        return WeatherData(name=city_name, main='', description='', icon='', temperature=0, humidity=0)

    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=int(resp.get('main').get('temp', 0)),
        name=city_name,
        humidity=int(resp.get('main').get('humidity', 0))
    )
    print(f"Processed Weather Data for {city_name}: {data}")
    return data


def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    # If lat or lon is None, handle gracefully
    if lat is None or lon is None:
        return None
    
    weather_data = get_current_weather(city_name, lat, lon, api_key)
    return weather_data

if __name__ == "__main__":
    lat, lon = get_lat_lon('Dallas', 'TX', 'USA', api_key)
    city_name = 'Dallas'
    print(get_current_weather(city_name, lat, lon, api_key))