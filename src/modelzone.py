import streamlit as st 

from src.nlp.sentiment_analysis import SentimentAnalysis
from src.nlp.token_classification import TokenClassification
from src.nlp.zero_shot_classification import ZeroShotClassification
from src.nlp.table_qa import TableQuestionAnswer
from src.nlp.text_summarization import TextSummarization
from src.nlp.text_translation import TextTranslation
from src.audio.text_speech import text_to_speech
from src.nlp.feature_extraction import FeatureExtraction
from src.nlp.text_generation import TextGeneration
from src.nlp.fill_mask import FillMask
from src.nlp.sentence_similarity import SentenceSimilarity
from src.audio.text_to_audio import text_to_audio
from src.audio.speech_recognition import speech_recognition
from src.audio.audio_classification import audio_classifier
from src.multimodal.document_qa import document_question_answering
from src.multimodal.depth_estimation import depth_estimator
from src.multimodal.image_classification import image_classifier
from src.multimodal.object_detection import object_detector
from src.multimodal.text_to_image import text_to_image
from src.multimodal.image_to_text import image_to_text




class NLPZone:
    def __init__(self) -> None:
        self.sentiment_analysis=SentimentAnalysis()
        self.token_classification=TokenClassification()
        self.table_question_answer=TableQuestionAnswer()
        self.zero_short_classification=ZeroShotClassification()
        self.feature_extraction=FeatureExtraction()
        self.text_summarization=TextSummarization()
        self.text_translation=TextTranslation()
        self.text_generation=TextGeneration()
        self.fill_mask=FillMask()
        self.sentence_similarity=SentenceSimilarity()
    def nlp(self):
        st.title("Naural Language Processing (NLP)")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                ["Sentiment Analysis", "Name Entity Recognition", "Table Answer Question",
                                   "Zero-Shot Classification", "Feature Extraction", "Text Summarization",
                                   "Translation", "Text Generation", "Fill Mask", "Sentence Similarity"],
                                placeholder="Select a subcategory")
            
        if select=="Sentiment Analysis":
            self.sentiment_analysis.sentiment_analysis()
            
            
        if select=="Name Entity Recognition":
            self.token_classification.token_classification()
            
        if select=="Table Answer Question":
            self.table_question_answer.table_question_answering()
            
        if select=="Zero-Shot Classification":
            self.zero_short_classification.zero_shot_classification()
                
        if select=="Feature Extraction":
            self.feature_extraction.feature_extraction()
                
        if select=="Text Summarization":
            self.text_summarization.text_summarization()
        if select=="Translation":
            self.text_translation.text_translation()
        if select=="Text Generation":
            self.text_generation.text_generation()
                
        if select=="Fill Mask":
            self.fill_mask.fill_masK()
   
        if select=="Sentence Similarity":
            self.sentence_similarity.sentence_similarity()
           

class AudioZone:
    def __init__(self) -> None:
        pass
    def audio(self):
        st.title("Audio")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                ["Text to Speech", "Text to Audio", "Automatic Speech Recognition",
                                 "Audio Classification"],
                                placeholder="Select a subcategory")
        if select=="Text to Speech":
            st.subheader("Text to Speech")
            st.divider()
            text = st.text_area("Enter your Text", placeholder="The universe is vast and mysterious and holds countless wonders waiting to be discovered")
            speak_button_clicked = st.button("Identify")
            if speak_button_clicked:
                text_to_speech(text)
            else:
                st.write("Click the button to convert your text into speech")
                
        if select=="Text to Audio":
            st.subheader("Text to Audio")
            st.divider()
            text = st.text_area("Enter your Text", placeholder="liquid drum and bass, atmospheric synths, airy sounds")
            audio_button_clicked = st.button("Create Audio")
            if audio_button_clicked:
                text_to_audio(text)
        
        if select=="Automatic Speech Recognition":
            st.subheader("Automatic Speech Recognition")
            st.divider()
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            recognize_button_clicked = st.button("Recognize")
            if recognize_button_clicked:
                speech_recognition(filename)
            
        if select=="Audio Classification":
            st.subheader("Audio Classification")
            st.divider()
            audio = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            classify_button_clicked = st.button("Classify")
            if classify_button_clicked:
                audio_classifier(audio)
            
class MultiModalZone:
    def __init__(self) -> None:
        pass
    def multimodal(self):
        st.title("Multimodal")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                ["Document Q/A", "Depth Estimation", "Image Classification",
                                  "Object Detection", "Text to Image", "Image to Text"],
                                placeholder="Select a subcategory")
    
        if select=="Document Q/A":
            st.subheader("Document Question Answering")
            st.divider()
            text = st.text_area("Enter your querry", placeholder="")
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            process_button_clicked = st.button("Process")
            if process_button_clicked:
                document_question_answering(text, image)
            
        if select=="Depth Estimation":
            st.subheader("Depth Estimation")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            estimate_button_clicked = st.button("Estimate")
            if estimate_button_clicked:
                depth_estimator(image)
            
        if select =="Image Classification":
            st.subheader("Image Classification")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            classify_button_clicked = st.button("Classify")
            if classify_button_clicked:
                image_classifier(image)
        
        if select =="Object Detection":
            st.subheader("Object Detection")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            detect_button_clicked = st.button("Detect")
            if detect_button_clicked:
                object_detector(image)
            
        if select =="Text to Image":
            st.subheader("Text to Image")
            st.divider()
            text = st.text_area("Enter your querry", placeholder="Astronaut riding a horse")
            create_button_clicked = st.button("Create Image")
            if create_button_clicked:
                text_to_image(text)
            
        if select =="Image to Text":
            st.subheader("Image to Text")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            describe_button_clicked = st.button("Describe")
            if describe_button_clicked:
                image_to_text(image)