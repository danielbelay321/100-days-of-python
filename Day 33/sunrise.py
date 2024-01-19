import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    sunrise = int(response.json()['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(response.json()['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now > sunrise or time_now < sunset:
        return True

my_email = "danielbelay321@gmail.com"
password = "gipk shlz vypu pwsk"

if is_iss_overhead() or is_night():
    with smtplib.SMTP("smtp.gmail.com") as smtpdata:
        smtpdata.starttls()
        smtpdata.login(my_email,password)
        smtpdata.sendmail(from_addr=my_email,to_addrs=my_email,
                          msg="Subject:hello\n\nHow are you dani")