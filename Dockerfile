FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose necessary ports (optional)
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]
