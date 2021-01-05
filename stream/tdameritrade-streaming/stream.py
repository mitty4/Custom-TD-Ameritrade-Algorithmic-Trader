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
from chart_equity_handler_functions.test_handler import test_handler

import pandas as pd
import numpy as np

    
#create the socket
async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.DELAYED)
    await stream_client.chart_equity_subs(tickers)
    
    stream_client.add_chart_equity_handler(equity_chart_handler)
    

    while True:
        await stream_client.handle_message()

asyncio.get_event_loop().run_until_complete(read_stream())







