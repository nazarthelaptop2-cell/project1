import streamlit as st
from google import genai


client = genai.Client(api_key=GENAI_API_KEY)
st.title("Chemicals AI")
argumentfield = st.text_input("Введите запрос:")
if st.button("Сгенерировать"):
    if argumentfield:
        answer = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=argumentfield
        )
        st.write(answer.text)
    elif argumentfield:
        st.success("вы отправили запрос")
    else:
        st.error("вы не написали запрос!")