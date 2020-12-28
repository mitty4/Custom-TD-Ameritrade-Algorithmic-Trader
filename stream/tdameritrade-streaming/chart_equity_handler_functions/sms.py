# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# TWILIO_ACCOUNT_SID=
# TWILIO_AUTH_TOKEN=

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ[TWILIO_ACCOUNT_SID]
# auth_token = os.environ[TWILIO_AUTH_TOKEN]


def send(data):
   #Define twilio credentials
    account_sid = 'AC3f244a803eb8ca53c33bbba841c1fdb3'
    auth_token = 'f9aa627775c01ac59e816b44ed7cc9a8'
    
    
    # Create client
    client = Client(account_sid, auth_token)

    
    # Send message
    message = client.messages.create(
        body=' buy \n {}, {} shares, ${}, total: ${}, \n Sell at: ${}, \n time: {} \n '
        .format(data['symbol'],
                data['quantity'],
                data['price'],
                data['quantity']*data['price'],
                data['sell_at'],
                data['time']
                ),
        from_='+14324005221',
        to='+19725766149'
        )

