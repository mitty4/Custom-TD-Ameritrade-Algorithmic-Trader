import json

def get_acct(client, config, callback):
    acct = client.get_account(config.ACCOUNT_ID)
    
    return callback(acct.json())


async def get_cash_available(acct):
    print(acct)
#    cash_available = acct['securitiesAccount']['projectedBalances']['cashAvailableForTrading']
 #   return cash_available
    
    
def get_cash(client, config):
    
    acct = client.get_account(config.ACCOUNT_ID).json()
    return acct['securitiesAccount']['currentBalances']['cashBalance']