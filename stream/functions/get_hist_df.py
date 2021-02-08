import pandas as pd


## GET HISTORICAL DATA 
def get_hist_df(client, ticker, Client):
    
    ## GET INDIVIDUAL PRICE HISTORY 
    resp = client.get_price_history(ticker['key'],
        period_type=Client.PriceHistory.PeriodType.DAY,
        period=Client.PriceHistory.Period.TEN_DAYS,
        frequency_type=Client.PriceHistory.FrequencyType.MINUTE,
        frequency=Client.PriceHistory.Frequency.EVERY_MINUTE)
    
    
    if "candles" in resp.json():
    
        ## CONVERT TO PANDAS DF
        df = pd.DataFrame(resp.json()['candles'])


        ## CREATE OPEN TO HIGH COLUMN FOR PART OF THE CONDITION
        df['open_high'] = df['high']-df['open']

        ## CREATE OPEN TO LOW COLUMN FOR PART OF THE CONDITION
        df['open_low'] = df['open']-df['low']
    
        return df
    
    else:
        return