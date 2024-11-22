
# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set an environment variable to disable buffering (optional)
ENV PYTHONUNBUFFERED=1

# Run the bot script
CMD ["python", "bot.py"]
