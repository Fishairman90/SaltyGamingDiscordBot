# Use Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy required files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port if needed
EXPOSE 8080

# Command to run the bot
CMD ["python", "bot.py"]
