import os
from pymongo import MongoClient
from utils.gemini_client import get_gemini_model


class MemoryAgent:

    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client["universal_memory"]
        self.collection = self.db["interactions"]

        self.llm = get_gemini_model()

    # 💾 Store ANY type of activity
    def store(self, user_input, response=None, metadata=None):
        self.collection.insert_one({
            "user_input": user_input,
            "response": str(response),
            "metadata": metadata or {}
        })

    # 🧠 Retrieve relevant context (Gemini-powered)
    def retrieve(self, user_input):
        memories = list(self.collection.find().limit(30))

        if not memories:
            return ""

        memory_text = "\n".join([
            f"User: {m['user_input']} | Response: {m.get('response')}"
            for m in memories
        ])

        prompt = f"""
You are an intelligent memory retrieval system.

Current input:
{user_input}

Past interactions:
{memory_text}

Return only the most relevant context that helps understand the current input.
If nothing is useful, return "None".
"""

        response = self.llm.invoke(prompt)
        return response.content.strip()

    # 🧹 Optional: clear memory
    def clear(self):
        self.collection.delete_many({})