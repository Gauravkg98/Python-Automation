import requests
import datetime
MY_Lat = 890.09
MY_lng =98.790


parameter={"lat":MY_Lat,
"lng" :MY_lng,
"formatted":0,
}


response = requests.get("https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)


#time_now = datetime.now()
