# SYMAI

SYMAI (Speak Your Mind AI) is a conversational AI that uses speech recognition, natural language processing and GPT-3 to interact with users. 

The system takes the user's speech as input, converts it to text using a speech-to-text service, processes the text using GPT-3, then generates a response, which is then converted to speech using a text-to-speech service. The system also utilizes OpenAI's API to access GPT-3.

## Requirements
- Python 3.6 or higher
- OpenAI API key
- SpeechRecognition
- gTTS

## Installation
1. Clone the repository
git clone https://github.com/Jubbery/symai.git

2. Create a virtual environment
python3 -m venv venv

3. Activate the virtual environment
source venv/bin/activate

4. Install the dependencies
pip install -r requirements.txt