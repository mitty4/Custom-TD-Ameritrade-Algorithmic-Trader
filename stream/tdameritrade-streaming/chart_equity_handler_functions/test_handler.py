import requests
import json
from config import TOKEN_PATH 
import pickle


def test_handler(msg):
    
    auth = pickle.load( open( TOKEN_PATH, "rb" ) )
    token = auth['access_token']
    print(token)

    # Define the params for the post request
#     endpoint = "https://api.tdameritrade.com/v1/accounts/277582772/savedorders"
    endpoint = "https://api.tdameritrade.com/v1/accounts/277582772/orders"
    header = {'Authorization': 'Bearer {}'.format(token),
               'Content-Type':'application/json'}


    # Define buy/sell json for posting to td ameritrade
    payload = {
      "orderType": "MARKET",
      "session": "NORMAL",
      "duration": "DAY",
      "orderStrategyType": "TRIGGER",
      "orderLegCollection": [
        {
          "instruction": "BUY",
          "quantity": 1,
          "instrument": {
            "symbol": "AAPL",
            "assetType": "EQUITY"
          }
        }
      ],
      "childOrderStrategies": [
        {
          "orderType": "MARKET",
          "session": "NORMAL",
          "duration": "DAY",
          "orderStrategyType": "SINGLE",
          "orderLegCollection": [
            {
              "instruction": "SELL",
              "quantity": 1,
              "instrument": {
                "symbol": "AAPL",
                "assetType": "EQUITY"
              }
            }
          ]
        }
      ]
    }
    
    payload2 = {
      "orderType": "LIMIT",
      "session": "NORMAL",
      "price": "2.00",
      "duration": "DAY",
      "orderStrategyType": "SINGLE",
      "orderLegCollection": [
        {
          "instruction": "Buy",
          "quantity": 15,
          "instrument": {
            "symbol": "XYZ",
            "assetType": "EQUITY"
          }
        }
      ]
    }
    
    payload3 = {
      "orderType": "MARKET",
      "session": "NORMAL",
      "duration": "DAY",
      "orderStrategyType": "TRIGGER",
      "orderLegCollection": [
        {
          "instruction": "BUY",
          "quantity": 10,
          "instrument": {
            "symbol": "XYZ",
            "assetType": "EQUITY"
          }
        }
      ],
      "childOrderStrategies": [
        {
          "orderType": "MARKET",
          "session": "SEAMLESS",
          "duration": "DAY",
          "orderStrategyType": "SINGLE",
          "orderLegCollection": [
            {
              "instruction": "SELL",
              "quantity": 10,
              "instrument": {
                "symbol": "XYZ",
                "assetType": "EQUITY"
              }
            }
          ]
        }
      ]
    }


    content = requests.post(url=endpoint, json=payload, headers=header)
    print(content.status_code)
    print(content.raise_for_status())