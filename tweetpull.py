#-----------------------------
#    Twitter- Gendered Reaction to International Conflict
#-----------------------------

#Set up
    #pip install tweepy ==3.7
    #conda install -c conda-forge geopy

#Authentication with Tweepy
import tweepy
import key
import pandas as pd
auth = tweepy.OAuthHandler(key.consumer_key,
                          key.consumer_secret)
auth.set_access_token(key.access_token,
                     key.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Querying the Tweets
from tweetutilities import print_tweets
query = 'Iran OR iran'
max_tweets = 1000
iran_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
iran_tweets =[]
last_id = -1
while len(iran_tweets) < max_tweets:
    count = max_tweets - len(iran_tweets)
    try:
        newIran_tweets = api.search(q = query, count = count, max_id = str(last_id - 1))
        if not newIran_tweets:
            break
        iran_tweets.extend(newIran_tweets)
        last_id = newIran_tweets[-1].id
    except tweepy.TweepError as e:
        break 
df = pd.DataFrame(data = iran_tweets)