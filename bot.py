import discord
from discord.ext import commands
import pymysql
import asyncio
import os

# Load configuration
TOKEN = os.getenv("DISCORD_TOKEN")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
ARK_DISCORD_DB = os.getenv("ARK_DISCORD_DB")
ARK_ASA_PERMISSIONS_DB = os.getenv("ARK_ASA_PERMISSIONS_DB")

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

# Helper functions
def update_permissions(eos_id, permission, add=True):
    conn = get_db_connection(ARK_ASA_PERMISSIONS_DB)
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT PermissionGroups FROM ark_asa_permissions WHERE EOS_Id = %s", (eos_id,))
            result = cursor.fetchone()
            current_permissions = result['PermissionGroups'].split(',') if result and result['PermissionGroups'] else []

            if add and permission not in current_permissions:
                current_permissions.append(permission)
            elif not add and permission in current_permissions:
                current_permissions.remove(permission)

            updated_permissions = ','.join(current_permissions)
            cursor.execute("UPDATE ark_asa_permissions SET PermissionGroups = %s WHERE EOS_Id = %s", (updated_permissions, eos_id))
            conn.commit()
    finally:
        conn.close()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")

@bot.event
async def on_member_update(before, after):
    conn = get_db_connection(ARK_DISCORD_DB)
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Eos_Id FROM ark_discord WHERE DiscordId = %s", (after.id,))
            player = cursor.fetchone()
            if not player:
                return
            eos_id = player['Eos_Id']

        added_roles = set(after.roles) - set(before.roles)
        removed_roles = set(before.roles) - set(after.roles)

        for role in added_roles:
            update_permissions(eos_id, role.name, add=True)

        for role in removed_roles:
            update_permissions(eos_id, role.name, add=False)

    finally:
        conn.close()

bot.run(TOKEN)