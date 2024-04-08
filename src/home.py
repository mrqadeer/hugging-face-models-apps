import streamlit as st

class Home:
    def __init__(self):
        pass
    def home():
        if 'access_token' not in st.session_state:
            st.session_state.access_token=None
            
        st.title("HuggingFace Models")

        token=st.text_input("Hugging Face Token",type='password')
        if len(token)>0:
            st.info("Thanks for providing Access Token")
            st.session_state.access_token=token

        st.subheader('A gold mine of models and tools.')
        st.image("https://huggingface.co/front/assets/huggingface_logo.svg")
        st.write("Hugging Face is a company that provides a large collection of pre-trained models and tools for Natural Language Processing (NLP).")

