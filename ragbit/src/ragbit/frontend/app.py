import streamlit as st
import requests
import os

st.markdown("# RAGbit")
st.markdown("RAGbit is good at answering questions about dwarf rabbits")

user_prompt = st.text_input("Ask a question")

backend_url = os.environ.get("API_URL", "http://127.0.0.1:8000")

if st.button("SEND") and user_prompt.strip() != "":
    response = requests.post(f"{backend_url}/rag/query", json={"prompt": user_prompt})
    data = response.json()
    st.write(data)