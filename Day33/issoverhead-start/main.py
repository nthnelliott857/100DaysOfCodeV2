import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.419958  # Your latitude
MY_LONG = -120.341966  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# iss_latitude = float(data["iss_position"]["latitude"])
# iss_longitude = float(data["iss_position"]["longitude"])


iss_latitude = 43
iss_longitude = -118


# Your position is within +5 or -5 degrees of the ISS position.

def iss_is_nearby(iss_lat, iss_long):
    if iss_lat >= 5 + MY_LAT or iss_long >= 5 + MY_LONG or iss_lat <= MY_LAT - 5 or iss_long <= MY_LONG - 5:  # if my latitude or longitude + 5 is greater than those of the ISS
        # and MY_LONG - 5 <= iss_long or MY_LONG + 5 >= MY_LONG
        return False
    #elif iss_lat <= MY_LAT - 5 or iss_long <= MY_LONG - 5:  # if my latitude or longitude + 5 is less than those of the ISS
        #return False
    else:
        return True

print(iss_is_nearby(iss_lat=iss_latitude, iss_long=iss_longitude))
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
# time_now = datetime.now()
# print(time_now)


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise_minutes = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
    sunset_minutes = int(data["results"]["sunset"].split("T")[1].split(":")[1])
    daylight_cycle = {"sunset_hour": sunset_hour, "sunset_minutes": sunset_minutes, "sunrise_hour": sunrise_hour,
                      "sunrise_minutes": sunrise_minutes}
    time_now = datetime.now()
    print(time_now)
    print(sunrise_hour)
    print(sunset_hour)

    pst_sunset = 8

    if sunrise_hour - 8 < time_now.hour < sunset_hour - 8:
        return False
    else:
        return True
    # print(data)
    # print(daylight_cycle)
    # time_now = datetime.now()
    # print(time_now)


# print(f"Subject: Alert: The ISS is approaching your location "
#                 f"and should be visible."
#                 f"\n\nISS Latitude: {iss_latitude}"
#                 f"\nISS Longitude: {iss_longitude}"
#                 f"\nYour Latitude: {MY_LAT}"
#                 f"\nYour Longitude: {MY_LONG}")

def send_email():
    if iss_is_nearby(iss_lat=iss_latitude, iss_long=iss_longitude) and is_dark():
        my_email = "natedoggg109312@gmail.com"
        my_password = "HorseDartNinjaPilot#6"
        yahoo_account = "nthnelliott857@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=yahoo_account,
                msg=f"Subject: Alert: The ISS is approaching your location "
                    f"and should be visible."
                    f"\n\nISS Latitude: {iss_latitude}"
                    f"\nISS Longitude: {iss_longitude}"
                    f"\nYour Latitude: {MY_LAT}"
                    f"\nYour Longitude: {MY_LONG}"
            )
    print(datetime.now())
    print(f"ISS Latitude: {iss_latitude}"
          f"\nISS Longitude: {iss_longitude}"
          f"\nYour Latitude: {MY_LAT}"
          f"\nYour Longitude: {MY_LONG}")
    time.sleep(60)
    send_email()


#send_email()
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
