import ollama

print("\n================================")
print("       MY PERSONAL AI")
print("================================")
print("Powered by Llama 3.2")
print("Type 'exit' to close the chatbot.")

messages = []

while True:

    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "exit":
        print("\nAI: Goodbye! Have a great day!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        print("\nAI is thinking...")

        response = ollama.chat(
            model="llama3.2",
            messages=messages
        )

        answer = response.message.content

        print("\nLlama:", answer)

        messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        print("\nError:", e)
        messages.pop()