import streamlit as st
import requests
from pathlib import Path
# import os
from dotenv import load_dotenv

load_dotenv()

ASSETS_PATH = Path(__file__).absolute().parents[1] / "assets"

# url = f"https://ragbit.azurewebsites.net/rag/query?code={os.getenv('FUNCTION_APP_API')}"
url = "http://127.0.0.1:8000/rag/query"

def layout():
    st.markdown("# Ragbit")
    st.markdown("Ask a question about different dwarf rabbits")
    text_input = st.text_input(label="Ask a question")

    if st.button("Send") and text_input != "":
        response = requests.post(url, json={"prompt": text_input})

        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])

        st.image(ASSETS_PATH / f"{data['filename']}.png")


if __name__ == "__main__":
    layout()
