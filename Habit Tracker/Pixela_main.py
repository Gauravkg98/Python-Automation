import requests
import datetime

pixela_endpoint="https://pixe.la/v1/users"
username="gk"
TOKEN="435367890[p]okljh"
GRAPH_ID = "graph1"
user_param = {

  "token" : "dfgyhujik;oi89",
  "username":"gk",
  "agreeTermsOfService":"yes",
  "notMinor":"yes"
  
  }

response =requests.post(url=pixela_endpoint,json=user_param)
#print(response.status_code)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config={
  "id":"graph1",
  "name":"Cycling Graph",
  "unit":"Km",
  "type":"float",
  "color":"ajisai",

}

header = {

  "X-USER-TOKEN":TOKEN,
}
response2 = requests.post(url = graph_endpoint,json=graph_config,headers=header)

print(response2)

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"


today = datetime(year=2026, month = 7, day =23)

pixel_data ={

"date":today.strftime("%Y%m%d"),
"quantity":"3.5",

}

response3=requests.post(url =pixel_creation_endpoint, json = pixel_data,headers = header)
#print(response3.text)

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
  "quanity":"4.5",
}

#response = requests.put(url =update_endpoint, json=new_pixel_data, headers=header)

#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers= header)
print(response.text)