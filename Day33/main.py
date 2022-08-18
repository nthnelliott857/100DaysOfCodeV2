import requests
from datetime import datetime
LAT = 47.419958
LNG = -120.341966

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
# print(iss_position)


my_lat_and_long = "47.419958,-120.341966"
parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)
sunrise = data["results"]["sunrise"]
print(sunrise)
print(sunrise.split("T")[1].split(":")[0])
sunset = data["results"]["sunset"]
print(sunset)
print(sunset.split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)
time_now = datetime.now()
print(time_now.hour)