from flask import Flask, jsonify, request
from flask_cors import CORS
from transcript_extractor import save_youtube_transcript, transcribe_audio, download_audio
from summary_generator import generate_summary
import os
from logger import setup_logger

logger = setup_logger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Use absolute paths to avoid path issues
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "OutputFiles")
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the YouTube Summary API!"})

@app.route('/summary', methods=['POST'])
def create_summary():
    try:
        data = request.get_json()
        video_url = data.get('url')

        logger.info(f"Processing summary request for {video_url}")
        
        # Extract video ID from URL
        video_id = video_url.split('v=')[-1]
        transcript_file = os.path.join(OUTPUT_DIR, f"transcript_{video_id}.txt") 
        summary_file = os.path.join(OUTPUT_DIR, f"summary_{video_id}.txt")

        try:
            # Download audio
            logger.info(f"Downloading audio for video {video_id}")
            audio_file = download_audio(video_url, OUTPUT_DIR, video_id)
            logger.info(f"Audio downloaded to {audio_file}")
        except Exception as e:
            logger.error(f"Audio download failed: {e}")
            return jsonify({"error": f"Audio download failed: {str(e)}"}), 500

        try:
            # Generate transcript
            logger.info(f"Transcribing audio for video {video_id}")
            transcribe_audio(audio_file, transcript_file)
            logger.info(f"Transcript saved to {transcript_file}")
        except Exception as e:
            logger.error(f"Transcription failed: {e}")
            return jsonify({"error": f"Transcription failed: {str(e)}"}), 500

        try:
            # Generate summary
            logger.info(f"Generating summary for video {video_id}")
            generate_summary(transcript_file, summary_file)
            logger.info(f"Summary saved to {summary_file}")
        except Exception as e:
            logger.error(f"Summary generation failed: {e}")
            return jsonify({"error": f"Summary generation failed: {str(e)}"}), 500
        
        logger.info(f"Summary generation completed for video {video_id}")
        return jsonify({
            "message": "Summary generation initiated",
            "video_id": video_id
        }), 201
    except Exception as e:
        logger.error(f"Summary generation failed: {e}")
        return jsonify({"error": str(e)}), 400

@app.route('/summary/<video_id>', methods=['GET'])
def get_summary(video_id):
    try:
        summary_file = os.path.join(OUTPUT_DIR, f"summary_{video_id}.txt")
        with open(summary_file, 'r') as file:
            summary = file.read()
        return jsonify({
            "video_id": video_id,
            "summary": summary
        })
    except FileNotFoundError:
        return jsonify({
            "error": "Summary not found"
        }), 404

if __name__ == '__main__':
    app.run(debug=True)