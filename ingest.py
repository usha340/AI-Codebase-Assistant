# ingest.py
import os
import argparse
from git import Repo
from pathlib import Path
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS

# Supported file extensions to index (customize)
DEFAULT_EXTS = {'.py', '.js', '.ts', '.java', '.go', '.md', '.txt', '.yaml', '.yml', '.json', '.cpp', '.c', '.h', '.html'}

def clone_repo(git_url: str, dest: str):
    dest_path = Path(dest)
    if dest_path.exists():
        print(f"[clone] Destination exists — pulling latest in {dest}")
        try:
            Repo(dest).remote().pull()
        except Exception as e:
            print("Pull failed, skipping pull:", e)
    else:
        print(f"[clone] Cloning {git_url} -> {dest}")
        Repo.clone_from(git_url, dest, depth=1)

def collect_files(root: str, exts=DEFAULT_EXTS):
    root = Path(root)
    files = []
    for p in root.rglob('*'):
        if p.is_file() and p.suffix.lower() in exts:
            files.append(p)
    print(f"[collect] Found {len(files)} files to index")
    return files

def file_to_documents(path: Path, chunk_size=1000, chunk_overlap=200):
    text = path.read_text(encoding='utf-8', errors='ignore')
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_text(text)
    docs = []
    for i, c in enumerate(chunks):
        meta = {
            "path": str(path),
            "name": path.name,
            "chunk_index": i,
        }
        docs.append(Document(page_content=c, metadata=meta))
    return docs

def build_index(docs, index_dir: str, model_name="all-MiniLM-L6-v2"):
    print("[index] creating embeddings model:", model_name)
    embeddings = SentenceTransformerEmbeddings(model_name=model_name)
    print("[index] building FAISS index (this may take a bit)...")
    faiss_index = FAISS.from_documents(docs, embeddings)
    os.makedirs(index_dir, exist_ok=True)
    faiss_index.save_local(index_dir)
    print(f"[index] saved index to {index_dir}")

def main(git_url, out_repo_dir="data/repos/repo", index_dir="indices/faiss_index"):
    clone_repo(git_url, out_repo_dir)
    files = collect_files(out_repo_dir)
    all_docs = []
    for f in files:
        docs = file_to_documents(f)
        # attach relative path for nicer metadata
        for d in docs:
            d.metadata["relpath"] = os.path.relpath(d.metadata["path"], out_repo_dir)
        all_docs.extend(docs)
    print(f"[ingest] Total chunks: {len(all_docs)}")
    if len(all_docs) == 0:
        print("No documents to index. Exiting.")
        return
    build_index(all_docs, index_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--git_url", required=True, help="GitHub repo url to clone")
    parser.add_argument("--out_repo_dir", default="data/repos/repo", help="where to clone repo")
    parser.add_argument("--index_dir", default="indices/faiss_index", help="where to save FAISS index")
    args = parser.parse_args()
    main(args.git_url, args.out_repo_dir, args.index_dir)
