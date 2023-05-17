from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import whisper
import os
import requests
from gpt4free import you
import base64

app = Flask(__name__)

api_key_user = "YOUR ELEVEN LABS API KEY HERE"
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

chat = [{'question': "I want you to channel your inner Tony Stark from the Marvel Universe. I want your responses and answers to embody the charismatic, witty, and genius persona of Stark, using the tone, manner and vocabulary he would use. No need for explanatory notes. Just respond in pure Stark style. You must have a comprehensive understanding of Tony Stark's character traits. My first sentence is, “Hi Tony.”", 'answer': "Greetings, my friend. It's always a pleasure to hear from another genius such as myself. How can I assist you today?"}]


@app.route('/ask_question', methods=['POST'])
def ask_question():

    question = request.json.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    # simple request with links and details
    gptresponse = you.Completion.create(prompt=question, detailed=True, include_links=True,  chat=chat)
    chat.append({"question": question, "answer": gptresponse.text})

    # Converting to Voice stuff
    # CHUNK_SIZE = 1024
    # url = "https://api.elevenlabs.io/v1/text-to-speech/I4BiQB0HqUz18tjI4kWN"
    #
    # headers = {
    #     "Accept": "audio/mpeg",
    #     "Content-Type": "application/json",
    #     "xi-api-key": api_key
    # }
    #
    # data = {
    #     "text": gptresponse.text,
    #     "model_id": "eleven_monolingual_v1",
    #     "voice_settings": {
    #         "stability": 0,
    #         "similarity_boost": 0
    #     }
    # }
    #
    # response = requests.post(url, json=data, headers=headers)
    # with open('output.mp3', 'wb') as f:
    #    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
    #        if chunk:
    #            f.write(chunk)

    # Encode the audio file as base64
    with open('output.mp3', 'rb') as audio_file:
        audio_base64bytes = base64.b64encode(audio_file.read())
        audio_base64string = audio_base64bytes.decode('utf-8')

    return jsonify({'answer': gptresponse.text, 'audio': audio_base64string})
    # return jsonify({'answer': gptresponse.text, 'audio': audio_base64string})


if __name__ == '__main__':
    app.run(port=5300, debug=True)
