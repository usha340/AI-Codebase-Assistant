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


