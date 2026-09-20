import requests

api_key="9c5f073441b9482017a597e3e209d791"
api_url=f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"


# Uncomment before deployment
# def fetch_data():
#     print("Fetching weather data from  web API...")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("api response recieved succesfull")
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f" an error occured: {e}")
#         raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-09-18 00:23', 'localtime_epoch': 1789690980, 'utc_offset': '-4.0'}, 'current': {'observation_time': '04:23 AM', 'temperature': 24, 'weather_code': 176, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0025_light_rain_showers_night.png'], 'weather_descriptions': ['Patchy rain nearby'], 'astro': {'sunrise': '06:39 AM', 'sunset': '07:00 PM', 'moonrise': '02:32 PM', 'moonset': '11:10 PM', 'moon_phase': 'First Quarter', 'moon_illumination': 42}, 'air_quality': {'co': '223', 'no2': '34.5', 'o3': '53', 'so2': '2.7', 'pm2_5': '15.7', 'pm10': '16.8', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 14, 'wind_degree': 217, 'wind_dir': 'SW', 'pressure': 1017, 'precip': 0, 'humidity': 78, 'cloudcover': 100, 'feelslike': 25, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}