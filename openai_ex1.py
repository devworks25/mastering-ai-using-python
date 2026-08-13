import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



# Send request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Why is learning the OpenAI API valuable for developers?"
        }
    ]
)

# Print response
print(response.choices[0].message.content)