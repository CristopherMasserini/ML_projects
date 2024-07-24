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


# os.environ['API_KEY']
query = {'lat':'45', 'lon':'180'}
response = requests.get("http://api.open-notify.org/astros.json", params=query)
# print(response.content)
# print(response.text)
print(response.json())


