import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
#percentage =

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "AC92b7d82fd44be3edb7e4ad6c8383d162"
auth_token = "4285b1a12a6fc45567ec055552bcc6cc"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "7R5F2EXY3YDPP5I9"
}

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_response_info = stock_response.json()
stock_data = stock_response_info['Time Series (Daily)']
#print(stock_data)
#print(stock_data['Time Series (Daily)']['2022-02-07']['4. close'])
# for date in stock_data.keys():
#     print(date)
#     print(stock_data[date]["4. close"])
closing_prices = {date: stock_data[date]["4. close"] for date in stock_data}
dates = [date for date in closing_prices]
#close_today = closing_prices.keys()[0]
yesterday_close = closing_prices[dates[0]]
day_before_yesterday_close = closing_prices[dates[1]]

#print(closing_prices)

#yesterdays_close =
#TODO 2. - Get the day before yesterday's closing stock price


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
print(closing_prices)

difference = abs(float(yesterday_close) - float(day_before_yesterday_close))
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage = 100*(difference/float(yesterday_close))

#print(percentage - 1)

#print(percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": "9a13a24c1393435f903b77eea9c73265"
}


# for article in news_request_data["articles"]:
#     print(article)
#print(news_request_data)

#print(first_three_articles)



    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#if percentage > 5:
news_request = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_request.raise_for_status()
news_request_data = news_request.json()
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
first_three_articles = [article for article in news_request_data["articles"][0:3]]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# for article in first_three_articles:
#     print(article["title"])
#     print(article["description"])
first_three_articles_basic_info = [{"title": article["title"] , "description": article["description"]} for article in first_three_articles]
print(first_three_articles_basic_info)
#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(account_sid, auth_token)

for i in range(0, len(first_three_articles_basic_info)):
    article = first_three_articles_basic_info[i]
    message = client.messages \
        .create(
        body=f"{STOCK_NAME}"
             f"Headline: {article}"
             f"Brief: {message}",
        from_='+19124556582',
        to='+15096680216'
    )
    print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

