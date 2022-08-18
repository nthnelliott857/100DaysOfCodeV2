import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 177.8
AGE = 26

APP_ID = ""
API_KEY = ""

# APP_ID = os.environ[""]
# API_KEY = os.environ[""]

exercise_text = input("Which exercises did you do? ")

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_parameters,
                                 headers=headers)
exercise_result = exercise_response.json()



sheety_url = "https://api.sheety.co/f52b8e4843b40bf130666f82709b14cc/myWorkouts/workouts"
sheety_headers = {
    "Authorization": "Basic TmF0aGFuOlBhc3N3b3Jk"
}

today = datetime.now()

# print(exercise_result)
# print(exercise_result["exercises"][0]["duration_min"])
# print(exercise_result["exercises"][0]['name'])
# print(exercise_result["exercises"][0]['name'])
# print(exercise_result["exercises"][0]['nf_calories'])

sheet_inputs = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": exercise_result['exercises'][0]["duration_min"],
        "exercise": exercise_result["exercises"][0]['name'],
        "duration": exercise_result["exercises"][0]["duration_min"],
        "calories": exercise_result["exercises"][0]['nf_calories'],
    }
}



sheety_request = requests.post(url=sheety_url, headers=sheety_headers, json=sheet_inputs)
print(sheety_request.text)
