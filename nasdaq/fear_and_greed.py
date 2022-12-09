import tweepy
from textblob import TextBlob
# import requests
import yfinance as yf
import fear_and_greed

vixOpen = yf.Ticker('^VIX').info['open']
vixClose = yf.Ticker('^VIX').info['regularMarketPreviousClose']
fearAndGreedRating = fear_and_greed.get()[1]
fearAndGreedScore = fear_and_greed.get()[0]
# odd lot
# nyse bullish 
# high/low indicator
# NYSE 200-day Moving Average
# buffet index (gdp/value of market or maybe the converse)

# print(vixOpen)
# print(vixClose)
# print(fearAndGreedRating)
# print(fearAndGreedScore)