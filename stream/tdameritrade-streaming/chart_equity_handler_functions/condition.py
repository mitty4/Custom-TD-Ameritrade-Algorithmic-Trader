import numpy as np

def trigger(live_df, hist_df):
    #define conditions
    
    #define variables
    candle_diff = 1.2 #1.2
    morn15 = ['08:{}:00'.format(30+x) for x in range(0,15)]
    noon60 = ['03:{}:00'.format(0+x) for x in range(0,59)]

    #define open higher than open low
    high_not_zero = (live_df['HIGH_PRICE']-live_df['OPEN_PRICE']) != 0 
    low_not_zero = (live_df['OPEN_PRICE']-live_df['LOW_PRICE']) != 0 
    tall_candle = (live_df['HIGH_PRICE']-live_df['OPEN_PRICE']) > candle_diff*(live_df['OPEN_PRICE']-live_df['LOW_PRICE'])
    volume75 = live_df['VOLUME'] >= np.percentile(hist_df['volume'],[0])[0] #90
    price65th = live_df['OPEN_PRICE']<np.percentile(hist_df['high'],[65])[0] #65
    not_penny = live_df['OPEN_PRICE']>1
    #     not_first15 = ~live_df['time'].isin(morn15)
    #     not_last60 = ~live_df['time'].isin(noon60)

    return high_not_zero[0] & low_not_zero[0] & tall_candle[0] & volume75[0] & price65th[0] & not_penny[0] # & not_first15[0] & not_last60[0]