from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import whisper
import os
from gpt4free import usesless
app = Flask(__name__)
api_key = "5588257c8b7ce1107f7b7f374eef211d"
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
    file_name = "prompt.mp3"

    # Save the audio file
    audio_file.save(os.path.join(save_path, file_name))

    result = model.transcribe("prompt.mp3")
    transcription = result["text"]

    return transcription

id = "chatcmpl-7GwNVB25cgHQzEtDOpWXXWLHA1iGA"
@app.route('/ask_question', methods=['POST'])
def ask_question():
    message_id = id
    question = request.json.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    req = usesless.Completion.create(prompt=question, parentMessageId=message_id)
    answer = req['text']
    message_id = req["id"]

    return jsonify({'answer': answer, "id": message_id})


if __name__ == '__main__':
    app.run(port=5100, debug=True)
