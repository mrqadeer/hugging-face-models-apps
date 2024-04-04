import streamlit as st

class ModelZone:
    def __init__(self):
        pass

    def nlp(self):
        st.title("Natural Language processing (NLP)")
        with st.sidebar:
            select=st.selectbox("Select the action you want to perform", 
                                ["Sentiment Analysis", "Name Entity Recognition", "Table Answer Question",
                                "Zero-Shot Classification", "Feature Extraction", "Text Summarization", "Translation",
                                "Text Generation", "Fill Mask", "Sentence Similarity",], placeholder="Select an action")
            if select == "Sentiment Analysis":
                st.subheader("Sentiment Analysis")
            elif select == "Name Entity Recognition":
                st.subheader("Name Entity Recognition")
            elif select == "Table Answer Question":
                st.subheader("Table Answer Question")
            elif select == "Zero-Shot Classification":
                st.subheader("Zero-Shot Classification")
            elif select == "Feature Extraction":
                st.subheader("Feature Extraction")
            elif select == "Text Summarization":
                st.subheader("Text Summarization")
            elif select == "Translation":
                st.subheader("Translation")
            elif select == "Text Generation":
                st.subheader("Text Generation")
            elif select == "Fill Mask":
                st.subheader("Fill Mask")
            elif select == "Sentence Similarity":
                st.subheader("Sentence Similarity")
            else:
                st.write("Select an action")

    def audio(self):
        st.title("Audio")
        with st.sidebar:
            select=st.selectbox("Select the action you want to perform", 
                                ["Text to Speech", "Text to Audio", "Automatic Speech Recognition",
                                 "Audio Classification"], placeholder="Select an action")

    def multimodal(self):
        st.title("Multimodal")
        with st.sidebar:
            select=st.selectbox("Select the action you want to perform", 
                                ["Document Question Answering", "Depth Estimation", "Image Classification",
                                 "Object Detection", "Text to Image", "Image to Text"], placeholder="Select an action")