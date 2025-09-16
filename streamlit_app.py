# streamlit_app.py
import streamlit as st
from query import load_retriever, build_qa_chain

st.title("RAG Codebase Assistant — Demo")

if "qa" not in st.session_state:
    retriever = load_retriever()
    st.session_state.qa = build_qa_chain(retriever)

q = st.text_input("Ask about the codebase:")
if st.button("Ask") and q:
    with st.spinner("Searching and generating..."):
        resp = st.session_state.qa.run(q)
    st.markdown("**Answer:**")
    st.write(resp)
