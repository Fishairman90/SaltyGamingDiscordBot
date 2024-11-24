FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Ensure /app/config exists and contains default configuration
RUN mkdir -p /app/config && cp config.conf /app/config/config.conf

# Expose necessary ports (optional)
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]
