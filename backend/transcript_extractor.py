from youtube_transcript_api import YouTubeTranscriptApi

def save_youtube_transcript(video_id, output_file='transcript.txt'):
    try:
        api = YouTubeTranscriptApi()
        transcript_snippets = api.fetch(video_id)
        transcript_text = "\n".join(snippet.text for snippet in transcript_snippets)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript_text)
        print(f"Transcript saved to {output_file}")
        return True
    except Exception as e:
        print("Error fetching transcript:", e)
        return False
