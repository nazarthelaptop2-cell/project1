import streamlit as st
from google import genai
from google.genai.types import ApiKeyConfig
GEMINI_API_KEY= st.secrets["GEMINI_API_KEY"]
st.write("Chemicals AI")
client = genai.Client(gemini_key=GEMINI_API_KEY)
argumentfield = st.text_input("введите запрос")
if st.button("generate"):

    answer = client.models.generate_content(model = "gemini-3.6-flash", contents= argumentfield)
    st.write(answer.text)
