from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

llm = Ollama(
    model="llama3.1:latest", 
    request_timeout=120.0
)

# Single query
resp = llm.complete("Who is Paul Graham")

# Call Chat with list of messages
messages = [
    ChatMessage(role="system", content="You are a pirate with a colorful personality"),
    ChatMessage(role="user", content="What is your name")
]
resp = llm.chat(messages)

# Stream complete
resp = llm.stream_complete ("Who is Paul Graham")

for r in resp:
    print(r.delta, end=" ")