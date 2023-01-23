import speech_recognition as sr
from dotenv import load_dotenv
from dotenv import find_dotenv
import os
import openai

def userVoice():
    load_dotenv(find_dotenv())
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Set up SpeechRecognition microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Listen for user speech
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Convert speech to text
    speech_text = recognizer.recognize_google(audio)

    # Send text to Whisper API and get response
    openai.api_key = api_key
    print(openai.api_key)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"whisper {speech_text}",
    )
    return response["choices"][0]["text"]
