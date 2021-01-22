import time
import pickle
import requests
import pandas as pd
from datetime import datetime
from math import floor

from login.client import client
from tda.client import Client
from functions.get_cash_available import get_cash_available
from functions.get_hist_df import get_hist_df
from functions.get_condition import get_condition
from db.sqlite import insert_trade, get_trade

import login.config as config
import functions.settings as settings


## FIND TRIGGER AND POST A MARKET BUY THEN SEND TRADE TO DB
def find_trigger(msg):
    
    ## GET CASH AVAILABLE FOR TRADING
    cash_available = get_cash_available(client, config)
    print(cash_available)
    
    

    
    
    ## LOOP THROUGH THE CHOSEN TICKERS    
    for i,ticker in enumerate(msg['content']):     

            
        # DEFINE SYMBOL
        symbol = ticker['key']
        
        
        ## GET LIVE DF TO SEARCH FOR TRIGGERS
        live = pd.DataFrame.from_dict(ticker, orient="index").T 
        live['time'] = live.apply(lambda row: datetime.fromtimestamp(row.CHART_TIME/1000).strftime("%I:%M:%S"),axis=1 )
        
        ## GET HISTORICAL DATA FOR ANALYSIS
        df = get_hist_df(client, ticker, Client)
        
        ## DEFINE TIME OF TRIGGER FOR VISUALIZATION
        trig_time = datetime.fromtimestamp(live.CHART_TIME/1000).strftime("%I:%M")
      
    
    
    
    
        
        ## CHECK IF CONDITION/TRIGGER IS PRESENT
        if get_condition(live, df):
               
                            
            ## SET MONEY PER TRADE 
            per_trade = 50         # <<<<<<<<<<<<

            ## GET QUANTITY OF SHARES TO BUY
            quantity = floor(per_trade/round(live['OPEN_PRICE'][0],2))
            
            ## DEFINE THE STRING TO PRINT
            string = '\n____________________***__  {} TRIGGER t: {}  q: {} lp: ${} __***______________          '

            
            ## PRINT THE TRIGGER SYMBOL AND TIME
            print(string.format(symbol,trig_time, quantity, settings.myDict[symbol]))

            
            
            
            
            
            ## SET AMOUNT OF $$ TO RISK, 1% of initial balance recommended
            if cash_available >=25500:         # <<<<<<<<<<<< 
                
                
                
                
                
                ## IF PRICE MORE THAN per_trade SET QUANTITY TO 1
                if quantity <1:
                    quantity = 1
                
                
                
                
                
                ## IF QUANTITY AT LEAST ONE
                if quantity>=1:
                    
                    
                    ## DING A SOUND ALERT
                    print('\a')              

                    ## DEFINE THE ORDER SPECS FOR A MARKET BUY DURING NORMAL DAY
                    payload = {
                      "orderStrategyType": "TRIGGER",
                      "session": "NORMAL",
                      "duration": "DAY",
                      "orderType": "MARKET",
                      "orderLegCollection": [
                        {
                          "instruction": "BUY",
                          "quantity": quantity,
                          "instrument": {
                            "symbol": symbol,
                            "assetType": "EQUITY"
                          }
                        }
                      ],
                    }
                                   

                    ## SEND POST REQUEST TO BUY EQUITY
                    content = requests.post(url=config.endpoint, json=payload, headers=config.header)
                    
                    ## CHECK FOR TYPE OF RESPONSE
#                     print(content.status_code)
#                     print(content.raise_for_status())
                    
                    ## DEFINE TRADE OBJECT FOR DB
                    trade = {
                        'id':datetime.now().timestamp(),
                        'sym':symbol,
                        'price': settings.myDict[symbol],
                        'quantity':quantity
                        }
            
                    ## ADD TRADE TO DB
                    insert_trade(trade)
                    
                    ## CHECK FOR CASH AVAILABLE AFTER TRADE
                    cash_available_after = get_cash_available(client, config)

                    ## PRINT CASH DIFFERENCE AFTER TRADE
                    print('from $'cash_available,' ---->> to $',cash_available_after)                    
                    
                
                
                
        ## IF NO TRIGGER THEN PRINT  
        else:
            no_t = '-----------------------------------------------------------------------no__trigger'
            print(symbol,trig_time, settings.myDict[symbol], no_t)
            
          
        
        
    # Formatting between minute data  
    print('\n\n')
