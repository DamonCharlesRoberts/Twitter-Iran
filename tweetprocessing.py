#--------------------------
#Run Twitter-Genderd Reactions....py file first
#-------------------------
#pip install tweet-preprocessor
import preprocessor as p
import tweetpull
#Cleaning the tweet
p.clean(tweetpull.iran_tweets)