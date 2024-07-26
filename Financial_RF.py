"""
Ideas:
- create a random forest model to model financial data
- get data with columns like: 10 year, 5 year, 1 year, 6 months, 3 months, 1 month, 1 week, sector, stock or fund, etc.
- get from sometime previous and have to +1month, +1 year, etc. to see how stock did after
- see if model can predict future trend from previous


Using Marketstack API
"""
import os
import requests
import json


def get_ticker_info_request():
    query_market = {'access_key': os.environ['API_KEY']}
    response = requests.get("http://api.marketstack.com/v1/tickers",
                            params=query_market)

    return response.json()


def get_ticker_info_file(filename: str):
    with open(f"{filename}", "r") as file:
        data = json.load(file)
    print(data['data'])


def get_ticker_EOD(symbol: str, day: str):
    query_market = {'access_key': os.environ['API_KEY'],
                    'symbols': symbol}
    response = requests.get(f"http://api.marketstack.com/v1/eod/{day}",
                            params=query_market)

    return response.json()


get_ticker_info_file('ticker_info.json')
