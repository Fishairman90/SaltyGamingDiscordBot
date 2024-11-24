import configparser

# Load the .conf file
def load_config(file_path='config.conf'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

# Load configuration
config = load_config()

# Access Discord bot token
bot_token = config['Discord']['bot_token']

# Access database settings
db_host = config['Database']['host']
db_user = config['Database']['user']
db_password = config['Database']['password']

# Access role-to-group mapping
role_to_group_map = dict(config.items('RoleToGroupMap'))

# Function to get group for a role ID
def get_group_for_role(role_id):
    return role_to_group_map.get(role_id, None)

# Example: test output for a role
test_role_id = "1050611380086112326"
print(f"Group for role {test_role_id}: {get_group_for_role(test_role_id)}")

# Additional bot logic goes here...
