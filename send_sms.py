# Download the helper library from https://www.twilio.com/docs/python/install
import os

from time import sleep
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC0cea4694c21bd1a7055c28665f4da017'
auth_token = '670f0a595db902d6145427eea477a3b9'
client = Client(account_sid, auth_token)

for i in range(10):
    message = client.messages \
                    .create(
                        body="Hola Axius, como van los dotas?.",
                        from_='+19123943422',
                        to='+573058842998'
                    )
    sleep(3)
    print(message.sid)