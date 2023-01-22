import speech_recognition as sr
import openai

def userVoice():
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
    openai.api_key = "YOUR_API_KEY"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"whisper {speech_text}",
    )
    return response["choices"][0]["text"]
