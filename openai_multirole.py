from importlib.resources import contents
import os
from urllib import response
from dotenv import load_dotenv
from openai import OpenAI

#Load env

load_dotenv()
# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# prompt = [
#   {
#     "role": "system",
#     "content": "You are a study planning assistant that creates plans for learning new skills."
#   },
#   {
#     "role": "user",
#     "content": "I want to learn to speak Dutch."
#   }
# ]

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   max_completion_tokens=150,
#   messages= prompt
# )

# # Extract the assistant's text response
# print(response.choices[0].message.content)



#Another Prompt

sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
     {"role":"system","content":sys_msg},
     {"role":"user","content":"Help me learn to languages"}
  ]
)

print(response.choices[0].message.content)