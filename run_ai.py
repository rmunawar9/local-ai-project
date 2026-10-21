from langchain_ollama import ChatOllama

print("🤖 Connecting to local Ollama...")

# Initialize your local Llama model via LangChain
llm = ChatOllama(model="llama3.2", temperature=0)

print("🧠 Asking AI a question...")
response = llm.invoke("Give me a one-sentence cheer for successfully setting up my local AI environment!")

print("\n✨ AI Response:")
print(response.content)
