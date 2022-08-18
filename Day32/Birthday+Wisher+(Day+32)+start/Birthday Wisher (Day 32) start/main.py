import smtplib
import datetime as dt
import random

quotes = []

now = dt.datetime.now()
day = now.weekday()


days_of_the_week = { 0: "Monday", 1: "Tuesday",2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()


my_email = "natedoggg109312@gmail.com"
my_password = "HorseDartNinjaPilot#6"
yahoo_account = "natedoggg109312@yahoo.com"


if day == 6:
    #print(f"Subject: Motivational {days_of_the_week[day]}\n\n{random.choice(quotes)}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=yahoo_account,
            msg=f"Subject: Motivational {days_of_the_week[day]}\n\n{random.choice(quotes)}"
        )



