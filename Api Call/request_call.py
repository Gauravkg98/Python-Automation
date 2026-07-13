import requests
import datetime

MY_Lat = 890.09
MY_lng =98.790

def is_iss_overhead():
  response = requests.get(url = "http://api.open-notify.org/iss-now.json")

  #return staus code
  print(response.status_code)

  #to raise exception for all the hhtp request no nee to create exception manually for all exception raise
  response.raise_for_status()

  #getting the data from api call
  data=response.json()

  longitude = float(data["iss_position"]["longitude"])
  latitude = float(data["iss_poisition"]["latitude"])
  iss_position = (longitude,latitude)

  print(iss_position)


  '''if response.status_code==404:
    raise Exception("The Resource Does npt exist")

  if response.status_code==401:
    raise Exception("The Resource is showing error")
    '''
  if MY_Lat <= longitude <=MY_Lat+5 and MY_lng-5< longitude <=MY_lng:
    return True;

def is_night():
    
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
  time_now = datetime.now().hour
  if time_now>= sunset or time_now<= sunrise:
    return True

  