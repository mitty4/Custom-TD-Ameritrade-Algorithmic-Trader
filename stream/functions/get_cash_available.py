import json
        
def get_cash_available(client, config):
    acct = client.get_account(config.ACCOUNT_ID).json()
    return acct['securitiesAccount']['currentBalances']['cashBalance']