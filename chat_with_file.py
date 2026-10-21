import os
from langchain_ollama import ChatOllama

# 1. Path to your local file
file_path = "sample_log.txt"

if not os.path.exists(file_path):
    print(f"❌ Error: Could not find {file_path}")
    exit()

print(f"📄 Loading local file: {file_path}...")
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# 2. Set up your local Llama model
print("🤖 Initializing local Llama...")
llm = ChatOllama(model="llama3.2", temperature=0)

print("\n🚀 Interactive Session Started!")
print("Type your questions about the file below. Type 'exit' to quit.\n")

# 3. The Interactive Loop
while True:
    # Get user input right from the terminal
    user_question = input("❓ Ask something about the file: ")
    
    # Check if the user wants to leave
    if user_question.lower().strip() == 'exit':
        print("👋 Exiting session. Goodbye!")
        break
        
    # Skip empty inputs
    if not user_question.strip():
        continue

    # Construct the instruction template dynamically
    prompt = f"""
    You are an AI assistant analyzing a local file. Use the following file content to accurately answer the question.
    
    ---
    FILE CONTENT:
    {file_content}
    ---
    
    QUESTION: {user_question}
    """
    
    print("🧠 Thinking...")
    response = llm.invoke(prompt)
    
    print(f"\n✨ AI Response:\n{response.content}\n")
    print("-" * 50)
