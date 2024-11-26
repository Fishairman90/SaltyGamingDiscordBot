import discord
from discord.ext import commands
import pymysql
import os

# Load configuration from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable is missing or invalid.")

MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
ARK_DISCORD_DB = os.getenv("ARK_DISCORD_DB", "ark_discord")
ARK_ASA_PERMISSIONS_DB = os.getenv("ARK_ASA_PERMISSIONS_DB", "ark_asa_permissions")

# Debug: Print loaded token type and partial value
print(f"Discord Token Loaded: {TOKEN[:10]}...")  # Avoid exposing full token
print(f"Token type: {type(TOKEN)}")

# Discord setup
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# MySQL connection setup
def get_db_connection(db_name):
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

# Remaining bot logic...
bot.run(TOKEN)