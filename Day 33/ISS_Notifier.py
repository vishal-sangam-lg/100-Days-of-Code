import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "aditirao292@gmail.com"
MY_PASSWORD = "CD9A4DEA1D457B9C39EDA1CC8F2271F24C18"

MY_LAT = 12.295810
MY_LONG = 76.639381


def is_iss_overhead():
    # Getting the co-ordinates of International space station(ISS) satellite
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the iss position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    # Getting the sunrise and sunset of my location
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.elasticemail.com", 2525) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="lgvishalsangam@gmail.com",
                                msg=f"Subject: ISS notification\n\nLook up! ISS is "
                                    f"above you")
        break
