from flask import Flask, request
from flask_cors import CORS, cross_origin
import whisper
import librosa
import numpy as np
from tempfile import NamedTemporaryFile

app = Flask(__name__)

model = whisper.load_model("base")
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/transcribe', methods=['POST'])
@cross_origin()
def transcribe_audio():
    if 'audio' not in request.files:
        return 'No audio file in request', 400

    audio_file = request.files['audio']

    # Create a temporary file and save the audio data into it
    temp_file = NamedTemporaryFile(delete=False)
    audio_file.save(temp_file.name)

    # Use librosa to load the temporary audio file into a numpy array
    audio_data, _ = librosa.load(temp_file.name, sr=None, mono=True)
    audio_data = np.array(audio_data, dtype=np.float32)

    result = model.transcribe(audio_data)
    transcription = result["text"]

    return transcription


if __name__ == '__main__':
    app.run(port=5100, debug=True)
