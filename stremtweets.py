#---------------------
#  Streaming the API
#--------------------
#Initiate the Process
import tweepy
import key
auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#tweet listner
from tweetlisten import TweetListener
tweet_listener = TweetListener(api)
iran_stream = tweepy.Stream(auth = api.auth, listener = tweet_listener)
iran_stream.filter(track=['Iran or iran'], is_async=True)