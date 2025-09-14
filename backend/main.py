from transcript_extractor import save_youtube_transcript
from summary_generator import generate_summary
from pytube import YouTube

def download_audio(video_id, output_file="audio.mp3"):
    url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(filename=output_file)
    print(f"Audio downloaded as {output_file}")
    return output_file


def main():
    video_url = "https://www.youtube.com/watch?v=P0Fk-K2eZF8"
    video_id = video_url.split('v=')[-1]
    transcript_file = "transcript.txt"
    summary_file = "summary.txt"

    # Step 1: Extract and save transcript
    print("Extracting transcript...")
    if not save_youtube_transcript(video_id, transcript_file):
        print("Skipping summary generation (no transcript available).")
        return
    print("Transcript extraction complete.")

    # Step 2: Generate summary and save to file
    print("Generating summary. This may take a moment, please wait...")
    generate_summary(transcript_file, summary_file)
    print("Summary generation complete.")

if __name__ == "__main__":
    main()