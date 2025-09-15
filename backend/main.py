from transcript_extractor import save_youtube_transcript, transcribe_audio
from summary_generator import generate_summary
import os
import subprocess

def download_audio(url: str, output_dir: str, video_id: str) -> str:
    """Download audio from YouTube URL using yt-dlp."""
    try:
        output_file = os.path.join(output_dir, f"{video_id}_audio.mp3")
        command = [
            "yt-dlp",
            "--extract-audio",
            "-o", output_file,
            url
        ]
        subprocess.run(command, check=True)
        print(f"✅ Audio downloaded successfully as {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"❌ Error downloading audio: {e}")
        return ""

def main():
    # Use absolute paths to avoid path issues
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTPUT_DIR = os.path.join(BASE_DIR, "OutputFiles")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    video_url = "https://www.youtube.com/watch?v=P0Fk-K2eZF8"
    video_id = video_url.split('v=')[-1]
    
    # Define file paths using os.path.join
    transcript_file = os.path.join(OUTPUT_DIR, "transcript.txt")
    summary_file = os.path.join(OUTPUT_DIR, "summary.txt")
    
    # Download and process
    audio_file = download_audio(video_url, OUTPUT_DIR, video_id)
    if os.path.exists(audio_file):
        if transcribe_audio(audio_file, transcript_file):
            if os.path.exists(transcript_file):
                generate_summary(transcript_file, summary_file)
                print("✅ Processing complete!")
            else:
                print("❌ Transcript file not created")
        else:
            print("❌ Transcription failed")
    else:
        print("❌ Audio download failed")

if __name__ == "__main__":
    main()