import os
import requests
from dotenv import load_dotenv
load_dotenv()
url="https://api.weatherapi.com/v1/current.json"
api_key = os.getenv("WEATHER_API_KEY")
if not api_key:
   raise ValueError("API key not found")
params={
    "key":api_key,
    "q":"hyderabad"
}
try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    result = response.json()

    print("status code:", response.status_code)
    # loctaion
    city = result["location"]["name"]
    region = result["location"]["region"]
    country = result["location"]["country"]
    # weather
    current = result["current"]
    temperature = current["temp_c"]
    feels_like = current["feelslike_f"]
    humidity = current["humidity"]
    condition = current["condition"]["text"]
    last_updated = current["last_updated"]
    print("city name: ", city)
    print("region:", region)
    print("temperature in celsius:", temperature)
    print("feels_like temperature:", feels_like)
    print("humidity:", humidity)
    print("weather condition:", condition)
    print("last updated:", last_updated)


except requests.exceptions.RequestException as e:
    print(e)
except (KeyError, TypeError) as e:
    print("unexpected API response")

