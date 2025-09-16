# 📘 RAG Codebase Assistant

A Retrieval-Augmented Generation (RAG) assistant for exploring and querying large codebases.  
It clones a repository, indexes its code into embeddings, and allows interactive Q&A via command line or a Streamlit UI.

---

## 🚀 Features
- Clone and index any GitHub repository.
- Split source files into semantic chunks.
- Create FAISS vector index with `SentenceTransformer` embeddings.
- Query the indexed codebase using OpenAI’s GPT models.
- Simple **Streamlit UI** for interactive exploration.

---

## 📂 Project Structure

- **ingest.py** → Clone repo + build FAISS index  
- **query.py** → Load index + run queries via OpenAI LLM  
- **streamlit_app.py** → Streamlit interface for Q&A  
- **indices/** → Saved FAISS index (generated after ingestion)  
- **data/** → Cloned repositories  
- **requirements.txt** → Python dependencies  

---

## ⚙️ Installation

### 1️⃣ Clone this repo
```bash
git clone https://github.com/your-username/rag-codebase-assistant.git
cd rag-codebase-assistant

### 2️⃣ Create virtual environment & install dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # on Linux/Mac
.venv\Scripts\activate      # on Windows

pip install -r requirements.txt


Step 2: Query from the terminal

python query.py


You’ll be prompted to enter questions interactively.

🔹 Step 3: Run Streamlit UI

streamlit run streamlit_app.py


Then open http://localhost:8501 in your browser.

🔑 API Key Setup

In query.py, replace the placeholder with your OpenAI API key:

OPENAI_API_KEY = "your-openai-api-key-here"


Or, set it as an environment variable:

Linux/Mac:

export OPENAI_API_KEY="your-openai-api-key-here"


Windows:

setx OPENAI_API_KEY "your-openai-api-key-here"


Then update query.py to fetch from environment:

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


📌 Requirements

Dependencies are listed in requirements.txt:

langchain

faiss-cpu

sentence-transformers

openai

streamlit

gitpython

Install them with:

pip install -r requirements.txt


🎯 Example Query

Enter question (or 'exit'): Where are API routes defined?
=== ANSWER ===
The API routes are defined in `src/routes/api.js` under the Express router.


