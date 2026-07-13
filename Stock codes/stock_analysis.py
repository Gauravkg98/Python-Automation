import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPPOINT = "https://www.alphaavantage.co.query"
NEWS_ENDPOINT  ="https://newsapi.org/v2/everything"



NEWS_API_KEY = "fghyuio-098u"
STOCK_API_KEY = "yguhoipooihkg23145"


TWILIO_SID="yhujoipk00"
TWILIO_AUTH = "5w465789poijklhg"



stock_params={"function" :"TIME_SERIES_DAILY",
              "symbol": STOCK_NAME,
              "apikey":STOCK_API_KEY}

response = requests.get(STOCK_ENDPPOINT,params = stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yest_data = data_list[0]
yesterday_closingprice = yest_data["4. close"]
print(yesterday_closingprice)

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]


diff = abs(float(day_before_yesterday_data_closing_price)-float(day_before_yesterday_data_closing_price))

print(diff)

diff_prcnt = (diff/float(yesterday_closingprice))*100

if diff_prcnt> 5:
  print("Get News")
  news_params = {
    "apikey":NEWS_API_KEY,
    "qInTitle":STOCK_NAME,

  }
  news_response = requests.get(NEWS_ENDPOINT,params=news_params)
  news_data=news_response.json()
  articles = news_data["articles"]
  print(articles)

  selected_articles = articles[:3]
  print(selected_articles)

formatted_articles = [f"Headline:{article["title"]}. \nBreif:{article["description"]}" for article in selected_articles]


client = Client(TWILIO_SID,TWILIO_AUTH)

for article in formatted_articles:
  message = client.messages.create(

    body=articles,
    from_ ="+1234567",
    to="+12345675433"
  )
