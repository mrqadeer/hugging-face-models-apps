# Import necessary libraries
import streamlit as st 

# Import model zones
from src.modelzone import NLPZone,AudioZone,MultiModalZone,ComputerVisionZone

# Define the class 
class HuggingFace:
    def __init__(self) -> None:
        """
        Initializes the HuggingFace object by creating instances of NLPZone, AudioZone, MultiModalZone, and ComputerVisionZone.
        """
        # Initialize each model zone object
        self.nlp_zone=NLPZone()
        self.audio_zone=AudioZone()
        self.multmodal_zone=MultiModalZone()
        self.computer_zone=ComputerVisionZone()
    
    # Defining the function 
    def huggingface(self):
        """
        This function determines the category selected by the user and calls the corresponding method based on the category.
        """
        # Creating a sidebar for selecting the category
        with st.sidebar:
            # Add a select box to the sidebar for user to select the category
            category=st.selectbox("Select a category",sorted([
            "NLP","Audio","MultiModal","Computer Vision"
        ]))
        
        # Call methods from respective model zones based on the category selected
        if category=="NLP":
            self.nlp_zone.nlp()
        elif category=="Audio":
            self.audio_zone.audio()
        elif category=="MultiModal":
            self.multmodal_zone.multimodal()
        else:
            self.computer_zone.computer_vision()
            
            