# LangChain Learning Journey

A personal repo documenting my hands-on learning of LangChain and Gen AI engineering — built alongside the CampusX playlist and official LangChain docs.

---

## Stack

- **Python** 3.13
- **LangChain** 1.2.17+
- **Package Manager** uv

---

## Models

### LLMs (Chat Models)
| Model | Provider | Tier |
|---|---|---|
| `gemini-2.5-flash-lite` | Google Gemini | Free |
| `llama-3.3-70b-versatile` | Groq | Free |

### Embedding Models
| Model | Provider | Tier |
|---|---|---|
| `gemini-embedding-001` | Google Gemini | Free API |
| `BAAI/bge-small-en-v1.5` | HuggingFace | Local |

> **Note:** Using Chat Models only — not the legacy LLM interface.

---

## Progress

### Day 1 — Chat Models
- Understood the difference between LLMs (legacy) and Chat Models (current standard)
- Set up LangChain with `uv`, configured `.env` for API keys
- Initialized and invoked models using `ChatGoogleGenerativeAI` and `ChatGroq`
- Understood `AIMessage` response structure (`content`, `usage_metadata`, etc.)
- Set up local HuggingFace embeddings (`bge-small-en-v1.5`) — no API key needed
- Providers explored: Google Gemini, Groq, HuggingFace

### Day 2 — Prompt Templates
- Understood `ChatPromptTemplate` — dynamic prompts with variable injection
- Learned to keep prompt logic separate from application logic (prompt.py vs app.py)
- Built a **Gen AI Roadmap Generator** using Streamlit — users provide 4 inputs, system prompt stays hidden
- Understood the separation of concerns: prompt template = data model, app = route
- Built first end-to-end LangChain chain: `prompt | llm`

---

## Project Structure

```
lang/
├── models/
│   ├── gemini_chat.py        # Gemini chat model
│   ├── gemini_embeddings.py  # Gemini embeddings
│   ├── huggingface.py        # HuggingFace local embeddings
│   └── groq_chat.py          # Groq/Llama chat model
├── prompts/
│   ├── prompt.py             # Prompt template logic
│   └── app.py                # Streamlit UI
├── .env
├── pyproject.toml
└── README.md
```

---

## Setup

```bash
git clone https://github.com/Raktabhbhattacharjee/genai-playground
cd lang
uv sync
```

Add a `.env` file:
```
GOOGLE_API_KEY=your_key
GROQ_API_KEY=your_key
```

---

## Resources
- [LangChain Docs](https://docs.langchain.com)
- [CampusX YouTube](https://www.youtube.com/@campusx-official)