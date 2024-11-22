
import os
import discord
from discord.ext import commands
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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

# Role-to-permission mapping
ROLE_TO_GROUP_MAP = {
    "123456789012345678": "Admin",
    "987654321098765432": "Moderator"
}

# Initialize bot with intents
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f"Bot logged in as {bot.user}")
    for guild in bot.guilds:
        logging.info(f"Connected to guild: {guild.name} with {len(guild.members)} members")

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        logging.info(f"Role change detected for {after.name}")
        added_roles = [role.name for role in after.roles if role not in before.roles]
        removed_roles = [role.name for role in before.roles if role not in after.roles]
        logging.info(f"Added roles: {added_roles}")
        logging.info(f"Removed roles: {removed_roles}")
        # Add further handling logic here

@bot.command()
async def test(ctx):
    guild = ctx.guild
    members = guild.members
    for member in members:
        logging.info(f"{member.name}: {[role.name for role in member.roles]}")

try:
    bot.run(TOKEN)
except Exception as e:
    logging.error(f"Error running the bot: {e}")
