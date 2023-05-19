# Stark Chat: An Interactive GPT ChatBot that acts and sounds like Tony Stark

This project is a voice-activated AI Chatbot that replicates Tony Stark from the Avengers movies. The application integrates several state-of-the-art technologies to create a natural, intuitive user interface, providing a highly engaging user experience.

## Key Technologies

### Whisper: 
Developed by OpenAI, Whisper is an automatic speech recognition (ASR) system that transcribes spoken language into text. This enables users to interact with the chatbot through either typing or speaking, enhancing both accessibility and usability.

### GPT (Generative Pre-trained Transformer): 
GPT is a powerful language understanding AI model developed by OpenAI. The model understands context, generates human-like text, and provides insightful answers to user queries.

### Eleven Labs' Text-to-Speech service: 
GPT generated responses are converted into lifelike speech using Eleven Labs' Text-to-Speech service. This gives an auditory response to the user's query, simulating a natural conversation.

### Python/Flask: 
The backend of the application is built using Python and Flask, a lightweight web server framework that handles HTTP requests and responses. Flask endpoints facilitate the interaction between the user interface and the underlying ASR, AI, and Text-to-Speech services.

### JavaScript, HTML, and CSS: 
The frontend is built using JavaScript, HTML, and CSS. The UI is sleek and modern, with text input, audio recording, and audio playback functionality for seamless interaction with the Chatbot.
Getting Started

To use this chatbot, you'll need to sign up at Eleven Labs to obtain an API key. This key allows the chatbot to use Eleven Labs' Text-to-Speech service to generate lifelike speech.

You will also need to create a voice on Eleven Labs so that the chatbot will respond as Tony Stark. To train this voice, use the sample "" provided in the audio directory

## About the Project

This project demonstrates an innovative blend of technologies to create a conversational AI that can understand, generate, and vocalize language. The chatbot, role-playing as Tony Stark, delivers responses in his voice, further enhancing the user experience and giving Marvel fans a unique interaction opportunity.
![Stark Chat System Architecture](https://github.com/matt-norris/StarkChat/assets/97650920/721f73b9-0410-49a3-822e-f988abb96dd7)


## Installation

Before you can run the project, you need to make sure Python and Flask are installed on your machine. If you don't have them installed, you can download Python here and install Flask using pip:


```
pip install flask
```
Next, clone the repository to your local machine:

```
git clone https://github.com/matt-norris/starkchat.git
```
Install the required Python packages:

```
pip install -r requirements.txt
```
Make sure to replace "yourapikey" in the Python script with the API key you obtained from Eleven Labs.

## Usage

To start the server, navigate to the project directory and run:

```
python gptchat.py
```
The server will start on localhost:5300. Open your web browser and navigate to this address. You should see the chatbot interface. You can type your question in the input box or click the "Start Recording" button to ask your question verbally.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

I would like to express my gratitude to OpenAI for the GPT and Whisper models, and to Eleven Labs for their text-to-speech service. This project would not have been possible without these advanced technologies.
