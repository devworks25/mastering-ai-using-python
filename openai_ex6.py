import os
from urllib import response
from dotenv import load_dotenv
from openai import OpenAI

#Load token
load_dotenv()
client = OpenAI(
 api_key=os.getenv("OPENAI_API_KEY")   
)

# Create a detailed prompt
prompt = """
Generate Product Description for SonciPro HeadPhone
Its should contains top level feature
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=100,
    temperature=2
)

print(response.choices[0].message.content)