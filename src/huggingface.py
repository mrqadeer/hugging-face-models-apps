import streamlit as st 
from src.hf_intro import HuggingFace
class HuggingFace:
    def __init__(self) -> None:
        self.hf_intro=HuggingFace()
    
    def huggingface(self):
        
        with st.sidebar:
            category=st.selectbox("Select a category",[
            "NLP","Audio","MultiModal"
        ])
        if category=="NLP":
            self.introduction.nlp()
        elif category=="Audio":
            self.introduction.audio()
        elif category=="MultiModal":
            self.introduction.multimodal()
            
            