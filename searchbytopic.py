import requests
from apikeyconstants import *

url = ('http://newsapi.org/v2/top-headlines?'
    'q=Apple&'
    'language=en&'
    'from=2020-05-14&'
    'sortBy=popularity&'
    'apiKey='+str(NewsApiKeyMine))
response = requests.get(url).json()

print(response)