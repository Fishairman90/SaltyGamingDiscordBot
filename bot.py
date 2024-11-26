import discord
from discord.ext import commands
import pymysql
import json
import os

# Load configuration
CONFIG_PATH = os.getenv("CONFIG_PATH", "config.json")
try:
    with open(CONFIG_PATH, 'r') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    raise FileNotFoundError(f"Configuration file not found at {CONFIG_PATH}")
except json.JSONDecodeError:
    raise ValueError(f"Invalid JSON format in configuration file: {CONFIG_PATH}")

# Debugging: Print loaded config (avoid printing sensitive values in production)
print(f"Loaded configuration: {config}")

TOKEN = config.get("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is missing or invalid in config.json")

print(f"Discord Token Loaded: {TOKEN[:10]}...")  # Debug token (partial)

MYSQL_HOST = config["MYSQL_HOST"]
MYSQL_USER = config["MYSQL_USER"]
MYSQL_PASSWORD = config["MYSQL_PASSWORD"]
ARK_DISCORD_DB = config["ARK_DISCORD_DB"]
ARK_ASA_PERMISSIONS_DB = config["ARK_ASA_PERMISSIONS_DB"]

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