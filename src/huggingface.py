import streamlit as st 

from src.modelzone import ModelZone
#changed

class HuggingFace:
    def __init__(self) -> None:
        self.introduction=HuggingFace()
    
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
            
            