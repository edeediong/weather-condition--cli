import os

from datetime import datetime
from dotenv import load_dotenv

import requests
import click


def initialize():
    load_dotenv()

    api_key = os.environ.get("WEATHER_API_KEY")

    today = datetime.now()
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=auto:ip&dt={today.date()}"
    response = requests.get(url)
    json_response = response.json()
    forecast = json_response["forecast"]["forecastday"][0]

    return forecast, today


def shine(uv):
    print(f"Today's prediction for UV index: {uv}")
    if uv > 3:
        return True


def rain(chance_of_rain):
    print(f"Today's chance of rain: {chance_of_rain}%")
    if chance_of_rain > 5:
        return True


@click.command()
@click.argument("condition", type=str)
def weather(condition):
    forecast, today = initialize()

    if condition == "shine":
        uv_today = forecast["day"]["uv"]
        value = shine(uv_today)
        return value

    if condition == "rain":
        current_hour = today.hour
        chance_of_rain = forecast["hour"][current_hour]["chance_of_rain"]
        value = rain(chance_of_rain)
        return value

    print("Please enter 'rain' or 'shine' as arguments!")


if __name__ == "__main__":
    weather()
