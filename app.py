from agents.memory_agent import MemoryAgent


def main():
    memory = MemoryAgent()

    print("\n🧠 Universal Memory Agent (Gemini)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        # 🔍 Retrieve context
        context = memory.retrieve(user_input)
        print("\n🧠 Retrieved Context:", context)

        # (simulate system response)
        response = f"Processed: {user_input}"

        # 💾 Store interaction
        memory.store(user_input, response)

        print("💾 Stored in memory\n")


if __name__ == "__main__":
    main()