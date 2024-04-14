import pandas as pd
import smtplib
import datetime as dt
import random


my_email = "random@gmail.com"
password = "qslo cbfc xsnv guld"


now = dt.datetime.now()
month = now.month
day = now.day

data = pd.read_csv("Day 32/birthdays.csv")

today_birthdays = data[(data['month'] == month) & (data['day'] == day)]

if not today_birthdays.empty:

    letter = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    
    with open(f"Day 32/letter_templates/{letter}") as base_letter:
        contents = base_letter.read()
    
    for index, person in today_birthdays.iterrows():
        personalized = contents.replace("[NAME]", person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="another_random@gmail.com", 
            msg=f"Subject:Happy Birthday\n\n{personalized}"
        )
