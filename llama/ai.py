import ollama
model_name = "llama3.2:latest "
prompt = "who is the president of the United States?"
response = ollama.generate(model=model_name, prompt=propmt)
print(response)