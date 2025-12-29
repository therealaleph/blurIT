# Telegram Video Blur Bot

**Live Bot:** [@bluritbot](https://t.me/bluritbot)

A professional Telegram bot that blurs videos with customizable blur percentage.

## Features

- Receive video files from users
- Apply Gaussian blur with configurable intensity (1-100%)
- Preserves audio and video quality
- Async processing for fast performance

## Setup

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Telegram bot token:
```
TELEGRAM_BOT_TOKEN=your_token_here
```

3. Start with Docker Compose:
```bash
docker-compose up -d
```

## Usage

1. Send `/start` to the bot
2. Send a video file
3. Enter blur percentage (1-100)
4. Receive the blurred video

