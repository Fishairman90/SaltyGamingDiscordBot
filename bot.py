
import os
import discord
from discord.ext import commands

# Read environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
DB_CONFIG_ARK_DISCORD = {
    "host": os.getenv("DB_DISCORD_HOST"),
    "user": os.getenv("DB_DISCORD_USER"),
    "password": os.getenv("DB_DISCORD_PASSWORD"),
    "database": os.getenv("DB_DISCORD_NAME"),
}
DB_CONFIG_ARK_PERMISSIONS = {
    "host": os.getenv("DB_PERMISSIONS_HOST"),
    "user": os.getenv("DB_PERMISSIONS_USER"),
    "password": os.getenv("DB_PERMISSIONS_PASSWORD"),
    "database": os.getenv("DB_PERMISSIONS_NAME"),
}
ROLE_TO_GROUP_MAP = {
    "123456789012345678": "Admin",
    "987654321098765432": "Moderator",
}

# Initialize bot with proper intents
intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Error running the bot: {e}")
