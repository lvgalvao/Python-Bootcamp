from config import API_KEY, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, NEWSAPI, TWILIO_FROM, TWILIO_TO
import requests
from twilio.rest import Client
from newsapi import NewsApiClient
from datetime import datetime, timedelta

## CONTANTS
URI = 'https://www.alphavantage.co/query?' #URI TO GET THE STOCK PRICE
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

parametros = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': API_KEY
}


newsapi = NewsApiClient(api_key=NEWSAPI)


## STEP 1: Use https://www.alphavantage.co
# Get the STOCK price
response = requests.get(URI, params=parametros)
dict = response.json()

last_data = dict["Meta Data"]["3. Last Refreshed"]
last_data_date = datetime.strptime(last_data, '%Y-%m-%d').date()
last_day = last_data_date - timedelta(days=1)
open_price = dict["Time Series (Daily)"][last_data]['1. open']
close_price = dict["Time Series (Daily)"][last_data]['4. close']
variation = (float(close_price)/float(open_price))-1
variation_format = "{:.0%}".format(variation)

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

all_articles = newsapi.get_everything(q='bitcoin',
                                        sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        from_param=last_data_date,
                                        to=last_day,
                                        language='en',
                                        sort_by='relevancy',
                                        page=1)
    
n_article = all_articles['totalResults']


titles = []
descriptions = [] 
if n_article >= 1:
    for artticle in range(0, all_articles['totalResults']):
        title = (all_articles['articles'][artticle]['title'])
        description = (all_articles['articles'][artticle]['description'])
        titles.append(title)
        descriptions.append(description)
else:
    titles = "Sem artigos hoje"
    descriptions = "Sem artigos hoje"

if variation >=0:
    simbol = '🔺'
else:
    simbol = '🔻'
if variation < -0.05 or variation > 0.05:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    n_article = all_articles['totalResults']
    titles = []
    descriptions = [] 
    if n_article >= 1:
        for artticle in range(0, all_articles['totalResults']):
            title = (all_articles['articles'][artticle]['title'])
            description = (all_articles['articles'][artticle]['description'])
            titles.append(title)
            descriptions.append(description)
    else:
        titles = "Sem artigos hoje"
        descriptions = "Sem artigos hoje"
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    message = client.messages \
                    .create(
                        body=f"""Ação: {STOCK}\nvariação: {simbol}{variation_format}\nnoticias: {titles}\nbrief: {descriptions}""",
                        from_=TWILIO_FROM,
                        to=TWILIO_TO
                    )
