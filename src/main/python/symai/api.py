from dotenv import load_dotenv
from dotenv import find_dotenv
import os


def apikey(): 
    load_dotenv(find_dotenv())
    api_key = os.environ.get("OPENAI_API_KEY")
    return api_key