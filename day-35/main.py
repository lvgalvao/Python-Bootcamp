import datetime 
import requests
from config import API_KEY_CONFIG, LATITUDE, LONGITUDE, PASSWORD, EMAIL_FROM, EMAIL_TO
import smtplib


MY_EMAIL = EMAIL_FROM
MY_PASSWORD = PASSWORD

parametros = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'exclude': 'current,minutely,daily,alerts',
    'appid': API_KEY_CONFIG
}

URI = 'https://api.openweathermap.org/data/2.5/onecall'
response = requests.get(URI, params=parametros)
text = response.json()
weather_slice = text['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
   condition_code = hour_data['weather'][0]['id']
   if int(condition_code) < 700:
        print(condition_code)
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=EMAIL_TO,
            msg=f"Hoje esta chovendo muito! {will_rain}"
        )
