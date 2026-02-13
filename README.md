# YouTube Mashup Generator

A full-stack web application that generates a music mashup from YouTube videos of a given singer.  
The system downloads videos, converts them to audio, trims them, merges them, and sends the final mashup to the user via email.

This project was developed as part of the Mashup Assignment.

---

## Features

- Download N YouTube videos of a singer
- Convert videos to audio
- Trim first Y seconds of each audio
- Merge all audio files into one mashup
- Send final mashup as ZIP via email
- Command Line Interface version
- Web App version (Flask)
- Background processing to prevent timeout
- Cloud deployment support (Render)

---

## Project Architecture

User Form → Flask Server → Background Processing  
→ Download Videos → Convert Audio → Trim → Merge  
→ Zip File → Email to User

---

## Project Structure

```
mashup-project/
│
├── mashup_core/          # Core mashup logic
│   ├── downloader.py
│   ├── audio_processor.py
│   └── merger.py
│
├── cli/                  # Command line program
│   └── <rollnumber>.py
│
├── webapp/               # Web application
│   ├── app.py
│   ├── utils.py
│   └── templates/
│       └── index.html
│
├── requirements.txt
├── render.yaml
├── README.md
```

---

## Technologies Used

- Python
- Flask
- yt-dlp (YouTube download)
- pydub (audio processing)
- moviepy
- ffmpeg
- SMTP (email service)
- Gunicorn
- Render (deployment)

---

## Local Setup

### 1. Clone repository

```
git clone <repo-url>
cd mashup-project
```

### 2. Create virtual environment

```
py -3.11 -m venv .venv
source .venv/Scripts/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install ffmpeg (required)

Download from:

```
https://www.gyan.dev/ffmpeg/builds/
```

Add ffmpeg to system PATH.

Verify installation:

```
ffmpeg -version
```

### 5. Setup environment variables

Create `.env` file in project root:

```
EMAIL=your_email@gmail.com
PASSWORD=your_gmail_app_password
```

Use a Gmail App Password, not your normal Gmail password.

### 6. Run Web App

```
cd webapp
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## Command Line Usage

```
python <rollnumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFile>
```

Example:

```
python 102303170.py "Karan Aujla" 20 25 output.mp3
```

---

## Web App Usage

User provides:

- Singer name
- Number of videos
- Duration (seconds)
- Email address

The system generates the mashup in the background and sends a ZIP file via email.

---

## Deployment (Render)

1. Push project to GitHub  
2. Create a new Web Service on Render  
3. Set environment variables:

```
EMAIL=your_email
PASSWORD=your_app_password
PYTHON_VERSION=3.11.9
```

4. Start command:

```
gunicorn webapp.app:app
```

---

## Important Notes

- Python 3.11 is required for pydub compatibility
- ffmpeg is required for audio processing
- Background processing prevents timeout issues
- `.env` file should never be pushed to GitHub

---

## Assignment Requirements Covered

- Python CLI Mashup Program
- Web Service Implementation
- YouTube Video Download
- Audio Conversion and Trimming
- Audio Merging
- Email Delivery of Result

---

## Author
Vishwas Khattar
