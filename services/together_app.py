import os
from dotenv import load_dotenv
from together import Together

load_dotenv()

MODEL_NAME="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

# Qucik Response
resp = client.chat.completions.create (
    model=MODEL_NAME,
    messages=[
        {"role": "user", "content": "What is 2 and 2"}
    ],
)
print(resp.choices[0].message.content + "------\n")

# Stream response
stream = client.chat.completions.create (
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[
        {"role": "user", "content": "Tell me about Embeddings"}
    ],
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
print("-------\n")

