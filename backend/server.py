from flask import Flask, jsonify, request
from flask_cors import CORS
from transcript_extractor import save_youtube_transcript
from summary_generator import generate_summary

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the YouTube Summary API!"})

@app.route('/summary', methods=['POST'])
def create_summary():
    try:
        data = request.get_json()
        video_url = data.get('url')
        
        # Extract video ID from URL
        video_id = video_url.split('v=')[-1]
        transcript_file = f"transcript_{video_id}.txt"
        summary_file = f"summary_{video_id}.txt"

        # Generate transcript and summary
        save_youtube_transcript(video_id, transcript_file)
        generate_summary(transcript_file, summary_file)
        
        return jsonify({
            "message": "Summary generation initiated",
            "video_id": video_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/summary/<video_id>', methods=['GET'])
def get_summary(video_id):
    try:
        with open(f"summary_{video_id}.txt", 'r') as file:
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