import streamlit as st

class Home:
    def __init__(self):
        pass
    def home():
        st.title("HuggingFace Models")
        token=st.text_input("Hugging Face Token",type='password')
        st.session_state=token