from config import APP_ID, APP_KEY
import requests
from datetime import datetime

#--->endpoints<---

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = 'https://api.sheety.co/2ed037d0510709194f08a83f71d960dd/myWorkoutsLuciano/workouts'

#--->exercise<---

headers = {
    'x-app-id': APP_ID,
    'x-app-key':APP_KEY
}

parameters_ = {
 "query":"ran 3 miles and walk 5 minutes",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

response = requests.post(url=exercise_endpoint, headers=headers, json=parameters_)
result = response.json()

#--->sheety<---

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

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

    sheety_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheety_response.status_code)
    print(sheety_response.text)
