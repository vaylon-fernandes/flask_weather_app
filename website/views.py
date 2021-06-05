from os import environ
from flask import render_template, redirect, request, flash
from flask.blueprints import Blueprint
from flask.scaffold import F
import requests
from .forms import CityForm


views = Blueprint('views', __name__)

API_KEY = environ.get("API_KEY")


def required_data(data_from_source):
    lon = str(data_from_source['coord']['lon'])
    lat = str(data_from_source['coord']['lat'])
    coordinates = str(lat + " ," + lon)
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
    }
    return data


def form_is_empmty(form):
    result = form == ''
    return result


@views.route('/', methods=['GET', 'POST'])
@views.route('/<city_name>', methods=['GET', 'POST'])
@views.route('/<city_name>/<country_name>', methods=['GET', 'POST'])
def weather(city_name=None, country_name=None):
    form = CityForm(request.form)
    if city_name and country_name:
        city = f"{city_name},{country_name}"
    elif city_name:
        city = city_name
    else:
        if request.method == "POST":

            city = request.form['city']
            if form_is_empmty(city) and not form.validate():
                flash('Please enter a City name')
        else:
            city = "Madgaon"

    url = f"http://api.openweathermap.org/data/2.5/find?q={city}&units=metric&appid={API_KEY}"

    get_data = requests.get(url).json()
    cities = get_data["list"]
    count = get_data["count"]

    if cities:
        data_to_client = []
        for city_data in cities:
            data_to_client.append(required_data(city_data))
    else:
        data_to_client = "City Not Found"

    if count > 1:

        flash(
            f'''Found {count} cities with the name {cities[0]['name']}. 
            For your search to be more accurate enter  
            'cityname, two character countrycode'. 
            For Example, ''', category="Info")

    return render_template('index.html', data=data_to_client, count=count, city=city, country=cities[0]["sys"]["country"])
