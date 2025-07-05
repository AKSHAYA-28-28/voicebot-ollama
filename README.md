# voicebot-ollama
A local voice assistant using Ollama and LLaMA 3
# 🎙️ VoiceBot Ollama — Your Offline AI Assistant with Voice

VoiceBot Ollama is a lightweight **offline voice assistant** that listens to your voice using your microphone, converts it to text, sends it to a local **LLaMA 3 model via Ollama**, and speaks the response aloud using natural speech.

No OpenAI key. No cloud. Just fast, private, local AI in Python.

---

#🚀 Features

- 🗣️ **Speech Recognition**: Converts your voice to text using Google STT
- 🧠 **AI-powered**: Sends your query to a locally running **LLaMA 3** via Ollama
- 🔊 **Text-to-Speech**: Speaks the AI’s response back to you
- 🔁 **Looping Assistant**: Keep chatting until you say “exit” or “stop”
- 💻 **Works Offline** (except Google STT)
- 🪶 Lightweight & easy to modify

---

#🧑‍💻 How It Works

1. You speak a query through the mic.
2. The script uses **Google SpeechRecognition** to transcribe it.
3. The transcribed query is sent to **Ollama’s REST API** running **llama3**.
4. The response is spoken aloud using **pyttsx3**.
5. The loop continues until you say **"exit"**.

---

#🧩 Dependencies

Install them via:

bash
pip install -r requirements.txt

If pyaudio gives errors, install it with:
pip install pipwin
pipwin install pyaudio


🛠️ Setup Instructions
Install Ollama
👉 https://ollama.com

Download the LLaMA 3 model

ollama run llama3
Run the bot

python voicebot.py
🎤 Talk to your bot!
Try:

"What’s the capital of Germany?"

"Tell me a joke"

"Define quantum computing"

Say "exit", "quit", or "stop" to end the session.

📁 Project Structure
voicebot-ollama/
├── voicebot.py         # Main script
├── requirements.txt    # Python dependencies
└── README.md           # Documentation (this file)


🔄 Future Upgrades (Ideas 💡)
- Wake-word detection ("Hey Jarvis")
- Streaming response from Ollama
- GUI with Streamlit / Gradio
- Local Whisper instead of Google STT (fully offline)
- Command execution (e.g., open apps, tell time)
- Dashboard to configure TTS rate, model, etc.

⚠️ Notes
Needs a working microphone

Requires internet access for Google Speech API (unless you switch to Whisper)

Ollama and LLaMA 3 must be installed locally

