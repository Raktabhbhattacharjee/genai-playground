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

### Day 3 — Structured Output
- Understood structured output — forcing LLM to return typed, validated data instead of free-form text
- Used `with_structured_output(PydanticModel)` to extract structured data from messy natural language
- Defined schemas using Pydantic `BaseModel` — same pattern as FastAPI request/response schemas
- Built a **Person Info Extractor** using Streamlit — paste any text, get back name, age, skills
- Understood LLM as a parsing layer — replaces fragile regex/string splitting with intelligent extraction
- Key insight: same Pydantic contract used in backend, now LLM fills it instead of clean JSON from frontend

### Day 4 — Output Parsers
- Understood output parsers — transforming raw `AIMessage` into usable Python types (`str`, `dict`)
- Used `StrOutputParser` to strip `AIMessage` wrapper and get a clean string
- Used `JsonOutputParser` to get a proper Python `dict` directly from LLM response
- Understood the modern split: `with_structured_output` for structured/typed data, `StrOutputParser` for clean text
- Key insight: `PydanticOutputParser` (old way) manually injects format instructions into the prompt and parses the string — `with_structured_output` (modern way) delegates this to the model's native tool-calling API, far more reliable
- `StrOutputParser` remains relevant — used in every chain, RAG pipeline, and agent going forward

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
├── structured_output/
│   ├── structured.py         # Pydantic schema + structured LLM logic
│   └── app.py                # Streamlit UI
├── output_parsers/
│   ├── parsers.py            # StrOutputParser + JsonOutputParser
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

### Articles (Mangesh Salunke — Data and Beyond)

- [Output Parsers in LangChain](https://medium.com/data-and-beyond/output-parsers-in-langchain-b2e0db20880f)
- [Chains in LangChain — Part 1](https://medium.com/data-and-beyond/chains-in-langchain-part-1-040624795f91)
- [Chains in LangChain — Part 2](https://medium.com/data-and-beyond/chains-in-langchain-part-2-6c13dfadc45f)
- [Runnables in LangChain](https://medium.com/data-and-beyond/runnable-and-its-types-in-langchain-3b7a1ccfc922)
- [Document Loaders in LangChain](https://medium.com/data-and-beyond/document-loaders-in-langchain-f23d3ce70d66)
- [Text Splitters in LangChain](https://medium.com/data-and-beyond/text-splitters-in-langchain-for-data-processing-3a958eea2797)