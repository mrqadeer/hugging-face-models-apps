import streamlit as st 
from src.modelzone import NLPZone,AudioZone,MultiModalZone,ComputerVision
#changed
class HuggingFace:
    def __init__(self) -> None:
        self.nlp_zone=NLPZone()
        self.audio_zone=AudioZone()
        self.multmodal_zone=MultiModalZone()
        self.computer_zone=ComputerVision()
    def huggingface(self):
        
        with st.sidebar:
            category=st.selectbox("Select a category",[
            "NLP","Audio","MultiModal","Computer Vision"
        ])
        if category=="NLP":
            self.nlp_zone.nlp()
        elif category=="Audio":
            self.audio_zone.audio()
        elif category=="MultiModal":
            self.multmodal_zone.multimodal()
        else:
            self.computer_zone.computer_vision()
            
            