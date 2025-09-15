from youtube_transcript_api import YouTubeTranscriptApi
import os
import whisper

def transcribe_audio(audio_file: str, transcript_file: str) -> bool:
    """Transcribe audio file to text using Whisper."""
    try:
        print("🎤 Running Whisper transcription...")
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file not found: {audio_file}")
            
        model = whisper.load_model("base")
        result = model.transcribe(audio_file)
        
        os.makedirs(os.path.dirname(transcript_file), exist_ok=True)
        with open(transcript_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
            
        print(f"✅ Transcript saved to {transcript_file}")
        return True
    except Exception as e:
        print(f"❌ Error during Whisper transcription: {e}")
        return False

def save_youtube_transcript(video_id: str, output_file: str) -> bool:
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        api = YouTubeTranscriptApi()
        transcript_snippets = api.fetch(video_id)
        transcript_text = "\n".join(snippet.text for snippet in transcript_snippets)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript_text)
        print(f"Transcript saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return False