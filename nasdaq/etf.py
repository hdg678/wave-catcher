import yfinance as yf
import datetime
from yahoo_fin.stock_info import *

class ETF:
    def __init__(self, ticker):
        self.ticker = ticker
        self.averageVolume = yf.Ticker(ticker).info['averageVolume']
        self.averageVolumeTenDays = yf.Ticker(ticker).info['averageVolume10days']
        self.regularMarketVolume = yf.Ticker(ticker).info['regularMarketVolume']
        self.recommendations = yf.Ticker(ticker).recommendations
        self.options =  yf.Ticker(ticker).options
        self.fiftyTwoWeekHigh = yf.Ticker(ticker).info['fiftyTwoWeekHigh']
        self.fiftyTwoWeekLow = yf.Ticker(ticker).info['fiftyTwoWeekLow']
        self.regularMarketDayHigh = yf.Ticker(ticker).info['regularMarketDayHigh']
        self.regularMarketDayLow = yf.Ticker(ticker).info['regularMarketDayLow']
        self.preMarketPrice = yf.Ticker(ticker).info['preMarketPrice']
        self.regularMarketPrice = yf.Ticker(ticker).info['regularMarketPrice']
        self.previousClose = yf.Ticker(ticker).info['previousClose']
        self.regularMarketOpen = yf.Ticker(ticker).info['regularMarketOpen']
        self.preMarketPercent = round(yf.Ticker(ticker).info['preMarketPrice'] / yf.Ticker(ticker).info['previousClose'],2)