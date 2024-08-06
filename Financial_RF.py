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
    return data['data']


def get_ticker_EOD(symbol: str, day: str):
    query_market = {'access_key': os.environ['API_KEY'],
                    'symbols': symbol}
    response = requests.get(f"http://api.marketstack.com/v1/eod/{day}",
                            params=query_market)

    return response.json()


def get_ticker_names(ticker_info: list):
    return [info['name'] for info in ticker_info]


def get_ticker_symbols(ticker_info: list):
    return [info['symbol'] for info in ticker_info]


def get_ticker_prices(ticker_info):
    return ticker_info['data'][0]['close']


def get_all_ticker_closed(day, tickerPrices_previous=None):
    ticker_list = get_ticker_info_file('ticker_info.json')
    all_tickers = get_ticker_symbols(ticker_list)
    if not tickerPrices_previous:
        ticker_prices = {}
    else:
        ticker_prices = tickerPrices_previous
    for ticker in all_tickers:
        ticker_info = get_ticker_EOD(ticker, day)
        price_close = get_ticker_prices(ticker_info)
        ticker_prices[ticker] = {'day': price_close}



get_ticker_info_file('ticker_info.json')
# print(get_ticker_EOD('MSFT', '2024-07-01'))
# data_test = {'pagination': {'limit': 100, 'offset': 0, 'count': 1, 'total': 1}, 'data': [{'open': 448.61, 'high': 457.37, 'low': 445.66, 'close': 456.73, 'volume': 17545940.0, 'adj_high': 457.37, 'adj_low': 445.66, 'adj_close': 456.73, 'adj_open': 448.66, 'adj_volume': 17662818.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2024-07-01T00:00:00+0000'}]}
#
# print(get_ticker_prices(data_test))
