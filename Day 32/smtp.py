import smtplib

my_email = "random@gmail.com"
password = "qslo cbfc xsnv guld"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="another_random@gmail.com", 
        msg="Subject:Hello\n\nContents"
    )