import tweepy
import apikeyconstants

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

last_seen_id = retrieve_last_seen_id(FILENAME)
mentions = api.mentions_timeline(last_seen_id,tweet_mode = 'extended')
for mention in reversed(mentions):
    print(str(mention.id) + " " + mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id,FILENAME)
    print('Responding back')
    api.update_status('@' + mention.user.screen_name + ' ' + 
        'Test reply from bot, Yayy!',mention.id)