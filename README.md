# BlurIT - Video Blur Tool

A professional tool for blurring videos with customizable blur percentage. Available in three different ways to suit your needs.

## Features

- Apply Gaussian blur with configurable intensity (1-100%)
- Real-time preview of blur effect (HTML version)
- Preserves audio and video quality
- Multiple deployment options
- Bilingual interface (English & Persian)

## Usage Methods

### 1. Live Bot (Easiest)

Use our hosted Telegram bot - no setup required!

**Live Bot:** [@bluritbot](https://t.me/bluritbot)

#### Usage

1. Open Telegram and search for [@bluritbot](https://t.me/bluritbot)
2. Send `/start` to the bot
3. Send a video file
4. Enter blur percentage (1-100)
5. Receive the blurred video

**Pros:**
- No setup required
- Works on any device with Telegram
- No installation needed

---

### 2. Docker Local (Self-Hosted Bot)

Run your own Telegram bot instance locally using Docker.

#### Prerequisites

- Docker and Docker Compose installed

#### Setup

1. Clone this repository:
```bash
git clone https://github.com/therealaleph/blurIT.git
cd blurIT
```

2. Copy the example environment file:
```bash
cp .env.example .env
```

3. Edit `.env` and add your Telegram bot token:
```
TELEGRAM_BOT_TOKEN=your_token_here
```

4. Start with Docker Compose:
```bash
docker-compose up -d
```

#### Usage

1. Send `/start` to your bot
2. Send a video file
3. Enter blur percentage (1-100)
4. Receive the blurred video

**Pros:**
- Full control over your bot
- Private instance
- No dependency on external services

**Cons:**
- Requires Docker setup
- Needs Telegram bot token
- Must keep server running

---

### 3. HTML Local (Fully Offline)

A completely offline HTML application that runs entirely in your browser. No internet, no server, no uploads required.

#### Features

- **100% Local Processing** - Everything runs in your browser
- **No Internet Required** - Works completely offline
- **Privacy First** - Your videos never leave your device
- **Real-time Preview** - See blur effect before processing
- **Auto-download** - Processed videos download automatically
- **WEBM Output** - Outputs in WEBM format (can be converted to MP4 online)

#### Browser Compatibility

- Chrome (Recommended)
- Firefox
- Edge
- Safari (Not supported)

#### Usage

1. Open `local-version/index.html` in a compatible browser
2. Click or drag a video file to upload
3. Adjust blur intensity using the slider (1-100%)
4. Click "Blur Video" to process
5. Video will automatically download as WEBM format

#### Converting WEBM to MP4

Since the tool outputs WEBM format, you can use these online converters to convert to MP4:

- [CloudConvert](https://cloudconvert.com/webm-to-mp4)
- [FreeConvert](https://www.freeconvert.com/webm-to-mp4)
- [Online-Convert](https://video.online-convert.com/convert/webm-to-mp4)

**Pros:**
- Completely offline
- No setup required
- Maximum privacy
- Works on any device with a browser
- Real-time preview

**Cons:**
- Outputs WEBM format (needs conversion for MP4)
- Safari not supported
- Processing happens in browser (may be slower for large videos)

---

## Comparison

| Feature | Live Bot | Docker Local | HTML Local |
|---------|----------|--------------|------------|
| Setup Required | No | Yes | No |
| Internet Required | Yes | Yes | No |
| Privacy | Medium | High | Maximum |
| Output Format | MP4 | MP4 | WEBM |
| Real-time Preview | No | No | Yes |
| Works Offline | No | No | Yes |
| Browser Support | Any (Telegram) | Any (Telegram) | Chrome/Firefox/Edge |

## Credits

**By:** [Shin](https://github.com/therealaleph)

- **Source Code:** [GitHub Repository](https://github.com/therealaleph/blurIT)
- **Website:** [sh1n.org](https://sh1n.org)

## License

This project is open source and available for use.
