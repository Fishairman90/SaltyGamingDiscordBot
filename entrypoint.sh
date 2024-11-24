#!/bin/bash

# Ensure the config directory exists
mkdir -p /app/config

# If config.conf doesn't exist in the mapped directory, copy the default
if [ ! -f /app/config/config.conf ]; then
  echo "Copying default config.conf to /app/config"
  cp /defaults/config.conf /app/config/config.conf
fi

# Start the bot
exec "$@"
