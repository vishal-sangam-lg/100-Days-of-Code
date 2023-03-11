import requests
from datetime import datetime

# Getting data from user. Posting to nutritionix endpoint for NLP processing
GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 175
AGE = 21

NUTRITIONIX_APP_ID = "APPID"
NUTRITIONIX_API_KEY = "APIKEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

##########################################################################

# Saving data to sheets using sheety
sheet_endpoint = "YOUR_SHEET_ENDPOINT"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # No Authentication
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # # Basic Authentication
    # SHEETY_USERNAME = "YOUR_USERNAME"
    # SHEETY_PASSWORD = "YOUR_PASSWORD"
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         SHEETY_USERNAME,
    #         SHEETY_PASSWORD,
    #     )
    # )

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": "Bearer YOUR_SECRET_KEY"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
