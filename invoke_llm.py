
from langchain_ollama import OllamaLLM

# Initialize the Ollama Llama 3.1 model
llm = OllamaLLM(model="llama3.1")

# Example prompt
prompt = "What is business intelligence?"

# Invoke the model
response = llm.invoke(prompt)
print("Response:", response)
