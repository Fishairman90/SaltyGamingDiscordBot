FROM python:3.11-slim

WORKDIR /app

COPY bot.py .
COPY requirements.txt .
COPY .env .  # Ensure the .env file is copied

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]