# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy bot source code and default .conf file
COPY . .
COPY config.conf /app/config.conf

# Set entrypoint to the bot script
CMD ["python", "bot.py"]
