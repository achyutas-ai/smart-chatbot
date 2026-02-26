import os
from dotenv import load_dotenv

from chatbot.prompt import get_prompt
from chatbot.llm import get_llm
from chatbot.memory import get_memory
from chatbot.chain import build_chain

# Load environment variables
load_dotenv()

def main():
    print("🤖 Smart Chatbot (type 'exit' to quit)\n")

    prompt = get_prompt()
    llm = get_llm()
    memory = get_memory()

    chain = build_chain(prompt, llm, memory)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = chain.invoke(user_input)

        print("Bot:", response.content)

        # Save to memory
        memory.save_context(
            {"input": user_input},
            {"output": response.content}
        )

if __name__ == "__main__":
    main()