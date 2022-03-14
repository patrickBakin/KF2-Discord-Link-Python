import socket
import time

from requests.exceptions import Timeout
from discord_webhook import DiscordWebhook,DiscordEmbed

from threading import Thread


class ReceiveChat:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sent_webhook=None
        self.webhook=None
    def Connect(self):

        while True:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(None)
                self.client.connect(("127.0.0.1", 2424))

                break
            except Exception as e:
                print("retrying: ", e)
                time.sleep(1)

        print("connected")

        self.HandleMessage()



    def HandleMessage(self):
        while True:

            data = self.client.recv(1024)
            if (data == bytes()):
                print("Reconnecting...")
                self.client.close()

                self.Connect()
                break
            else:
                self.webhook = DiscordWebhook('Your Webhook URL',content=self.decodedata(data.decode('utf-8')))

                self.sent_webhook = self.webhook.execute()
    @staticmethod
    def decodedata(string):
        numarray=string.split('/')
        Text=""
        for numi in range(len(numarray)):
            Text=Text+chr(int(numarray[numi]))
        return Text
"""
class CDInfo:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sent_webhook = None
        self.webhook = None
        self.embed = None
    def Connect(self):
        while True:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(None)
                self.client.connect(("127.0.0.1", 2425))

                break
            except Exception as e:
                print("CDInfo retrying: ", e)
                time.sleep(1)

        print("connected")

        self.HandleCDInfo(self.embed)
    def HandleCDInfo(self,Embed):
        while True:

            data = self.client.recv(1024)
            if (data == bytes()):
                self.client.close()

                self.Connect()
                break
            elif Embed == None or self.webhook == None:
                try:
                    self.webhook = DiscordWebhook('Your Webhook URL')

                    Embed = DiscordEmbed(title="CD Info", color='FF0F00')
                except Exception as e:
                    print(e)



            elif Embed != None:


                self.sent_webhook=self.webhook.execute(remove_embeds=True)
            Embed.set_author(name="Server Name")
            Embed.add_embed_field(name="Maxmonsters", value="0", inline=False)
            Embed.add_embed_field(name="SpawnPoll", value="0", inline=False)
            Embed.add_embed_field(name="CohortSize", value="", inline=False)
            Embed.add_embed_field(name="WaveSizeFakes", value="12", inline=False)
            Embed.add_embed_field(name="SpawnCycle", value="ts_mig_v3", inline=False)
            self.webhook.add_embed(Embed)
            self.sent_webhook = self.webhook.execute()

"""
if __name__ == '__main__':
   ReceiveChat().Connect()
   # t1 = Thread(target=ReceiveChat().Connect()).start()
   # t2 = Thread(target=CDInfo().Connect()).start()

