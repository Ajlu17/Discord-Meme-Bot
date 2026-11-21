import os
from dotenv import load_dotenv
import discord
import requests
import json 

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print("Logged as {0}!".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello World!")

        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())
        
        if message.content.startswith("$ping"):
            await message.channel.send(f"Pong! Latency: {round(self.latency * 1000)}ms")

        if message.content.startswith("$embed"):
            embed = discord.Embed(title="Embedded Message", 
            description="This is an embedded message.", 
            color=discord.Color.blue()
            )
            await message.channel.send(embed=embed)

intents = discord.Intents.default()
intents.message_content = True 

client = MyClient(intents=intents)

@client.tree.command(name="hello", description="Says hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!")

@client.tree.command(name="meme", description="Sends a random meme")
async def meme(interaction: discord.Interaction):
    await interaction.response.send_message(get_meme())

@client.tree.command(name="ping", description="Pings the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Latency: {round(client.latency * 1000)}ms")

@client.tree.command(name="embed", description="Sends an embedded message")
async def embed(interaction: discord.Interaction):

    embed = discord.Embed(title="Embedded Message", 
    description="This is an embedded message.", 
    color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=embed)

client.run(TOKEN)

