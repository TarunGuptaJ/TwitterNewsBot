import tweepy
import apikeyconstants
import requests
import random

CONSUMER_KEY = apikeyconstants.CONSUMER_KEY
CONSUMER_SECRET = apikeyconstants.CONSUMER_SECRET
ACCESS_KEY = apikeyconstants.ACCESS_KEY
ACCESS_SECRET = apikeyconstants.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

FILENAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 

# 1272502525892026368

def construct_url_api(mention,topic):
    url = 'http://newsapi.org/v2/top-headlines?'
    url = url + 'q=' + str(topic).lower() + '&'
    url = url + 'language=en&'
    date = mention.created_at
    datestr = str(date.year)+'-'+str(date.month)+'-'+str(date.day)
    url = url + 'from=' + str(datestr) + '&'
    url = url + 'sortBy=popularity&'
    url = url + 'apiKey='+str(apikeyconstants.NewsApiKeyMine)
    return url
    
def getinfo(url,mention):
    lenofat = len(str(mention.user.screen_name))+3
    response = requests.get(url).json()
    totalarticles = len(response['articles'])
    if(totalarticles == 0):
        return 'Sorry, There seem to be no articles for the requested topic'

    else:
        # Tweet Size is the main constraint
        # Iterate through them and find the first best matching 

def construct_tweet(mention,text):
    tweet = '@' + mention.user.screen_name + ' '


def onloop(FILENAME):
    last_seen_id = retrieve_last_seen_id(FILENAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(mention.created_at)
        print(str(mention.id) + " " + mention.full_text)
        
        textlist = list((mention.full_text).split())
        print(textlist)
        topic = textlist[1]
        print(topic)
        print(construct_url_api(mention,topic))

        last_seen_id = mention.id
        store_last_seen_id(last_seen_id,FILENAME)
        print('Responding back')
        api.update_status('@' + mention.user.screen_name + ' ' + 
            'Test reply from bot, Yayy!',mention.id)

onloop(FILENAME)