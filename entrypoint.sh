#!/bin/bash

# Debug: List contents of /app before starting
echo "DEBUG: Listing contents of /app"
ls -l /app

# Ensure the config directory exists
mkdir -p /app/config

# If config.conf doesn't exist in the mapped directory, copy the default
if [ ! -f /app/config/config.conf ]; then
    echo "Copying default config.conf to /app/config"
    cp /defaults/config.conf /app/config/config.conf
fi

# Debug: List contents of /app/config
echo "DEBUG: Listing contents of /app/config"
ls -l /app/config

# Start the bot
exec python /app/bot.py
