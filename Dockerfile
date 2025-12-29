FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir aiogram

COPY bot.py ./

CMD ["python", "bot.py"]

