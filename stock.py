import requests
import json
symbol = input("Stock symbol: ").upper()
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=YOUR_KEY_HERE"
response = requests.get(url)
total = 0
try:
    data = response.json()
    daily = data["Time Series (Daily)"]
    recent_dates = list(daily.keys())[:50]
    for date in recent_dates:
        day_data = daily[date]
        price = day_data["4. close"]
        total += float(price)
    moving_average = total / len(recent_dates)
    print(f"The moving average is: {moving_average}.")
except requests.RequestException:
    print("Error. Please try again.")
