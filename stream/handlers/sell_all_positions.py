import login.config as config
from login.client import client
from tda.client import Client
from functions.sms import send
import time
import pickle


# this code will sell all the positions if the roi is at zero - dont forget to turn off the 'find_trigger' handler

def sell_all_positions(msg):

    ## DOES THIS DO ANYTHING VALUABLE?? -- REQUEST LIMIT 120/min
    time.sleep(1)

    ## SELL AT CURRENT MARKET PRICE
    roi = 0.00

    ## SELL AT CURRENT MARKET PRICE
    profit = 1 + roi

    ## SELL AT CURRENT MARKET PRICE
    loss = 1 - (roi*0.25)

    # GET ACCOUNT WITH POSITIONS
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

                
                
                
                ## LOSS ___________LOSS_________________________LOSS______________________           
                # when k['averagePrice']*loss <= k['marketValue']
                if p['averagePrice']*loss*quantity >= p['marketValue']:
                    
                    ## VISUALIZE THE LOSS
                    print('                        loss')

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
                          "quantity": quantity,
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
#                     print(content.status_code)
#                     print(content.raise_for_status())





                ## MONEY____________ MONEY_________________MONEY________________________  
                if p['averagePrice']*profit*quantity <= p['marketValue']:
                    
                    ## VISUALIZE THE PROFIT
                    print('                        profit')

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
                          "quantity": quantity,
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
#                     print(content.status_code)
#                     print(content.raise_for_status())










