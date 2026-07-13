import requests
from twilio.rest import Client
OWM_ENDPOINT ="https://api.openweathermap.org/data2.5/forecast"
api_key = "78293045hjkjh403"

#twilio
account_id ="yuio09890u890989"
auth_token = "7890-0987uioiughjkjh"

weather_params = {
  "lat":51.1234,
  "lon":23.324546,
  "appid":api_key,
  "cnt":4,
}

response = requests.get (OWM_ENDPOINT,weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain =False
for hour_data in weather_data["list"]:
  condition_code=hour_data["weather"][0]["id"]
  if int(condition_code)<700:
      will_rain=True
      
if will_rain:
   client =Client(account_id,auth_token)
   message = client.messages \
      .create(
      body = "Join Earth Mightest hereos",
      from = "+1234567",
      to="+123456576876544"
    )
   
   print(message.status)
