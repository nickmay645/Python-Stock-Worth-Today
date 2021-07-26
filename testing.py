# ticker_name = 'AMD'
import yfinance as yf
import datetime

today = datetime.date.today()

ticker_name = input("Enter ticker symbol: ")
date = input("Enter date: YYYY-MM-DD: ")
investment = input("Initial Investment: ")

ticker = yf.Ticker(ticker_name)
# ticker_df = ticker.history(period="max")
current_price = ticker.info['currentPrice']
past_data = yf.download(ticker_name, start=date)
past_price = past_data['Close'].array[0]
percent_change = ((current_price / past_price) - 1) * 100
val_today = float(investment) * float(float(current_price) / float(past_price))
print()
print("Results\n-----------------------------\n")
print(f"{ticker_name} change from {date} to {today}")
print(f"Percent Change: {percent_change}%")
print(f"Initial Investment: ${investment}")
print(f"Value Today: {val_today}")
print(f"Total Gain: ${val_today - float(investment)}")