import configparser
import json
import os

def load_config(conf_file='config.conf', json_file='config.json'):
    if os.path.exists(conf_file):
        print("DEBUG: Loading configuration from config.conf")
        config = configparser.ConfigParser()
        config.read(conf_file)
        return config, "conf"
    elif os.path.exists(json_file):
        print("DEBUG: Loading configuration from config.json")
        with open(json_file, 'r') as f:
            return json.load(f), "json"
    else:
        raise FileNotFoundError("No config file found! Ensure config.conf or config.json exists.")

# Load configuration
config, config_type = load_config()

if config_type == "conf":
    # Parse .conf file
    bot_token = config['Discord']['bot_token'].strip()
    role_to_group_map = dict(config.items('RoleToGroupMap'))
    print(f"DEBUG: Loaded bot token from .conf: {bot_token[:6]}...")
    print("DEBUG: RoleToGroupMap:", role_to_group_map)
elif config_type == "json":
    # Parse .json file
    bot_token = config['discord_bot_token']
    role_to_group_map = config['role_to_group_map']
    print(f"DEBUG: Loaded bot token from .json: {bot_token[:6]}...")
    print("DEBUG: RoleToGroupMap:", role_to_group_map)

# Placeholder for bot logic
try:
    print("DEBUG: Attempting to log in...")
    # Simulate login
    if not bot_token or bot_token == "your_discord_bot_token_here":
        raise ValueError("Improper token has been passed")
    print("INFO: Logged in successfully (placeholder)")
except Exception as e:
    print(f"ERROR - Error running the bot: {e}")
