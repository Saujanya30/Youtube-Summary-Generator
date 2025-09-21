from youtube_transcript_api import YouTubeTranscriptApi
import os
import whisper
import subprocess
from logger import setup_logger

logger = setup_logger(__name__)

def download_audio(url: str, output_dir: str, video_id: str) -> str:
    """Download audio from YouTube URL using yt-dlp."""
    try:
        output_file = os.path.join(output_dir, f"{video_id}_audio.wav.webm")
        logger.info(f"Downloading audio from {url}")
        command = [
            "yt-dlp",
            "--audio-format", "wav",
            "-o", output_file,
            url
        ]
        subprocess.run(command, check=True)
        logger.info(f"Audio downloaded successfully: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to download audio: {e}")
        return ""
    
def transcribe_audio(audio_file: str, transcript_file: str) -> bool:
    """Transcribe audio file to text using Whisper."""
    try:
        logger.info("Starting Whisper transcription...")
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file not found: {audio_file}")
            
        model = whisper.load_model("base")
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