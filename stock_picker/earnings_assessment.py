import yfinance as yf
import requests_html
from yahoo_fin.stock_info import *
from datetime import datetime, timedelta
import stock
import json
import time

def compare_pe():
	with open('./wave-catcher/stock_picker/stats.json', 'r') as openfile:
		json_object = json.load(openfile)
		for tick in json_object:
			PEchange = tick['forwardPE'] 
			print(PEchange)
		return 0
		
		
def extract_today_tickers(day):
	temp = []
	reports = get_earnings_for_date(day)
	report_size = len(get_earnings_for_date(day))
	for report in reports:
		if (yf.Ticker(report['ticker']).info['exchange'] == 'NYQ') or (yf.Ticker(report['ticker']).info['exchange'] == 'NMS'):
			temp.append(report['ticker'])
		time.sleep(1)
		print(temp)
	return [*set(temp)]


def update_stock_data(ticker_list):
	temp = []
	for t in ticker_list:
		try:
			temp_stock = stock.Stock(t)
			stock_data = vars(temp_stock)
			temp.append(stock_data)
		except:
			pass
		time.sleep(1)
		print(temp)

	with open("new_stats.json", "w") as outfile:
		json.dump(temp, outfile)
		return 0



presentday = datetime.now() 
presentday = presentday.strftime('%m-%d-%Y')  
# tickers = extract_upcoming_tickers(presentday)
tickers = ['avgo', 'nvda', 'aapl']
update_stock_data(tickers)
# temp = stock.Stock('avgo')
