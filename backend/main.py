from transcript_extractor import save_youtube_transcript
from summary_generator import generate_summary

def main():
    video_id = "07BVxmVFDGY"
    transcript_file = "transcript.txt"
    summary_file = "summary.txt"

    # Step 1: Extract and save transcript
    print("Extracting transcript...")
    save_youtube_transcript(video_id, transcript_file)
    print("Transcript extraction complete.")

    # Step 2: Generate summary and save to file
    print("Generating summary. This may take a moment, please wait...")
    generate_summary(transcript_file, summary_file)
    print("Summary generation complete.")

if __name__ == "__main__":
    main()