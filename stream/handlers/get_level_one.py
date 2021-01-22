import functions.settings as settings


## GET LEVEL ONE INFO FOR THE last_price VALUE
def get_level_one(msg):
    
    ## VISUALIZE RETREIVING last_price
    print('got lp')
    
    ## LOOP THROUGH EACH SYMBOLs DATA
    for sym in msg['content']:
        
        ## DEFINE SYMBOL
        symbol = sym['key']
        
        
        
        
        ## DEFINE last_price IF IN SYMBOL DATA
        if 'LAST_PRICE' in sym:
            
            ## DEFINE VARIABLE
            last_price = sym['LAST_PRICE']
            
            ## ADD TO GLOBAL DICT FOR LATER RETREIVAL IN OTHER HANDLER
            settings.myDict[symbol] = last_price