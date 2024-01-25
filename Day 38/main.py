import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 184
AGE = 30

APP_ID = "4dcc663e"
# API_KEY = "80e549e0509a698f08f090dd7225626d"
API_KEY = os.environ["ENV_NIX_API_KEY"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/b4c965dac74a95681df01c9b2fb73fc5/workout/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    header = {
        "Content-type":"application/json",
        "Authorization":"Bearer veystrongbearerauthentication required"
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=headers)

    print(sheet_response.text)