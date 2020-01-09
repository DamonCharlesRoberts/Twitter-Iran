import key
import tweepy
import sys
from tweepy import OAuthHandler
from textblob import TextBlob
import preprocessor as p
class TwitterClient(tweepy.StreamListener):
   def __init__(self, api, sentiment_dict, topic):
       self.sentiment_dict = sentiment_dict
       self.tweet_count = 0
       self.topic = topic

       p.set_options(p.OPT.URL, p.OPT.RESERVED)
       super().__init__(api)

    def on_statuses(self,status):
        try:
            tweet_text = status.extended_tweet.full_text
        except:
            tweet_text = status.text
        tweet_text = p.clean(tweet_text)
        if self.topic.lower() not in tweet_text.lower():
            return
        blob = TextBlob(tweet_text)
        if blob.sentiment.polarity > 0:
            sentiment = '+'
            self.sentiment_dict['positive'] +=1
        elif blob.sentiment.polarity == 0:
            sentiment = ''
            self.sentiment_dict['neutral'] +=1
        else:
            sentiment = '_'
            self.sentiment_dict['negative'] +=1
        print(f'{sentiment}{status.user.screen_name}: {tweet_text}\n')
    def main():
        auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
        auth.set_access_token(key.access_token,key.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        search_key = sys.argv[1]
        sentiment_dict = {'positive': 0, 'neutral': 0, 'negative': 0}
        sentiment_listener = SentimentListener(api, sentiment_dict, search_key)
        stream = tweepy.Stream(auth=api.auth, listener=sentiment_listener)
        stream.filter(track=[search_key], languages=['en'], is_async=False)
        print(f'Tweet Sentiment for "{search_key}"')
        print('Positive: ', sentiment_dict['positive '])
        print('Neutral:', sentiment_dict['neautral '])
        print('Negative:', sentiment_dict['negative '])
if _name_ == '_main_':
    main()
