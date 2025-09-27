from youtube_transcript_api import YouTubeTranscriptApi
import os
import whisper
from pytubefix import YouTube
from pytubefix.cli import on_progress
from logger import setup_logger

logger = setup_logger(__name__)

def download_audio(url: str, output_dir: str) -> str:
    """Download audio from YouTube URL using yt-dlp."""
    try:
        output_file = os.path.join(output_dir, "audio.mp3")
        logger.info(f"Downloading audio from {url}")
        yt = YouTube(url, on_progress_callback=on_progress)
        
        ys = yt.streams.filter(only_audio=True).first()
        ys.download(output_path=output_dir, filename="audio.mp3")
        
        if os.path.exists(output_file):
            logger.info(f"Audio downloaded successfully: {output_file}")
            return output_file
        else:
            raise FileNotFoundError("Downloaded file not found")
            
    except Exception as e:
        logger.error(f"Failed to download audio: {e}")
        return ""
    
def transcribe_audio(audio_file: str, transcript_file: str) -> bool:
    """Transcribe audio file to text using Whisper."""
    try:
        logger.info("Starting Whisper transcription...")
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file not found: {audio_file}")
            
        model = whisper.load_model("base") # base model works fine, if you want better accuracy use "large", but it takes a lot of time.
        result = model.transcribe(audio_file)
        
        os.makedirs(os.path.dirname(transcript_file), exist_ok=True)
        with open(transcript_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
            
        logger.info(f"Transcript saved successfully: {transcript_file}")
        return True
    except Exception as e:
        logger.error(f"Transcription failed: {e}")
        return False

def save_youtube_transcript(video_id: str, output_file: str) -> bool:
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        api = YouTubeTranscriptApi()
        transcript_snippets = api.fetch(video_id)
        transcript_text = "\n".join(snippet.text for snippet in transcript_snippets)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript_text)
        logger.info(f"Transcript saved to {output_file}")
        return True
    except Exception as e:
        logger.error(f"Error fetching transcript: {e}")
        return False