import time
import pickle

import login.config as config

from tda.client import Client
from login.client import client
from functions.get_cash_available import get_cash_available
from db.sqlite import insert_trade, get_trade
from functions.sms import send



## LOOP THROUGH DB 'trades' CHECK FOR CONDITION AND SELL ASSOCIATED QUANTITY
def sell_by_trade(msg):

    ## SET DESIRED ROI
    roi = 0.0035       #.   <<<<<<<<<<<<<<<<<<  <<<<< <    <<<        <<            <
    
    ## NOT SURE IF THIS HELPS -- LIMIT OF 120/min REQUESTS
    time.sleep(1)

    ## DESIRED PROFIT PER TRADE
    profit = 1 + roi

    ## DESIRED LOSS PER TRADE
    loss = 1 - (roi*0.25)

    #GET ACCOUNT WITH POSITIONS
    data = client.get_account(277582772,fields=Client.Account.Fields.POSITIONS)
    positions = data.json()



    ## CHECK FOR POSITIONS OBJECT
    if 'securitiesAccount' in positions:
        if 'positions' in positions['securitiesAccount']:
            
            ## INITIALIZE DATA OBJECT FOR TEXT MESSAGE DATA
            data = dict()

            
            
            
            ## LOOP THROUGH EACH POSITION/SYMBOL
            for p in positions['securitiesAccount']['positions']:
                
                ## DEFINE VARIABLES
                symbol = p['instrument']['symbol']
                quantity = round(p['longQuantity'])
                data['symbol'] = symbol

                # LOOP THROUGH DB TABLE 'Trades'
                for t in get_trade():
                    
                    ## VISUALIZE HOW OFTEN CONDITION IS CHECKED
                    print('checking trades...')
                    
                    
                    
                    
                    ## IF THE SYMBOL OF POSITION AND SYMBOL OF TRADES MATCH
                    if p['instrument']['symbol'] == t[1]:
                        # if last price <= trade price then sell for a loss
                        
                        
                        
                        
                        ## LOSS ___________LOSS_________________________LOSS______________________ 
                        
                        ##IF trade_price * loss LESS THAN EQUAL TO last_price
                        ## ['marketValue'] gives the MV of current position. Divide by quantity for unit market price
                        if p['marketValue']/quantity <= t[2]*loss:
                            
                            ## VISUALIZE THE LOSS
                            space = '                             '
                            print(space,'...loss  q:{}  markVal:{}  lossVal:{}  tradeVal:{}'.format(quantity,t[2]*loss,t[2]))
                            
                            ## SEND TEXT MESSAGE WITH LOSS INFO
                            data['WoL'] = 'Loss'
                            send(data)
                            
                            ## DEFINE THE MARKET SELL DURING NORMAL DAY HOURS
                            payload = {
                              "orderType": "MARKET",
                              "session": "NORMAL",
                              "duration": "DAY",
                              "orderStrategyType": "TRIGGER",
                              "orderLegCollection": [
                                {
                                  "instruction": "SELL",
                                  "quantity": round(t[3]),
                                  "instrument": {
                                    "symbol": symbol,
                                    "assetType": "EQUITY"
                                  }
                                }
                              ],
                            }

                            ## POST REQUEST TO SELL AT MARKET PRICE
                            content = requests.post(url=config.endpoint, json=payload, headers=config.header)
                            
                            ## CHECK FOR TYPE OF RESPONSE
#                             print(content.status_code)
#                             print(content.raise_for_status())


                    ## add if response object is 201 then remove the trade
                            remove_trade(t[0])


        
        
                         ## MONEY____________ MONEY_________________MONEY________________________  
            
                        ## IF last_price GREATER THAN EQUAL TO trade_price * profit
                        ## ['marketValue'] gives the MV of current position. Divide by quantity for unit market price
                        if p['marketValue']/quantity <= t[2]*profit:
                            
                            ## VISUALIZE THE PROFIT
                            space = '                             '
                            print(space,'...money! q:{}  markVal:{}  gainVal:{}  tradeVal:{}'.format(quantity,t[2]*profit,t[2]))
                            
                            ## SEND TEXT MESSAGE WITH LOSS INFO
                            data['WoL'] = 'Profit'
                            send(data)
                            
                            ## DEFINE THE MARKET SELL DURING NORMAL DAY HOURS
                            payload = {
                              "orderType": "MARKET",
                              "session": "NORMAL",
                              "duration": "DAY",
                              "orderStrategyType": "TRIGGER",
                              "orderLegCollection": [
                                {
                                  "instruction": "SELL",
                                  "quantity": round(t[3]),
                                  "instrument": {
                                    "symbol": symbol,
                                    "assetType": "EQUITY"
                                  }
                                }
                              ],
                            }

                            ## POST REQUEST TO SELL AT MARKET PRICE
                            content = requests.post(url=config.endpoint, json=payload, headers=config.header)
                            
                            ## CHECK FOR TYPE OF RESPONSE
#                             print(content.status_code)
#                             print(content.raise_for_status())


                    ## add if response object is 201 then remove the trade
                            remove_trade(t[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        