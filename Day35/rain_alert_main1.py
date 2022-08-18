import requests
from datetime import datetime
from twilio.rest import Client

account_sid = ""
auth_token = ""


api_key = ""
OWM_EndPoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 47.423458,
    "lon": -120.310349,
    "appid": "",
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_EndPoint, params=parameters)
response.raise_for_status()

weather_data = response.json()


time_now = datetime.now()
hour_now = time_now.hour

next_twelve_hours_data = weather_data["hourly"][hour_now:hour_now + 13:1]
next_twelve_hours_codes = [next_twelve_hours_data[i]["weather"][0]["id"] for i in range(0, len(next_twelve_hours_data))]


will_rain = False

for code in next_twelve_hours_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today in Sedro-Woolley, WA. Bring an umbrella!",
        from_='+19124556582',
        to='+15096680216'
    )
    print(message.status)

