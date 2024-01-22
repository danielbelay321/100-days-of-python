import requests
import os
from twilio.rest import Client


account_sid = "AC4ca44b29a4185cdca4c006d31f8765c1"
auth_token = "d406dee101c1691d3a37a05603f0c8a8"


API_key= "7481580853971b6038e3450027157893",
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


