import os
from langchain_ollama import ChatOllama

# 1. Path to your local file
file_path = "sample_log.txt"

print(f"📄 Reading local file: {file_path}...")

# Check if the file exists before opening it
if not os.path.exists(file_path):
    print(f"❌ Error: Could not find {file_path}")
    exit()

with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# 2. Set up your local Llama model
print("🤖 Initializing local Llama...")
llm = ChatOllama(model="llama3.2", temperature=0)

# 3. Create a clean instruction for the AI (The Prompt)
question = "What caused the ERROR in these logs, and what time did it happen?"

prompt = f"""
You are an expert log analyzer. Below is the content of a local file.
Please read it carefully and answer the user's question based strictly on the content provided.

---
FILE CONTENT:
{file_content}
---

QUESTION: {question}
"""

# 4. Run the model
print("🧠 Local AI is analyzing the file contents...")
response = llm.invoke(prompt)

print("\n✨ AI Analysis Response:")
print(response.content)
