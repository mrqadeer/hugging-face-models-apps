import streamlit as st 
from src.modelzone import NLPZone,AudioZone,MultiModalZone,ComputerVisionZone
#changed
class HuggingFace:
    def __init__(self) -> None:
        """
        Initializes the HuggingFace object by creating instances of NLPZone, AudioZone, MultiModalZone, and ComputerVisionZone.
        """
        self.nlp_zone=NLPZone()
        self.audio_zone=AudioZone()
        self.multmodal_zone=MultiModalZone()
        self.computer_zone=ComputerVisionZone()
    def huggingface(self):
        """
        This function determines the category selected by the user and calls the corresponding method based on the category.
        """
        
        with st.sidebar:
            category=st.selectbox("Select a category",sorted([
            "NLP","Audio","MultiModal","Computer Vision"
        ]))
        if category=="NLP":
            self.nlp_zone.nlp()
        elif category=="Audio":
            self.audio_zone.audio()
        elif category=="MultiModal":
            self.multmodal_zone.multimodal()
        else:
            self.computer_zone.computer_vision()
            
            