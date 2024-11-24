
# Salty Gaming Discord Bot

A Discord bot to sync roles with Ark Survival Ascended in-game permissions using a MySQL database.

## Features
- Sync Discord roles with in-game permissions.
- Add/remove permissions dynamically based on role changes.
- Dockerized for easy deployment.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/salty_gaming_discord_bot.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your configuration in `config.json`.

4. Run the bot:
   ```bash
   python bot.py
   ```

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t saltygaming-discord-bot .
   ```

2. Run the container:
   ```bash
   docker run -d --name saltygaming-bot saltygaming-discord-bot
   ```

## Configuration
- Update `config.json` with:
  - Your Discord bot token.
  - Database credentials for Ark Discord and Ark Permissions databases.
  - Role-to-permission mapping.

---

### Contributing
Contributions are welcome! Please submit a pull request with your changes.

### License
MIT
