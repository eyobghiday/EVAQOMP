import alpaca_trade_api as tradeapi
import os

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)
# Placeholder for Reddit scraper using PRAW or requests

def market_buy(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

def set_stop_loss(symbol, qty, entry_price):
    stop_price = round(entry_price * 0.90, 2)
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='stop',
        stop_price=str(stop_price),
        time_in_force='gtc'
    )
