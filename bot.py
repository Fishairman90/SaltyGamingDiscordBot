import discord
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the token from the environment
import os
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable is not set.")

# Initialize the Discord client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f"We have logged in as {client.user}")

# Run the bot
client.run(TOKEN)
