import streamlit as st 
from src.modelzone import NLPZone,AudioZone,MultiModalZone

#changed
class HuggingFace:
    def __init__(self) -> None:
        self.nlp_zone=NLPZone()
        self.audio_zone=AudioZone()
        self.multmodal_zone=MultiModalZone()
    
    def huggingface(self):
        
        with st.sidebar:
            category=st.selectbox("Select a category",[
            "NLP","Audio","MultiModal"
        ])
        if category=="NLP":
            self.nlp_zone.nlp()
        elif category=="Audio":
            self.audio_zone.audio()
        elif category=="MultiModal":
            self.multmodal_zone.multimodal()
            
            