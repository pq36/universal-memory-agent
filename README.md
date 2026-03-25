# Universal Memory Agent

A Gemini-powered memory system for storing and retrieving context across AI agent interactions.

---

## Overview

Universal Memory Agent is a centralized memory module designed for multi-agent AI systems. It enables persistent storage and intelligent retrieval of past interactions such as messages, tasks, events, and other activities.

The system uses a Large Language Model (Gemini) to retrieve relevant context, allowing agents to make context-aware decisions.

---

## Features

- Persistent memory using MongoDB
- Context-aware retrieval using Gemini
- Supports multiple activity types (messages, tasks, events)
- Modular and reusable design
- Enables long-term memory for AI agents

---

## Architecture

```

User Input
↓
Memory Retrieval (Gemini)
↓
Context
↓
Agent Decision / Execution
↓
Memory Storage (MongoDB)

```

---

## Project Structure

```

memory-agent/
│
├── agents/
│   └── memory_agent.py
│
├── llm/
│   └── gemini_client.py
│
├── app.py
├── requirements.txt
└── .env

````

---

## Tech Stack

- Python
- Gemini (Google Generative AI)
- LangChain
- MongoDB
- dotenv

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/universal-memory-agent.git
cd universal-memory-agent
````

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
MONGO_URI=mongodb://localhost:27017/
```

---

### 4. Run the application

```bash
python app.py
```

---

## Example

Input:

```
Schedule meeting with client tomorrow
```

System:

* Retrieves relevant past context
* Stores new interaction

---

## Use Case

This memory agent can be integrated into:

* Task management agents
* Calendar scheduling systems
* Email automation agents
* Multi-agent AI workflows

---

## Author

Meghana
