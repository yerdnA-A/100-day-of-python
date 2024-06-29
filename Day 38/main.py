import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""

nutri_endpoint = "https://trackapi.nutritionix.com"

sheet_url = ""

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutri_params = {
    "query": input("Teell me wich exercises you did: "),
}

response_nutri = requests.post(url=nutri_endpoint, json=nutri_params, headers=headers)

nutri_data = response_nutri.json()

today = datetime.now()

for exercise in nutri_data["exercises"]:
    sheet_params = {
        "página1": {
            "date": today.strftime('%d/%m/%Y'),
            "time": today.strftime('%H:%M:%S'),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

sheet_response = requests.post(url=sheet_url, json=sheet_params)

print(sheet_response.text)