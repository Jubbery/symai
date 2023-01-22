import os
import openai
import openmic as userVoice

# Use the openai library to set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt for the Whisper model
prompt = (f"generate text given prompt: {userVoice()}")

# Use the openai library to generate text
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.7,
    max_tokens=2048
)

# Print the generated text
print(response["choices"][0]["text"])
