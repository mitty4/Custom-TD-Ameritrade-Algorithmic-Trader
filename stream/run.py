#import all we need
from tda.streaming import StreamClient

from handlers.sell_by_trade import sell_by_trade
from handlers.sell_all_positions import sell_all_positions
from handlers.find_trigger import find_trigger
from handlers.get_level_one import get_level_one

from variables.tickers import tickers
from login.client import stream_client, client
import login.config as config

import functions.settings as settings

import asyncio


# initialize global myDict
settings.init()
    
    
    
######## CREATE THE SOCKET ____________________________________________
async def read_stream():

    
### SETUP _____________________________________________________________    
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)
    
    
### GET LEVEL ONE QUOTES specifically last_price ______________________
    await stream_client.level_one_equity_subs(tickers)
    stream_client.add_level_one_equity_handler(get_level_one)
    
    
    
                    ######    ####    ### IMPORTANT TO SPECIFY #####
### SELL HOW????_______________________________________________________    
    ## by trade by intended ROI
    stream_client.add_level_one_equity_handler(sell_by_trade)   
    
    ## all positions at current price    
#     stream_client.add_level_one_equity_handler(sell_all_positions)   



    
# FIND TRIGGER ________________________________________________________
    await stream_client.chart_equity_subs(tickers)
    stream_client.add_chart_equity_handler(find_trigger)


    
    

    while True:
        await stream_client.handle_message()

        
        
asyncio.get_event_loop().run_until_complete(read_stream())







