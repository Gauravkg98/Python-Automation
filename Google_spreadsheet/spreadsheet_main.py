import requests
import datetime
GENDER = "male"
WEIGHT = 70
AGE = 30
HEIGHT =150

APP_ID= "app_284928b325c84939a18626e2"
API_KEY= "nix_live_ve7spkwUfABhmultA8p7vi6JARkAjCXw"

BASE_URL_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_END_POINT = "https://api.sheety.co/aed8ce861086afbe0ec4feb157da6040/myWorkouts/workouts"

exercise_text=input("Tell me which exercise you did: ")

header={
"x-app-id":APP_ID,
"x-app-key":API_KEY,

}

param={"query":exercise_text,
        "weight_kg":WEIGHT,
        "height_cm":HEIGHT,
        "age":AGE,
        "gender":GENDER}

response = requests.post(BASE_URL_ENDPOINT,json=param,headers=header)
result=response.json()
print("rtyuio :   ",result)

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
  sheet_inputs ={
    "workout":{
      "date":today_date,
      "time":now_time,
      "exercise":exercise["name"].title(),
      "duration":exercise["duration_min"],
      "calories":exercise["nf_calories"]
    }
  }
  #sheety authenticataion
  bearer_auth={"Authorization":"Basic R2swMDI1OjEyMzQ1Njc4"}  

  sheet_response = requests.post(SHEETY_END_POINT, json=sheet_inputs,headers=bearer_auth)
  print(sheet_response.text)