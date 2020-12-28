from tda.auth import easy_client

import login.config as config


#create the client to talk to td ameritrade
#initialize a session
TDSession = easy_client(
    config.API_KEY, 
    config.REDIRECT_URI, 
    config.TOKEN_PATH
)
