import pandas as pd

def get_df(client, ticker, Client):
    resp = client.get_price_history(ticker['key'],
        period_type=Client.PriceHistory.PeriodType.DAY,
        period=Client.PriceHistory.Period.TEN_DAYS,
        frequency_type=Client.PriceHistory.FrequencyType.MINUTE,
        frequency=Client.PriceHistory.Frequency.EVERY_MINUTE)
    
    
    df = pd.DataFrame(resp.json()['candles'])
    
    
    #create open to high column
    df['open_high'] = df['high']-df['open']
    #create open to low column
    df['open_low'] = df['open']-df['low']
    
    return df