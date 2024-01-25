import requests
import os
from twilio.rest import Client


account_sid = "##############################"
auth_token = "###############################"


API_key= "#######################################",
parameters = {
"lat":42.231361,
"lon":-8.712430,
"cnt":7,
"appid":API_key,
"exclude":"current,minutly,daily"

}




response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"][:12]

will_rain = False
for hourly_data in weather_data:
    condition_code = hourly_data["weather"][0]["id"]

    if int(condition_code) > 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hello daniel, it's going to rain today, don't forget to bring unumbrella! ☂️.",
        from_='+15108582656',
        to='+251930802769'
    )

    print(message.status)


