import os
from dotenv import load_dotenv
from openai import OpenAI

#Load Env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)