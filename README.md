# Salty Gaming Discord Bot

## Overview
The Salty Gaming Discord Bot synchronizes Discord roles with in-game permissions for Ark: Survival Ascended. It now uses a `.conf` file for configuration.

## Configuration

1. **Edit the Configuration File**:
   Locate the `config.conf` file and edit the following sections:
   - `[Discord]`: Add your bot token.
   - `[Database]`: Add your database credentials.
   - `[RoleToGroupMap]`: Map Discord role IDs to in-game group names.

   Example:
   ```ini
   [Discord]
   bot_token = your_discord_bot_token_here

   [Database]
   host = localhost
   user = root
   password = password

   [RoleToGroupMap]
   809576516068704267 = Birthday
   842104928855523339 = Nitro
   ```

2. **Run the Bot**:
   Build and run the bot using Docker:
   ```bash
   docker build -t saltygaming-discord-bot .
   docker run -d --name saltygaming-bot \
       -v /path/to/local/config.conf:/app/config.conf \
       saltygaming-discord-bot
   ```

3. **Restart After Changes**:
   If you edit `config.conf`, restart the bot:
   ```bash
   docker restart saltygaming-bot
   ```

## Features
- Synchronizes Discord roles with in-game permissions.
- Easy-to-edit `.conf` file for all configuration.
- Dockerized for streamlined deployment.

## Contributing
Feel free to contribute by submitting pull requests or opening issues on GitHub.
