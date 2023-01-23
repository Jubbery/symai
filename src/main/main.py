from python.symai.components.userVoice import userVoice
from python.symai.api import apikey

def main():   
   
    api_key = apikey()
    print(api_key)
    response = userVoice()
    print(response)