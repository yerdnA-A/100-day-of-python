import datetime as dt
import smtplib
import random

my_email = "andreycricco@gmail.com"
password = "qslo cbfc xsnv guld"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("Day 32/Birthday Wisher/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="andreyfutfifa@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )