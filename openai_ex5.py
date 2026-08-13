import os
from dotenv import load_dotenv
from openai import OpenAI

#Load env var

load_dotenv()
client = OpenAI(
    api_key=os.getenv("getOPENAI_API_KEY")
)

# prompt=f"""Replace car with plane and adjust phrase:
# A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

prompt = f"""Summarize the following text into two concise bullet points:
{"GDP of India"}"""

# Send request
response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        max_completion_tokens=400
)

print(response.choices[0].message.content)