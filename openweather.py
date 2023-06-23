import requests
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()

api = os.getenv('APIKEY')

def openweatherinfo(city_name):
    link = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api,
        'units': 'metric',
        'lang': 'ru'
    }
    respone = requests.get(link, params=params)
    data = respone.json()

    uzunlik = data['coord']['lon']
    kenglik = data['coord']['lat']
    main = data['weather'][0]['main']
    desc = data['weather'][0]['description']
    temp = data['main']['temp']
    feelslike = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressure = data['main']['pressure']
    humidity  = data['main']['humidity']
    windspeed = data['wind']['speed']
    clouds = data['clouds']['all']
    country = data['sys']['country']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']

    sunset = datetime.fromtimestamp(sunset)
    sunrise = datetime.fromtimestamp(sunrise)
    cod = data['cod']

    text = f'''Shahar: {city_name}
Davlat: {country}
Shahar kodi: {cod}
Koordiatalari: uzunlik: {uzunlik}
               kenglik: {kenglik}
Havo: {main}, {desc}
Harorat: {temp} ˚C
Tuyuladi: {feelslike} ˚C
Minimal harorat: {temp_min} ˚C
Maksimal harorat: {temp_max} ˚C
Bosim: {pressure} Pa
Namlik: {humidity} %
Shamol tezligi: {windspeed} m/s
Bulutlar: {clouds}

Quyosh chiqishi: {sunrise}
Quyosh botishi: {sunset}
'''
    return text
