from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient

import config


#create the client to talk to td ameritrade
client = easy_client(
        api_key=config.API_KEY,
        redirect_uri=config.REDIRECT_URI,
        token_path=config.TOKEN_PATH)
stream_client = StreamClient(client, account_id=config.ACCOUNT_ID)