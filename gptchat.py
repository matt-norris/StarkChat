from flask import Flask, request
from flask_cors import CORS, cross_origin
import whisper
import os
app = Flask(__name__)

model = whisper.load_model("small")
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/transcribe', methods=['POST'])
@cross_origin()
def transcribe_audio():
    if 'audio' not in request.files:
        return 'No audio file in request', 400

    audio_file = request.files['audio']

    # Define a directory path to save the audio files
    save_path = "/Users/mattnorris/Desktop/Files/Personal Projects/StarkChat2/"

    # Use the current timestamp to create a unique file name for each audio file
    file_name = str(1) + ".mp3"

    # Save the audio file
    audio_file.save(os.path.join(save_path, file_name))

    result = model.transcribe("1.mp3")
    transcription = result["text"]

    return transcription


if __name__ == '__main__':
    app.run(port=5100, debug=True)
