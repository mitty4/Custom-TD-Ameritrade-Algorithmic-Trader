from tda.orders.equities import equity_buy_limit
from tda.orders.equities import equity_sell_limit
from tda.orders.generic import OrderBuilder 
from tda.orders.common import Duration, Session, first_triggers_second

from chart_equity_handler_functions.condition import trigger
from chart_equity_handler_functions.orders import get_orders
from chart_equity_handler_functions.cash_available import get_cash_available, get_acct, get_cash
from chart_equity_handler_functions.sms import send
# from chart_equity_handler_functions.test_handler import sym

from tda.client import Client

from client import client
from tickers import tickers
from df import get_df
from five_days import date_by_subtracting_business_days
from six_minutes import date_by_subtracting_minutes
import config



import json
import asyncio
from datetime import date
from datetime import datetime
from math import floor
import requests
import pickle

import pandas as pd
import numpy as np


import settings


def test_handler2(msg):
#     print(json.dumps(msg, indent=4))
#     print('run handler2')
    
    for sym in msg['content']:
#         print(sym['key'])
        symbol = sym['key']
        if 'ASK_PRICE' in sym:
#             print(sym['ASK_PRICE'])
            ask_price = sym['ASK_PRICE']
            settings.myDict[symbol] = ask_price
#     print(settings.myDict)

#         settings.myList.append({'symbol':sym,'ask_price':ask_price})
#     print(settings.myList)
    




def equity_chart_handler(msg):
#     print(settings.myList)
    
#     data = {
#     'quantity':10,
#     'price': 6.95,
#     'time': '09:09',
#     'sell_at':6.96,
#     'symbol':'KO'
#     }

#     send(data)
    #iterate over tickers 
    print(get_cash(client, config))
    for i,ticker in enumerate(msg['content']):
#         print(i)
#         if i > -1:
#             print(settings.myDict[ticker['key']])

# ________________testing________________________________________________________________________________
        
        
#         symbol = ticker['key']
#         #see orders for that symbol
#         print(json.dumps(get_orders(client, config, symbol).json(), indent=4))
        
#         six_ago = date_by_subtracting_minutes(datetime.now(), 6)
#         six_min_orders = client.get_orders_by_query(symbol,from_entered_datetime=six_ago).json()
#         print('________-\n',json.dumps(six_min_orders, indent=4))
        
#         for order in orders:
#             if order['transactionItem']['instruction'] == 'BUY':
#                 buy_p = order['transactionItem']['price']
        
        
#         # Define the params for the post request
#         auth = pickle.load( open( config.TOKEN_PATH, "rb" ) )
#         token = auth['access_token']
#         endpoint = 'https://api.tdameritrade.com/v1/accounts/277582772/orders'
#         header = {'Authorization': 'Bearer {}'.format(token),
#                    'Content-Type':'application/json'}


#         # Define buy/sell json for posting to td ameritrade
#         payload = {
#           "orderStrategyType": "SINGLE",
#           "session": "NORMAL",
#           "duration": "DAY",
#           "price": 4.88,
#           "orderType": "LIMIT",
#           "orderLegCollection": [
#             {
#               "instruction": "SELL",
#               "quantity": 1,
#               "instrument": {
#                 "assetType": "EQUITY",
#                 "symbol": symbol
#               }
#             }
#           ]
#         }





#         # POST request to BUY and SELL contingently
# #         content = requests.post(url=endpoint, json=payload, headers=header)
#         print(content.status_code)
#         print(content.raise_for_status())
#         six_ago = date_by_subtracting_minutes(datetime.now(), 6)
#         six_min_orders = client.get_orders_by_query(from_entered_datetime=six_ago).json()
#         print(json.dumps(six_min_orders, indent=4))
#         # Make sound when trigger occurs
#         print("\a","\a")


#         #see orders for that symbol
#         get_orders(client, config, symbol)
        
        
        
