import requests
from datetime import datetime

from config import APP_ID, APP_KEY, YOUR_AGE, YOUR_GENDER, YOUR_HEIGHT, YOUR_WEIGHT, AUTH

#--->input_user---<

exercise_text = input("Tell me which exercises you did: ")

#--->endpoints<---

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = 'https://api.sheety.co/2ed037d0510709194f08a83f71d960dd/myWorkoutsLuciano/workouts'

#--->exercise<---

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key':APP_KEY
}

parameters_ = {
 "query":exercise_text,
 "gender":YOUR_GENDER,
 "weight_kg":YOUR_WEIGHT,
 "height_cm":YOUR_HEIGHT,
 "age":YOUR_AGE
}

response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=parameters_)
result = response.json()

#--->sheety<---

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_headers = {
"Authorization": AUTH
}

for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheety_response = requests.post(url=sheet_endpoint, headers=sheety_headers ,json=sheet_inputs)
    print(sheety_response.status_code)
    print(sheety_response.text)
