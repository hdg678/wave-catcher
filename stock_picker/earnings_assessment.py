import yfinance as yf
import requests_html
from yahoo_fin.stock_info import *
from datetime import datetime, timedelta
import stock
import json
import time

def compare_pe():
	with open('stats.json', 'r') as openfile:
		json_object = json.load(openfile)
		for tick in json_object:
			print(tick['forwardPE'])
		return 0





print(compare_pe())