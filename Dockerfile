FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files to the container
COPY . /app

# Ensure the config directory exists
RUN mkdir -p /app/config

# Copy default configuration files to the config directory
COPY config.conf /app/config/config.conf

# Install dependencies
RUN pip install -r requirements.txt

# Expose necessary ports (optional)
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]
