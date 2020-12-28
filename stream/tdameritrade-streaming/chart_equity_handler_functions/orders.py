import json

def get_orders(client, config, tickers):
    orders = client.get_transactions(config.ACCOUNT_ID, symbol=tickers)
    return orders