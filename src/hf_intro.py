import streamlit as st
from src.modelzone import ModelZone

class HuggingFace:
    def __init__(self):
        self.modelzone = ModelZone()
    
    def huggingface(self):
        with st.sidebar:
            category=st.selectbox("Select a category", ["NLP", "Audio", "Multimodal"])
            
        if category == "NLP":
            self.modelzone.nlp()
        elif category == "Audio":
            self.modelzone.audio()
        elif category == "Multimodal":
            self.modelzone.multimodal()