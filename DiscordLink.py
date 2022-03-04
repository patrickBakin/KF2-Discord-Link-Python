import socket  
import time

from discord import Webhook, RequestsWebhookAdapter # Importing discord.Webhook and discord.RequestsWebhookAdapter

webhook = Webhook.from_url('Your Discord Webhook Url', adapter=RequestsWebhookAdapter()) # Initializing webhook
webhook.send(content="Hello World")

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

        data = client.recv(1024).decode()
        if (data == ""):
            client.close()

            Connect()
            break
        else:
            webhook.send(data)


Connect()