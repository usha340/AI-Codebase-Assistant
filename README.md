# AI-Codebase-Assistant

# 📘 Ai Codebase Assistant

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
├── ingest.py # Clone repo + build FAISS index
├── query.py # Load index + run queries via OpenAI LLM
├── streamlit_app.py # Streamlit interface for Q&A
├── indices/ # Saved FAISS index (generated after ingestion)
├── data/ # Cloned repositories

yaml
Copy code

---

## ⚙️ Installation
### 1️⃣ Clone this repo
```bash
git clone https://github.com/your-username/rag-codebase-assistant.git
cd rag-codebase-assistant
2️⃣ Create virtual environment & install dependencies
bash
Copy code
python -m venv .venv
source .venv/bin/activate   # on Linux/Mac
.venv\Scripts\activate      # on Windows

pip install -r requirements.txt
📑 Usage
🔹 Step 1: Ingest a GitHub repository
This clones a repo, splits files, and builds the FAISS index.

bash
Copy code
python ingest.py --git_url https://github.com/openai/openai-cookbook
Optional arguments:

--out_repo_dir → where to clone repo (default: data/repos/repo)

--index_dir → where to save FAISS index (default: indices/faiss_index)

🔹 Step 2: Query from the terminal
bash
Copy code
python query.py
You’ll be prompted to enter questions interactively.

🔹 Step 3: Run Streamlit UI
bash
Copy code
streamlit run streamlit_app.py
Open http://localhost:8501 to use the assistant in your browser.

🔑 API Key Setup
In query.py, replace the placeholder with your OpenAI API key:

python
Copy code
OPENAI_API_KEY = "your-openai-api-key-here"
Or, set it as an environment variable:

bash
Copy code
export OPENAI_API_KEY="your-openai-api-key-here"   # Linux/Mac
setx OPENAI_API_KEY "your-openai-api-key-here"     # Windows
Then modify query.py to fetch from environment:

python
Copy code
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