# ________________________________________________________________________________________________



    
        # Get live dataframe to search for triggers
        live = pd.DataFrame.from_dict(ticker, orient="index").T 
        live['time'] = live.apply(lambda row: datetime.fromtimestamp(row.CHART_TIME/1000).strftime("%I:%M:%S"),axis=1 )

        
        # Get historical data for analysis
        df = get_df(client, ticker, Client)


        # Get orders from specific days ago
        pdt = date_by_subtracting_business_days(datetime.today(), 5)
        five_day_orders = client.get_orders_by_query(from_entered_datetime=pdt).json()

        
        # Define time of trigger
        trig_time = datetime.fromtimestamp(live.CHART_TIME/1000).strftime("%I:%M")
      
        
        # If conditions for trigger present?
        if trigger(live, df):
            print('\n_____________________***__   {} TRIGGER {}    __***_____________________'.format(ticker['key'],trig_time))
            
            
#             # Get orders from six minutes ago
#             six_ago = date_by_subtracting_minutes(datetime.now(), 6)
#             six_min_orders = client.get_orders_by_query(from_entered_datetime=six_ago).json()
          
        
            # Get cash available for trading
            cash_available = get_cash(client, config)

            
            # If cash available greater than desired savings? 
            if cash_available >=25500: #1% of initial balance
                
                
                 # Define the buy price as the last minute's (live df) open price
                buy_price = live['CLOSE_PRICE'][0]
                buy_prc = buy_price*1
                
                print('bp1:', buy_price)
                print('bp2:',buy_prc)
                
                buy_prc = round(buy_prc,2)
                print('round bp:', buy_prc)
                

                buy_prc = round(settings.myDict[ticker['key']],2)

                
                
                # Get number of shares to buy from dollar amount willing to risk per trade
                quantity = floor(50/buy_prc)
                
                
                
                
                # ____________________ -----------   ROI  ----------- ________________________ #
                
                # Define ROI
                
                roi = 0.01
                
                
               
                
                # Define desired profit per trade
                profit = 1 + roi
                
                # Define acceptable loss per trade
                loss = 1 - (roi/2)
                
                
                # Define sell price from buy price * desired profit
                sell_price = round(buy_prc*profit,2)
                
                # Define loss price from buy price * acceptable loss
                loss_price = round(buy_prc*loss,2)
                
                
                # Define symbol
                symbol = ticker['key']
                
                # if the number of shares greater than 1?
                if quantity>=1:
                    
                    data = {
                        'quantity':quantity,
                        'price': buy_prc,
                        'time': trig_time,
                        'sell_at':buy_prc*profit,
                        'lose_at':buy_prc*loss,
                        'symbol':symbol
                        } 
                    send(data)
                    print('\a')
                    
                    # Print quantity placed to be bought
                    print('       quantity: {}       '.format(quantity))
                    print('       bought: $ {}       '.format(buy_prc))
                    print('       sell at: {}        '.format(buy_prc*profit))
                    print('_________________________________________________________________________________________')


                    
                    # Define the params for the post request
                    auth = pickle.load( open( config.TOKEN_PATH, "rb" ) )
                    token = auth['access_token']
                    endpoint = 'https://api.tdameritrade.com/v1/accounts/277582772/orders'
                    header = {'Authorization': 'Bearer {}'.format(token),
                               'Content-Type':'application/json'}

                    
                    
                    
                    
