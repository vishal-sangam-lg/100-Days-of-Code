import requests
from twilio.rest import Client

MY_LAT = 12.295810
MY_LONG = 76.639381
API_KEY = "OPEN_WEATHER_API_KEY"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC_SID"
auth_token = "AUTH_TOKEN"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_="FROM_NUMBER",
        to="TO_NUMBER"
    )
    print(message.status)
