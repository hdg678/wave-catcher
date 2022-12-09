import yfinance as yf
import datetime
from yahoo_fin.stock_info import *
# qqq = yf.Ticker(stock).info
# inflation rate
# usd strength 
#todo
# get average price of the highest 5 in a row volumne options.  So whatever block of 5 options has the highest volumne.  Use that to predict price.  

# stock1 = tickers_nasdaq()[0]

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.averageVolume = yf.Ticker(ticker).info['averageVolume']
        self.averageVolumeTenDays = yf.Ticker(ticker).info['averageVolume10days']
        self.regularMarketVolume = yf.Ticker(ticker).info['regularMarketVolume']
        self.forwardPE = yf.Ticker(ticker).info['forwardPE']
        self.trailingPE = yf.Ticker(ticker).info['trailingPE']
        self.recommendations = yf.Ticker(ticker).recommendations
        self.options =  yf.Ticker(ticker).options
        self.fiftyTwoWeekHigh = yf.Ticker(ticker).info['fiftyTwoWeekHigh']
        self.fiftyTwoWeekLow = yf.Ticker(ticker).info['fiftyTwoWeekLow']
        self.regularMarketDayHigh = yf.Ticker(ticker).info['regularMarketDayHigh']
        self.regularMarketDayLow = yf.Ticker(ticker).info['regularMarketDayLow']
        self.sharesShort = yf.Ticker(ticker).info['sharesShort']
        self.shortRatio =  yf.Ticker(ticker).info['shortRatio']
        self.sharesShortPreviousMonthDate =  yf.Ticker(ticker).info['sharesShortPreviousMonthDate']
        self.earningsDateAndTime = get_next_earnings_date(ticker)
        
        
        
    def get_calls(self):
        date = self.options[0]
        calls = yf.Ticker(self.ticker).option_chain(date)
        return calls
        
    def get_puts(self):
        date = self.options[0]
        puts = yf.Ticker(self.ticker).option_chain(date)
        return puts
        

# msft = Stock('orcl')
# print(msft.trailingPE)
# print(msft.forwardPE)

# print(get_earnings_for_date('12/09/2022'))
orcl = Stock('orcl')
print(orcl.trailingPE)
print(orcl.forwardPE)