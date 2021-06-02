from os import environ
from flask import render_template, redirect, request
from flask.blueprints import Blueprint
import requests
from dotenv import dotenv_values

views = Blueprint('views', __name__)
try:
    load_env = dotenv_values(".env")
    API_KEY = load_env["API_KEY"]
except KeyError:
    API_KEY = environ.get("API_KEY")


def required_data(data_from_source):
    lon = str(data_from_source['coord']['lon'])
    lat = str(data_from_source['coord']['lat'])
    coordinates = str(lat + "," + lon)
    description = str(data_from_source['weather'][0]['description'])
    icon = str(data_from_source['weather'][0]['icon'])
    temp = str(data_from_source['main']['temp'])
    feels_like = str(data_from_source['main']['feels_like'])
    temp_min = str(data_from_source['main']['temp_min'])
    temp_max = str(data_from_source['main']['temp_max'])
    pressure = str(data_from_source['main']['pressure']) + " hpa"
    cloud_cover = str(data_from_source["clouds"]["all"])
    humidity = str(data_from_source['main']['humidity'])
    wind_speed = str(data_from_source['wind']['speed'])
    country_code = str(data_from_source["sys"]["country"])
    cityname = str(data_from_source["name"])
    response = str(data_from_source['cod'])

    data = {
        "coordinates": coordinates,
        "description": description,
        "icon": icon,
        "temp": temp,
        "feels_like": feels_like,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "pressure": pressure,
        "humidity": humidity,
        "cloud_cover": cloud_cover,
        "wind_speed": wind_speed,
        "country_code": country_code,
        "cityname": cityname,
        "response": response
    }
    return data


@views.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == "POST":
        city = request.form['city']
    else:
        city = "Madgaon"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    data_from_source = requests.get(url).json()
    try:
        data_to_client = required_data(data_from_source)
    except KeyError:
        data_to_client = "City Not Found"

    return render_template('index.html', data=data_to_client)
