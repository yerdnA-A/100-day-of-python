import requests
from datetime import datetime
import smtplib

MY_LAT = 48.487872
MY_LONG = 162.868126

my_email = "random@gmail.com"
my_password = "qslo cbfc xsnv guld"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    print("Its equal")
    print(f"Me Lat: {MY_LAT} = Iss Lat: {iss_latitude}\nMe Long: {MY_LONG} = Iss Long: {iss_longitude}")
    its_equal = True
else:
    print("Not is equal")
    print(f"Me Lat: {MY_LAT} = Iss Lat: {iss_latitude}\nMe Long: {MY_LONG} = Iss Long: {iss_longitude}")
    its_equal = False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(sunrise)
print(time_now.hour)

if time_now.hour >= sunrise:
    print("Its night")
    its_night = True
else:
    print("Its Morning")
    its_night = False

if its_night == True and its_equal == True:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="another@gmail.com",
            msg="Subject:Look At Up!\n\nThe ISS passing over you"
        )
    print("Email Send")
else:
    print("It's not the time now")
