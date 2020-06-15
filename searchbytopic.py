import requests
import random
from outsideconstants import *

url = ('http://newsapi.org/v2/top-headlines?'
    'q=apple&'
    'language=en&'
    'from=2020-05-15&'
    'sortBy=popularity&'
    'apiKey='+str(NewsApiKeyMine))
response = requests.get(url).json()

totalarticles = len(response['articles'])
chosearticle = random.randint(0,totalarticles-1)

for i in range(totalarticles):
    print(i)
    print(response['articles'][i])
    print(response['articles'][i]['description'])
    print(len(response['articles'][i]['description']))
    print()
    # Len of >
# print(chosearticle)
# print(response['articles'][chosearticle]['description'])

# print(0)
# print(response['articles'][0]['description'])

# print(totalarticles-1)
# print(response['articles'][totalarticles-1]['description'])