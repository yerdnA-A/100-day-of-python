import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "julio"

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