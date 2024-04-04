import streamlit as st 
from src.modelzone import ModelZone
class HuggingFace:
    def __init__(self) -> None:
        self.modelzone=ModelZone()
    
    def huggingface(self):
        
        with st.sidebar:
            category=st.selectbox("Select a category",[
            "NLP","Audio","MultiModal"
        ])
        if category=="NLP":
            self.modelzone.nlp()
        elif category=="Audio":
            self.modelzone.audio()
        elif category=="MultiModal":
            self.modelzone.multimodal()
            
            