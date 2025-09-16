from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

INDEX_DIR = "indices/ai_interviewer_faiss"   # adjust to where you saved index
EMB_MODEL = "all-MiniLM-L6-v2"

# 🔑 put your OpenAI API key here
OPENAI_API_KEY = "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"   # <-- replace with your real key

def load_retriever(index_dir=INDEX_DIR, emb_model=EMB_MODEL):
    embeddings = SentenceTransformerEmbeddings(model_name=emb_model)
    faiss_index = FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)
    retriever = faiss_index.as_retriever(search_kwargs={"k":5})
    return retriever

def build_qa_chain(retriever):
    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)  # pass key directly
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa

if __name__ == "__main__":
    retriever = load_retriever()
    qa = build_qa_chain(retriever)
    while True:
        q = input("\nEnter question (or 'exit'): ").strip()
        if q.lower() in ("exit", "quit"):
            break
        resp = qa.run(q)
        print("\n=== ANSWER ===\n")
        print(resp)
