import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged as {0}!".format(self.user))

intents = discord.Intents.default()
intents.message_content = True 

client = MyClient(intents=intents)
client.run("MTU3Mjk5NjEwMjIzMDExODUyMQ.GxYdVf.kIIhl0e-SwqNh7GxU1uStZFhFrbu8jyTM06skU")