
import streamlit as st
import requests

st.title("Gemini Q&A")

query = st.text_input("Ask a question:")

if st.button("Submit"):
    response = requests.post("http://localhost:8000/query", json={"query": query})
    st.write(response.json()["response"])
