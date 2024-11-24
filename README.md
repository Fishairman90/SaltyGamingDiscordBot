# SaltyGamingDiscordBot

## Configuration

The bot now uses a `.conf` file for configuration. An example file is provided below:

### Example `config.conf`:
```ini
[Discord]
Token = your-discord-bot-token

[Database]
Host = your-database-host
User = your-database-user
Password = your-database-password
Name = your-database-name

[RoleMappings]
HappyBirthday = birthday_permission_group
Moderator = mod_permission_group
Admin = admin_permission_group
```

### Setup Instructions

1. Copy `config.conf.example` to `config.conf`.
2. Edit `config.conf` with your credentials and role mappings.
3. Mount the file in Docker or place it in the project root.

## Running the Bot with Docker

### Build the Docker Image:
```bash
docker build -t saltygamingdiscordbot:latest .
```

### Run the Container:
```bash
docker run -d --name saltygaming-bot -v /path/to/config.conf:/app/config.conf saltygamingdiscordbot:latest
```
