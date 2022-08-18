##################### Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt



#TODO: 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.


data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient="records")
birthdays_dict = {(person["month"], person["day"]):(person["name"], person["email"]) for person in birthdays_dict}
print(birthdays_dict)
now = dt.datetime.now()
today_day = now.day
today_month = now.month





#TODO:2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }



#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:


if (today_month, today_day) in birthdays_dict:
    letters = []


    with open(r"letter_templates\letter_1.txt", "r") as letter_1:
        letters.append(letter_1.read())


    with open(r"letter_templates\letter_2.txt", "r") as letter_2:
        letters.append(letter_2.read())

    with open(r"letter_templates\letter_3.txt", "r") as letter_3:
        letters.append(letter_3.read())

    #print(letters)

    letter = random.choice(letters)
    #print(birthdays_dict[(today_month, today_day)][0])
    letter = letter.replace("[NAME]", f"{birthdays_dict[(today_month, today_day)][0]}")
    #print(letter)

    my_email = "natedoggg109312@gmail.com"
    my_password = "HorseDartNinjaPilot#6"
    yahoo_account = "natedoggg109312@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=yahoo_account,
            msg=f"Subject: Happy Birthday!\n\n{letter}"
        )







#TODO:3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

#TODO:4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



