from apikeyconstants import *
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key = NewsApiKeyMine)

# print(NewsApiKeyMine)
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',sources='bbc-news,the-verge',language='en').text()
print(top_headlines)
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',sources='bbc-news,the-verge',domains='bbc.co.uk,techcrunch.com',from_param='2017-12-01',to='2017-12-12',language='en',sort_by='relevancy',page=2).json()
print(all_articles)

# /v2/sources
sources = newsapi.get_sources()
print(sources)