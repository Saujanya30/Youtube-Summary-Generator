from youtube_transcript_api import YouTubeTranscriptApi
import os

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