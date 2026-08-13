import os
from urllib import response
from dotenv import load_dotenv
from openai import OpenAI

#Load Env var

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define a multi-line prompt to classify sentiment
# prompt = """Classify sentiment as 1-5 (negative to positive):
# 1. Unbelievably good!
# 2. Shoes fell apart on the second use.
# 3. The shoes look nice, but they aren't very comfortable.
# 4. Can't wait to show them off!"""

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role":"user","content":prompt}],
#     max_completion_tokens=100
# )

# print(response.choices[0].message.content)



#Another Example of short prompting

# Add the example to the prompt
# prompt = """Classify sentiment as 1-5 (negative to positive):
# 1. Love these! = 5
# 2. Unbelievably good! = 4
# 3. Shoes fell apart on the second use.=3
# 4. The shoes look nice, but they aren't very comfortable.=2
# 5. Can't wait to show them off! =1"""

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role":"user","content":prompt}],
#     max_completion_tokens=100
# )

# print(response.choices[0].message.content)


#Add another prompt

# Add the final example
prompt = """Classify sentiment as 1-5 (negative to positive):
1. but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 4
4. Shoes fell apart on the second use. = 1
5. The shoes look nice, but they aren't very comfortable. = 2
6. Can't wait to show them off! =3 """

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)