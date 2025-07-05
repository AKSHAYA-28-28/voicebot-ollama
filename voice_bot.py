import speech_recognition as sr
import pyttsx3
import requests

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# Text-to-Speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("🗣 You said:", text)
            return text
        except sr.UnknownValueError:
            print("😕 Could not understand.")
            return None
        except sr.RequestError:
            print("Could not request results.")
            return None

def ask_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        
        print(" Full response object:", response)
        print(" Response content:", response.text)  # <-- this line ensures it prints even if JSON is broken

        data = response.json()  # If this fails, we’ll see it in terminal

        if "response" in data:
            return data["response"]
        elif "error" in data:
            return f"Ollama error: {data['error']}"
        else:
            return "Unexpected response from Ollama."

    except Exception as e:
        print(" Error talking to Ollama:", e)
        return "Sorry, I couldn't process that."



def main():
    print("🤖 Voice Bot Ready! Say something...")
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() in ["exit", "quit", "stop"]:
                speak("Goodbye!")
                break
            response = ask_ollama(user_input)
            print("🤖 Bot:", response)
            speak(response)

if __name__ == "__main__":
    main()