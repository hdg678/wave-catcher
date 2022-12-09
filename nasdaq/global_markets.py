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


# print(ftse.percentageChange)
# print(nikkei.percentageChange)
# print(sse.percentageChange)
# print(hsi.percentageChange)
# print(gdaxi.percentageChange)


# print((float(yf.Ticker('^N225').info['open']) - float(yf.Ticker('^N225').info['regularMarketPreviousClose'])) / float(yf.Ticker('^N225').info['regularMarketPreviousClose']))