# _______________________________________________________________________________________________________________                    
                    
                    
                    payload = {
                      "orderStrategyType": "TRIGGER",
                      "session": "NORMAL",
                      "duration": "DAY",
                      "orderType": "LIMIT",
                      "price": buy_prc,
                      "orderLegCollection": [
                        {
                          "instruction": "BUY",
                          "quantity": quantity,
                          "instrument": {
                            "assetType": "EQUITY",
                            "symbol": symbol
                          }
                        }
                      ],
                      "childOrderStrategies": [
                        {
                          "orderStrategyType": "OCO",
                          "childOrderStrategies": [
                            {
                              "orderStrategyType": "SINGLE",
                              "session": "NORMAL",
                              "duration": "GOOD_TILL_CANCEL",
                              "orderType": "LIMIT",
                              "price": sell_price,
                              "orderLegCollection": [
                                {
                                  "instruction": "SELL",
                                  "quantity": quantity,
                                  "instrument": {
                                    "assetType": "EQUITY",
                                    "symbol": symbol
                                  }
                                }
                              ]
                            },
                            {
                              "orderStrategyType": "SINGLE",
                              "session": "NORMAL",
                              "duration": "GOOD_TILL_CANCEL",
                              "orderType": "STOP",
                              "stopPrice": loss_price,
                              "orderLegCollection": [
                                {
                                  "instruction": "SELL",
                                  "quantity": quantity,
                                  "instrument": {
                                    "assetType": "EQUITY",
                                    "symbol": symbol 
                                   }
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                    
                    
                    
                    
                    
                    
# _______________________________________________________________________________________________________________

#                     # Define buy/sell json for posting to td ameritrade
#                     payload = {
#                       "orderStrategyType": "SINGLE",
#                       "session": "NORMAL",
#                       "duration": "DAY",
#                       "orderType": "MARKET",
#                       "orderLegCollection": [
#                         {
#                           "instruction": "BUY",
#                           "quantity": quantity,
#                           "instrument": {
#                             "assetType": "EQUITY",
#                             "symbol": symbol
#                           }
#                         }
#                       ]
#                     }
                    
                    
                    
                    
        
#                     # POST request to BUY and SELL contingently
#                     content = requests.post(url=endpoint, json=payload, headers=header)
#                     print(content.status_code)
#                     print(content.raise_for_status())
                    
#                     # Make sound when trigger occurs
#                     print("\a","\a")
                    
                    
#                     six_ago = date_by_subtracting_minutes(datetime.now(), 6)
#                     orders = client.get_orders_by_query(from_entered_datetime=six_ago).json()
#                     print('________-\n',json.dumps(orders, indent=4))

#                     if orders[0]['transactionItem']['instruction'] == 'BUY':
#                         buy_p = orders[0]['transactionItem']['price']
        
        
        
#                     # sell order after getting the price of the market buy
#                     payload = {
#                         "orderStrategyType": "OCO",
#                         "childOrderStrategies": [
#                             {
#                               "orderType": "LIMIT",
#                               "session": "NORMAL",
#                               "price": round(buy_p*profit,2),
#                               "duration": "DAY",
#                               "orderStrategyType": "SINGLE",
#                               "orderLegCollection": [
#                                 {
#                                   "instruction": "SELL",
#                                   "quantity": quantity,
#                                   "instrument": {
#                                     "symbol": symbol,
#                                     "assetType": "EQUITY"
#                                   }
#                                 }
#                               ]
#                             },
#                             {
#                               "orderType": "STOP",
#                               "session": "NORMAL",
#                               "stopPrice": round(buy_p*loss,2),
#                               "duration": "DAY",
#                               "orderStrategyType": "SINGLE",
#                               "orderLegCollection": [
#                                 {
#                                   "instruction": "SELL",
#                                   "quantity": quantity,
#                                   "instrument": {
#                                     "symbol": symbol,
#                                     "assetType": "EQUITY"
#                                   }
#                                 }
#                               ]
#                             }
#                           ]
#                         }

                
                
# _______________________________________________________________________________________________________________                

                     # POST request to SELL 
                    content = requests.post(url=endpoint, json=payload, headers=header)
                    print(content.status_code)
                    print(content.raise_for_status())
                    
                    
                    # Get cash available for trading after transaction 
                    cash_available_after = get_cash(client, config)

                    
                    # Print cash available after transaction compared to before
                    print('           ',cash_available,'is now -------->> ',cash_available_after)

                
        # If no trigger then what?      
        else:
            no_t = '-----------------------------------------------------------------------no__trigger'
            print(ticker['key'],datetime.fromtimestamp(live.CHART_TIME/1000).strftime("%I:%M"), no_t)
            
          
        
        
    # Formatting between minute data  
    print('\n\n')
        
        

        
        

        
       
        
        
        
        
        
        

        
        
        
        
# the old payload for a trigger buy without the one cancels the other        
        
#  # Define buy/sell json for posting to td ameritrade
#                     payload = {
#                       "orderType": "MARKET",
#                       "session": "NORMAL",
# #                       "price": buy_price,
#                       "duration": "DAY",
#                       "orderStrategyType": "TRIGGER",
#                       "orderLegCollection": [
#                         {
#                           "instruction": "BUY",
#                           "quantity": quantity,
#                           "instrument": {
#                             "symbol": symbol,
#                             "assetType": "EQUITY"
#                           }
#                         }
#                       ],
#                       "childOrderStrategies": [
#                         {
#                           "orderType": "LIMIT",
#                           "session": "NORMAL",
#                           "price": sell_price,
#                           "duration": "GOOD_TILL_CANCEL",
#                           "orderStrategyType": "SINGLE",
#                           "orderLegCollection": [
#                             {
#                               "instruction": "SELL",
#                               "quantity": quantity,
#                               "instrument": {
#                                 "symbol": symbol,
#                                 "assetType": "EQUITY"
#                               }
#                             }
#                           ]
#                         }
#                       ]
#                     }
        
        
        

        
        
        
        
#          #test for definitions type and value
    
#          # Define the buy price as the last minute's (live df) open price
#         buy_price = round(live['OPEN_PRICE'][0],2)


#         # Get number of shares to buy from dollar amount willing to risk per trade
#         quantity = floor(200/buy_price)


#         # Define desired profit per trade
#         profit = 1.002


#         # Define sell price from buy price * desired profit
#         sell_price = round(buy_price*profit,2)


#         # Define symbol
#         symbol = ticker['key']


#         print(buy_price, quantity,sell_price,symbol)
#         print(type(buy_price),type(quantity),type(sell_price),type(symbol))
        
        
        
        
        
        
  #check the code - written without testing
            #if six_min_orders['orderLegCollection'][0]['instruction'] == 'BUY':
                # cancel the order by id number
    
#             buy=0
#             for order in five_day_orders:

#                 if order['orderLegCollection'][0]['instruction'] == 'BUY':
#                     buy += 1

#             print('Number of buys: {}'.format(buy))        
        
        
#             print(cash_available)        
#get_acct(client, config, print)
#print(df.head())

#print(datetime.today())
#print(date_by_subtracting_business_days(datetime.today(), 5))
#print(json.dumps(five_day_orders, indent=4))
#print(json.dumps(order, indent=4))
#print(order['orderLegCollection'][0]['instruction'])
#if len(five_day_orders)<3:
#print(json.dumps(five_day_orders, indent=4))
#if buy then sell (only if buy)

#this is where we buy and sell
                    
#  buy limit order                    
#                     client.place_order(equity_buy_limit(ticker['key'], quantity, buy_price)
#                         .set_duration(Duration.GOOD_TILL_CANCEL)
#                         .set_session(Session.SEAMLESS)
#                         .build())
                    
# #  sell limit order 1.005
#                     client.place_order(equity_sell_limit(ticker['key'], quantity, buy_price*profit)
#                          .set_duration(Duration.GOOD_TILL_CANCEL)
#                          .set_session(Session.SEAMLESS)
#                          .build())
    
#         print('trigger: df_high: {}, df_vol:{}'.format(np.percentile(df['high'],[95])[0],np.percentile(df['volume'],[5])[0]))
        
#         orders = get_orders(client, config, tickers)
#         print(orders.json())


# cancel unfilled orders older than 6 min
