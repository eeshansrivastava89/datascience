import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Starbucks!
""")

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

tickerDf = tickerData.history(period='1d', start='2019-01-01', end='2022-8-05')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
