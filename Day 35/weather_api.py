import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "42e0ff82d7e4f6f2b750b24d2ba6953d"

parameters = {
    "lat" : -23.550520,
    "lon" : -46.633308,
    "cnt" : 4, 
    "appid" : api_key,
}


response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")