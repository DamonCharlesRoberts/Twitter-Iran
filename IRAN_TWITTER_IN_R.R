#install.packages("rtweet")
#install.packages("remotes")
#install.packages("httpuv")
#install.packages("twitteR")
library(twitteR)
library(remotes)
library(rtweet)
library(httpuv)
library(tm)
api_key <- "YOUR_API_KEY_HERE"
api_secret <- "YOUR_API_SECRET_HERE"
access_token <- "YOUR_ACCESS_TOKEN_HERE"
access_secret <- "YOUR_ACCESS_TOKEN_SECRET_HERE"
token <- create_token(
  app = "Gender_War",
  consumer_key = api_key,
  consumer_secret = api_secret,
  access_token = access_token,
  access_secret = access_secret
)
Iran_tweet <- search_tweets(q = "Iran", n = 5000, langs = "en", include_rts = FALSE)
iran_tweet <- search_tweets(q = "iran", n = 5000, langs = "en", include_rts = FALSE)
#build a corpus
Iran_tweet_corpus <- Corpus(VectorSource(Iran_tweet$text))
Iran_tweet_corpus <- tm_map(Iran_tweet_corpus, content_transformer(tolower))
iran_tweet_corpus <- Corpus(VectorSource(iran_tweet$text))
iran_tweet_corpus <- tm_map(iran_tweet_corpus, content_transformer(tolower))
#stream Iran tweets for the next few weeks
iran_stream <- stream_tweets("Iran, iran, #iran", 
                             timeout = 60*60*24*7,
                             file_name = "irantweets.json",
                             parse = FALSE)
iran_stream_df = parse_stream("irantweets.json")