from tda.auth import easy_client
from tda.streaming import StreamClient

import login.config as config


#create the client to talk to td ameritrade
#initialize a session
client = easy_client(
    config.API_KEY,
    config.REDIRECT_URI,
    config.TOKEN_PATH
)

stream_client = StreamClient(client, account_id=config.ACCOUNT_ID)

stream_client2 = StreamClient(client, account_id=config.ACCOUNT_ID)