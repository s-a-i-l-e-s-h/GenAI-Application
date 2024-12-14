from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title = "Demo Page")
st.header("LLM Application")

input =st.text_input("Input: ",key="input")
submit=st.button("Ask the Question")

if submit:
    response = get_gemini_response("Now you are in the Museum Guided System. Guide me in terms of Mueseum for the assistance in "+input)
    st.subheader("The Response is")
    st.write(response)

