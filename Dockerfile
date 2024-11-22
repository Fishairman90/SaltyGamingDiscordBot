
# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for mariadb-python and debugging
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb3 \
    libmariadb-dev-compat \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to disable buffering for real-time logs
ENV PYTHONUNBUFFERED=1

# Run the bot script
CMD ["python", "bot.py"]
