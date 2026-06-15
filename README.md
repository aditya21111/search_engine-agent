# 🔍 Searchy — AI-Powered Search Assistant

An intelligent chatbot built with **LangChain**, **LangGraph**, and **Streamlit** that can search the web, Wikipedia, and academic research papers in real time. Powered by Groq's blazing-fast LLM inference.

## ✨ Features

- **Multi-Source Search** — Queries across four different search tools simultaneously:
  - 🌐 **DuckDuckGo** — General web search
  - 📖 **Wikipedia** — Encyclopedia lookups
  - 🔬 **Arxiv** — Academic & research paper search
  - 🔎 **Tavily** — AI-optimized web search
- **Conversational Memory** — Maintains chat history within a session using LangGraph checkpointing
- **Streaming Responses** — Real-time token streaming for a fluid chat experience
- **Agentic Architecture** — Uses a LangGraph agent that autonomously decides which tools to invoke based on the user's query

## 🛠️ Tech Stack

| Component       | Technology                          |
| --------------- | ----------------------------------- |
| **LLM**         | Qwen3-32B (via Groq)               |
| **Framework**   | LangChain + LangGraph               |
| **Frontend**    | Streamlit                           |
| **Search Tools**| DuckDuckGo, Wikipedia, Arxiv, Tavily|
| **Language**    | Python 3.13+                        |

## 📋 Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip
- API keys for:
  - [Groq](https://console.groq.com/) — LLM inference
  - [Tavily](https://tavily.com/) — AI search

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aditya21111/search_engine-agent
cd search-engine
```

### 2. Set up the environment

**Using uv (recommended):**

```bash
uv sync
```

**Using pip:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 4. Run the app

```bash
streamlit run main.py
```

The app will open in your browser .

## 📁 Project Structure

```
search-engine/
├── main.py              # Main Streamlit application & agent setup
├── requirements.txt     # Pinned dependencies
└── README.md            # This file
```

## 🧠 How It Works

1. **User sends a message** through the Streamlit chat interface
2. The **LangGraph agent** receives the message along with a system prompt defining its behavior
3. The agent **autonomously decides** which tools (DuckDuckGo, Wikipedia, Arxiv, Tavily) to use
4. Results are **streamed back** to the user in real time
5. **Conversation history** is preserved in-memory for context-aware follow-up questions

## ⚙️ Configuration

You can customize the agent's behavior by modifying the following in `main.py`:

- **LLM Model** — Change `model='qwen/qwen3-32b'` to any Groq-supported model
- **System Prompt** — Update the `system_prompt` parameter in `create_agent()`
- **Search Depth** — Adjust `top_k_results` and `doc_content_chars_max` for Wikipedia/Arxiv
- **Tavily Results** — Modify `max_results` in the `TavilySearch` configuration


