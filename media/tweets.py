import tweepy
from textblob import TextBlob
import requests



consumer_key = 's702kE4uvRF2KH7b48eDC6hoc'
consumer_secret = 'vn0GGKnZhMnnfAbm39KLsVRR0igKz5H9TILoM9HE37R30vcQX8'
bear = 'AAAAAAAAAAAAAAAAAAAAAHdyYQEAAAAA9ZJ89Y8juO4ttrbTZKF0gdWU7yI%3D1DMycgnI4qqeSxnCBEwBwCvtJRwZi7z1nZ9NZwJfPY3jnD6e9K'
access_token = '207211654-qW2SGxOA498SmRFsK3FnIfSBepp1Of6XTnddjpsw'
access_token_secret = 'ULMgADVPvhMnFW9arPLDEpKKwCR7eNMlX9RCgHAC7lBvp'

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

search_terms = 'market outlook'
tweet_count = 200

tweets = tweepy.Cursor(api.search_tweets, q=search_terms, lang='en').items(tweet_count)

overall_polarity = 0
positive_polarity = 0
neutral_polarity = 0
negative_polarity = 0

for tweet in tweets:
    cleaned_up_text = tweet.text.replace('RT', '')
    if cleaned_up_text.startswith(' @'):
        position = cleaned_up_text.index(':')
        cleaned_up_text = cleaned_up_text[position + 2:]
    if cleaned_up_text.startswith('@'):
        position = cleaned_up_text.index(' ')
        cleaned_up_text = cleaned_up_text[position + 2:]

    analysis = TextBlob(cleaned_up_text)
    overall_polarity += analysis.polarity

    if analysis.polarity > 0.00:
        positive_polarity += 1
    elif analysis.polarity < 0.00:
        negative_polarity += 1
    elif analysis.polarity == 0.00:
        neutral_polarity += 1