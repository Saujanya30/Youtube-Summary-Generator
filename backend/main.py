from transcript_extractor import save_youtube_transcript
from summary_generator import generate_summary
import os

def main():
    OUTPUT_DIR = "OutputFiles"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    video_url = "https://www.youtube.com/watch?v=P0Fk-K2eZF8"
    video_id = video_url.split('v=')[-1]
    
    transcript_file = f"{OUTPUT_DIR}/transcript.txt"
    summary_file = f"{OUTPUT_DIR}/summary.txt"

    print("Processing video...")
    if save_youtube_transcript(video_id, transcript_file):
        generate_summary(transcript_file, summary_file)
        print("Processing complete!")
    else:
        print("Failed to process video - no transcript available.")

if __name__ == "__main__":
    main()