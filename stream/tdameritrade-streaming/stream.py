#import all we need
from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient

import asyncio
import json
import config
from tickers import tickers
from client import stream_client, client
from chart_equity_handler_functions.cash_available import get_cash_available, get_acct
from chart_equity_handler_functions.sms import send

from chart_equity_handler_functions.chart_equity_handler import equity_chart_handler
from chart_equity_handler_functions.chart_equity_handler import test_handler2
from chart_equity_handler_functions.test_handler import test_handler

import pandas as pd
import numpy as np
import pickle
import requests
import time
    
import settings


# settings.init()          # Call only once
# subfile.stuff()         # Do stuff with global var
# print settings.myList[0]





def handler(msg):
#     print(json.dumps(msg, indent=4))
    for sym in msg['content']:
        last_price = sym['LAST_PRICE']
        sym = sym['key']
        print(sym, last_price)

    
    
async def say_after(delay, what):
    await asyncio.sleep(delay)
    return what
    
    
def test(msg):
    


    # Define the params for the post request
    auth = pickle.load( open( config.TOKEN_PATH, "rb" ) )
    token = auth['access_token']
    endpoint = 'https://api.tdameritrade.com/v1/accounts/277582772/orders'
    header = {'Authorization': 'Bearer {}'.format(token),
               'Content-Type':'application/json'}
    
    roi = 0.01


    # Define desired profit per trade
    profit = 1 + roi

    # Define acceptable loss per trade
    loss = 1 - (roi/2.3)
    
    while True:
        time.sleep(1)
        #get account with positions
        data = client.get_account(277582772,fields=Client.Account.Fields.POSITIONS)
        positions = data.json()
#         print(json.dumps(positions, indent=4))
        if 'securitiesAccount' in positions:
            if 'positions' in positions['securitiesAccount']:
                data = dict()
        
                #check each open position
                for k in positions['securitiesAccount']['positions']:
                    symbol = k['instrument']['symbol']
                    quantity = round(k['longQuantity'])
                    data['symbol'] = symbol
        # LOSS _______________________________________________________            
                    # LOSS point of sell
                    # when k['averagePrice']*loss <= k['marketValue']
                    if k['averagePrice']*loss*quantity >= k['marketValue']:
                        print('loss ', symbol, quantity)
                        print(loss,'*buyPrice = ',k['averagePrice']*loss*quantity)
                        print(k['marketValue'])
                        data['WoL'] = 'Loss'
                        send(data)
                        payload = {
                          "orderType": "MARKET",
                          "session": "NORMAL",
                          "duration": "DAY",
                          "orderStrategyType": "TRIGGER",
                          "orderLegCollection": [
                            {
                              "instruction": "SELL",
                              "quantity": quantity,
                              "instrument": {
                                "symbol": symbol,
                                "assetType": "EQUITY"
                              }
                            }
                          ],
                        }

                        # POST request to SELL 
                        content = requests.post(url=endpoint, json=payload, headers=header)
                        print(content.status_code)
                        print(content.raise_for_status())

        # GAIN _______________________________________________________
                    # GAIN point of sell
                    if k['averagePrice']*profit*quantity <= k['marketValue']:
                        print('money! ', symbol, quantity)
                        print(profit,'*buyPrice = ',k['averagePrice']*profit*quantity)
                        print(k['marketValue'])
                        data['WoL'] = 'Money!'
                        send(data)
                        payload = {
                          "orderType": "MARKET",
                          "session": "NORMAL",
                          "duration": "DAY",
                          "orderStrategyType": "TRIGGER",
                          "orderLegCollection": [
                            {
                              "instruction": "SELL",
                              "quantity": quantity,
                              "instrument": {
                                "symbol": symbol,
                                "assetType": "EQUITY"
                              }
                            }
                          ],
                        }

                        # POST request to SELL 
                        content = requests.post(url=endpoint, json=payload, headers=header)
                        print(content.status_code)
                        print(content.raise_for_status())    

    
#create the socket
async def read_stream():
    settings.init()
    
    
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)
    
    # last price
#     await stream_client.timesale_equity_subs(tickers)
#     stream_client.add_timesale_equity_handler(test_handler2)
#     stream_client.add_chart_equity_handler(equity_chart_handler)
    
    #get last price from first level
    await stream_client.level_one_equity_subs(tickers)
    stream_client.add_level_one_equity_handler(test_handler2)
    
    
    # trigger algotrader
    await stream_client.chart_equity_subs(tickers)
#     stream_client.add_chart_equity_handler(equity_chart_handler)
    stream_client.add_chart_equity_handler(test)


    

    while True:
        await stream_client.handle_message()

asyncio.get_event_loop().run_until_complete(read_stream())







