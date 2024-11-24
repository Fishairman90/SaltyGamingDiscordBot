import discord
import mysql.connector
import json

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Discord bot setup
intents = discord.Intents.default()
intents.guilds = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# Run the bot
client.run(config["discord_bot_token"])
