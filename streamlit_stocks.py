import yfinance as yf
import streamlit as st
import datetime
from datetime import timedelta

st.write("""
# Simple Stock Price App
Type the ticker symbol for which you'd like to see the last 90 Day stock closing price
""")

# Get Dates
tDate = datetime.datetime.now()
l90Date = tDate - timedelta(90)

#tDate = tDate.strftime("%Y-%m-%d")
#l90Date = l90Date.strftime("%Y-%m-%d")

# Put Date Selector
d1 = st.sidebar.date_input(
     "Start Date",
     l90Date)

d2 = st.sidebar.date_input(
     "End Date",
     tDate)

tickerSymbol = st.text_input('Ticker Symbol:','SBUX')
tickerData = yf.Ticker(tickerSymbol)
tickerInfo = tickerData.get_info()

# Ticker Stats
tickerLongName = tickerInfo['longName']
tickerEmployees = "${:,}".format(tickerInfo['fullTimeEmployees'])
tickerRevenue = "${:,}".format(tickerInfo['totalRevenue'])
tickerMarketCap = "${:,}".format(tickerInfo['marketCap'])

st.write("""
## Now fetching data for: {}
Key Stats:
* No. of Full Time Employees: {}
* Total Revenue: {}
* Market Cap: {}
""".format( tickerLongName, tickerEmployees, tickerRevenue, tickerMarketCap))

# Fetch Date
tickerDf = tickerData.history(period='1d', start=d1, end=d2)

st.write("""
### Stock Closing Price
""")
st.line_chart(tickerDf.Close)
