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

from chart_equity_handler_functions.chart_equity_handler import equity_chart_handler
from chart_equity_handler_functions.chart_equity_handler import test_handler2
from chart_equity_handler_functions.test_handler import test_handler

import pandas as pd
import numpy as np
    
    
    
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
    stream_client.add_chart_equity_handler(equity_chart_handler)



    

    while True:
        await stream_client.handle_message()

asyncio.get_event_loop().run_until_complete(read_stream())







