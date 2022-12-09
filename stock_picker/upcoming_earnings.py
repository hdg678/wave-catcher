import yfinance as yf
import requests_html
from yahoo_fin.stock_info import *
from datetime import datetime, timedelta
import stock
import json
import time

# todo
# -filter only nasdaq and large market stock earnings: legit exchanges nyq and nms
# -get forwardPE prior to earnings release and log it in json
# -if PE exceeds former forward pe, trigger a buy notice
# ['AZRE', 'MESA', 'MESA', 'AAM-PA', 'LEGN', 'ENZ', 'COUP', 'COUP',
 # 'RAAS', 'RAAS', 'RAAS', 'RAAS', 'ORCL', 'DLNG', 'DLNG', 'DAKT', 'DAKT', 'GEHI', 'FLNC', 'SEAC', 'SEAC', 'UTI', 'UTI']


# Get Dates
presentday = datetime.now() 
tomorrow = presentday + timedelta(1)
presentday = presentday.strftime('%m-%d-%Y')  
tomorrow = tomorrow.strftime('%m-%d-%Y')

# Get next round of earnings reports
def extract_upcoming_tickers(day):
	temp = []
	reports = get_earnings_for_date(day)
	report_size = len(get_earnings_for_date(day))
	for report in reports:
		if (yf.Ticker(report['ticker']).info['exchange'] == 'NYQ') or (yf.Ticker(report['ticker']).info['exchange'] == 'NMS'):
			temp.append(report['ticker'])
		time.sleep(1)
		# print(temp)
	return [*set(temp)]
 

# write current stock pe to compare tomorrow for exceeeded earnings
def update_stock_data(ticker_list):
	temp = []
	for t in ticker_list:
		try:
			temp_stock = stock.Stock(t)
			stock_data = {
			'ticker': t,
			'trailingPE': temp_stock.trailingPE,
			'forwardPE': temp_stock.forwardPE 
			}
			temp.append(stock_data)
		except:
			pass
		time.sleep(1)
		# print(temp)

	with open("stats.json", "w") as outfile:
		json.dump(temp, outfile)
		return 0

tickers = extract_upcoming_tickers(tomorrow)
update_stock_data(tickers)







