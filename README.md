# YouTube Video Summarizer

AI-powered web application that generates concise summaries of YouTube videos by transcribing audio and using Llama AI model.

## Features

- YouTube video audio extraction and transcription
- AI-powered summary generation
- RESTful API with easy-to-use frontend interface

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js and npm
- Ollama with model llama3.1:8b
- ffmpeg
- yt-dlp

### Installation

1. Clone and setup backend:
```bash
git clone <repository-url>
cd YoutubeSummary/backend
pip install -r requirements.txt
```

2. Start Ollama:
```bash
ollama run llama3.1:8b
```

3. Run backend server(Optional: this can be run from step 4):
```bash
python server.py
```

4. Start frontend development server:
```bash
cd ../frontend
npm install
npm run dev
```

The application will be available at `http://localhost:5173`

## Project Structure

```
YoutubeSummary/
├── frontend/          # React frontend application
├── backend/           # Python Flask backend
    ├── OutputFiles/   # Generated transcripts and summaries
    ├── logs/         # Application logs
    └── requirements.txt
```

## API Endpoints

- POST `/summary` - Create new summary
- GET `/summary/<video_id>` - Retrieve generated summary