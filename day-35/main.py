import requests
from config import API_KEY_CONFIG, LATITUDE, LONGITUDE, PASSWORD, EMAIL_FROM, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
import smtplib
import os
from twilio.rest import Client


MY_EMAIL = EMAIL_FROM
MY_PASSWORD = PASSWORD

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

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

will_rain = True

# for hour_data in weather_slice:
#    condition_code = hour_data['weather'][0]['id']
#    if int(condition_code) < 700:
#         print(condition_code)
#         will_rain = True

if will_rain:
    message = client.messages \
                    .create(
                        body="Olá amor, vamos mudar para a europa",
                        from_='whatsapp:+5521969897976',
                        to='whatsapp:+5521971135071'
                    )
