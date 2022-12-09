import sentiment as st
import json
import yfinance as yf
import pandas as pd
import csv

class Market:
    def __init__(self, ticker):
        self.ticker = ticker
        self.regularMarketPreviousClose = float(yf.Ticker(ticker).info['regularMarketPreviousClose'])
        self.open = float(yf.Ticker(ticker).info['open'])
        self.regularMarketPrice = float(yf.Ticker(ticker).info['regularMarketPrice'])
        self.percentageChange = round((float(yf.Ticker(ticker).info['open']) - float(yf.Ticker(ticker).info['regularMarketPreviousClose'])) / float(yf.Ticker(ticker).info['regularMarketPreviousClose']),4)
    
        
        
nikkei = Market("^N225")
ftse = Market('^FTSE')
hsi = Market('^HSI')
sse = Market('000001.SS')
gdaxi = Market('^GDAXI')


# fm.ftse.percentageChange
# fm.nikkei.percentageChange
# fm.sse.percentageChange
# fm.hsi.percentageChange
# fm.gdaxi.percentageChange
# st.fearAndGreedRating
# st.fearAndGreedScore
stats = {
    "fngscore": round(st.fearAndGreedScore,2)
}


def recommend_nasdaq():
    recommendation = ''
# the two most conistent indicators per my half hearted testing are the direction of the NIKKEI, FTSE and the cnn fear and greed index
    with open('stats.json', 'r') as openfile:
        json_object = json.load(openfile)
    old_fngscore = json_object['fngscore']
    
    if (st.fearAndGreedScore > old_fngscore) and (ftse.percentageChange >= 0) and (nikkei.percentageChange >= 0):
        recommendation = 'TQQQ'
    elif (st.fearAndGreedScore < old_fngscore) and (ftse.percentageChange <= 0) and (nikkei.percentageChange <= 0):
        recommendation = 'SQQQ'
    else:
        recommendation = 'Neither'
    return recommendation

    
def update_stats():
    with open("stats.json", "w") as outfile:
        json.dump(stats, outfile)
    return



# if (st.fearAndGreedScore < old_fngscore) and (ftse.percentageChange <= 0) and (nikkei.percentageChange <= 0):
#     print('SQQQ')

print(recommend_nasdaq())