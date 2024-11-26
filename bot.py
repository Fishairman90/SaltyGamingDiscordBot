import discord
from discord.ext import commands
import os

# Load the token and ensure no hidden characters
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    TOKEN = TOKEN.strip()

# Debugging: Log raw token
if not TOKEN:
    print("Token is missing. Please set the DISCORD_TOKEN environment variable.")
    raise ValueError("DISCORD_TOKEN environment variable is missing or invalid.")
else:
    print(f"Token loaded: {repr(TOKEN)}")  # Log raw token
    print(f"Token length: {len(TOKEN)}")

# Run the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print(f"LoginFailure Error: {e}")
    raise