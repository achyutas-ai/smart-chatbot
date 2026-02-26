import os
from dotenv import load_dotenv

from chatbot.prompt import get_prompt
from chatbot.llm import get_llm
from chatbot.memory import ChatMemory


def setup():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("❌ OPENAI_API_KEY not found in .env")

    prompt = get_prompt()
    llm = get_llm()
    memory = ChatMemory(max_messages=6)

    return prompt, llm, memory


def build_messages(memory, user_input):
    messages = [
        ("system", "You are a helpful AI assistant. Keep answers short and clear.")
    ]

    # Add history
    messages.extend(memory.get_messages())

    # Add current input
    messages.append(("user", user_input))

    return messages

def chat():
    prompt, llm, memory = setup()

    print("🤖 Smart Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Save user input
        memory.add_user_message(user_input)

        # Build messages
        messages = build_messages(memory, user_input)

        # Call LLM
        response = llm.invoke(messages)

        print("Bot:", response.content)

        # Save response
        memory.add_ai_message(response.content)

if __name__ == "__main__":
    chat()