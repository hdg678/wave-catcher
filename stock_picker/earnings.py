import yfinance as yf
from yahoo_fin.stock_info import *

# https://www.thepythoncode.com/article/reading-emails-in-python
# https://www.fool.com/services/
# https://investor.morningstar.com/mm/
# https://www.etoro.com/copytrader/
# https://reports.tradersalgo.com/google-ads-ats-trading-alerts-new-ta-alerts-campaign-v1/?gclid=Cj0KCQiAsoycBhC6ARIsAPPbeLtinUgr4RZRgpXjj54KDdkgD3WKQ2BRDgRDEyZ1-kohESVdb9TdH7MaAgPKEALw_wcB
# https://proxiesapi-com.medium.com/scraping-most-active-stocks-data-from-yahoo-finance-with-python-and-beautiful-soup-79a218c91835
# documentation on yahoo_fin
# http://theautomatic.net/yahoo_fin-documentation/
	
# print(get_day_gainers())
# print(get_day_losers())
# print(get_day_most_active())
# print(get_undervalued_large_caps())
# tickers_nasdaq()
# print(get_earnings_for_date('12/06/2022'))
get_premarket_price('tqqq')
get_postmarket_price('tqqq')