
import streamlit as st 

from src.nlp.sentiment_analysis import SentimentAnalysis
from src.nlp.token_classification import TokenClassification
from src.nlp.zero_shot_classification import ZeroShotClassification
from src.nlp.table_qa import TableQuestionAnswer
from src.nlp.text_summarization import TextSummarization
from src.nlp.text_translation import TextTranslation
from src.nlp.feature_extraction import FeatureExtraction
from src.nlp.text_generation import TextGeneration
from src.nlp.fill_mask import FillMask
from src.nlp.sentence_similarity import SentenceSimilarity

from src.audio.text_to_audio import TextAudio
from src.audio.speech_recognition import SpeechRecognition
from src.audio.audio_classification import AudioClassifier
from src.audio.text_speech import TextSpeech
from src.audio.text_speech import TextSpeech
from src.audio.audio_to_audio import AudioToAudio
from src.multimodal.document_qa import DocumentQuaestionAnswering

from src.computer_vision.image_classification import ImageClassifier
from src.computer_vision.object_detection import ObjectDetector
from src.computer_vision.text_to_image import TextToImageGenerator
from src.computer_vision.image_to_text import ImageToTextGenerator


class NLPZone:
    def __init__(self) -> None:
        """
        Initializes various NLP models for sentiment analysis, token classification, table question answering, zero-shot classification, feature extraction, text summarization, text translation, text generation, fill mask, and sentence similarity.
        """
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
        """
        This function handles Natural Language Processing (NLP) tasks by allowing the user to select from a variety of options such as Sentiment Analysis, Name Entity Recognition, Table Answer Question, Zero-Shot Classification, Text Summarization, Translation, Text Generation, Fill Mask, and Sentence Similarity. It displays a Streamlit UI with a sidebar for selecting the desired NLP task and calls the corresponding function based on the user's selection.
        """
        # Function dictionary mapping select options to functions
        options_functions_nlp = {
            "Sentiment Analysis": self.sentiment_analysis.sentiment_analysis,
            "Name Entity Recognition": self.token_classification.token_classification,
            "Table Answer Question": self.table_question_answer.table_question_answering,
            "Zero-Shot Classification": self.zero_short_classification.zero_shot_classification,
            # "Feature Extraction": self.feature_extraction.feature_extraction,
            "Text Summarization": self.text_summarization.text_summarization,
            "Translation": self.text_translation.text_translation,
            "Text Generation": self.text_generation.text_generation,
            "Fill Mask": self.fill_mask.fill_mask,
            "Sentence Similarity": self.sentence_similarity.sentence_similarity
        }
        # Streamlit UI
        st.title("Naural Language Processing (NLP)")
        with st.sidebar:
            select = st.selectbox("What do you want to perform",
                                sorted(options_functions_nlp.keys()),
                                placeholder="Select a subcategory")
        # Call the selected function
        if select in options_functions_nlp:
            options_functions_nlp[select]()
              

class AudioZone:
    def __init__(self) -> None:
        """
        Constructor method to initialize AudioZone class with instances of various audio processing components.
        """
        self.audio_classification=AudioClassifier()
        self.speech_recognition=SpeechRecognition()
        self.text_speech=TextSpeech()
        self.text_to_audio=TextAudio()
        self.audio_to_audio=AudioToAudio()
    def audio(self):
        """
        This function handles audio processing by providing a Streamlit UI for selecting different audio processing tasks such as Text to Speech, Text to Audio, Automatic Speech Recognition, Audio Classification, and Denoise Audio. It allows the user to choose a subcategory from the options displayed and then calls the corresponding function based on the selection.
        """
        options_functions_audio = {
            "Text to Speech": self.text_speech.text_to_speech,
            "Text to Audio":self.text_to_audio.text_to_audio,
            "Automatic Speech Recognition":self.speech_recognition.speech_recognition,
            "Audio Classification":self.audio_classification.audio_classifier,
            "Denoise Audio":self.audio_to_audio.audio_to_audio
        }
        # Streamlit UI
        st.title("Audio Processing Models")
        with st.sidebar:
            select = st.selectbox("What do you want to perform",
                                sorted(options_functions_audio.keys()),
                                placeholder="Select a subcategory")
        # Call the selected function
        if select in options_functions_audio:
            options_functions_audio[select]()
                  
                
class MultiModalZone:
    def __init__(self) -> None:
        """
        Initializes the object of the class. 
        No parameters are taken, and the function returns None.
        """
        self.document_qa=DocumentQuaestionAnswering()
        
    def multimodal(self):
        """
        This function handles the multimodal functionality by presenting a Streamlit UI for selecting different multimodal tasks, such as Document Question/Answering. It allows the user to choose a subcategory from the options displayed and then calls the corresponding function based on the selection.
        """
        options_functions_mm = {
            "Document Q/A":self.document_qa.document_question_answering
        }
        # Streamlit UI
        st.title("Multimodal")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                sorted(options_functions_mm.keys()),
                                placeholder="Select a subcategory")
        # Call the selected function
        if select in options_functions_mm:
            options_functions_mm[select]()   
                    
class ComputerVisionZone:
    def __init__(self) -> None:
        """
        Initializes the ComputerVisionZone class with instances of various components for image classification, object detection, text to image generation, and image to text generation.
        """
        self.image_classification=ImageClassifier()
        self.object_detection=ObjectDetector()
        self.text_to_image=TextToImageGenerator()
        self.image_to_text=ImageToTextGenerator()
        
        
    def computer_vision(self): 
        """
        This function handles the computer vision functionality by presenting a Streamlit UI for selecting different computer vision tasks, such as Image Classification, Object Detection, Text to Image, and Image to Text. It allows the user to choose a subcategory from the options displayed and then calls the corresponding function based on the selection.
        """
        options_functions_cv = {
            "Image Classification":self.image_classification.image_classifier,
            "Object Detection":self.object_detection.object_detector,
            "Text to Image":self.text_to_image.text_to_image, 
            "Image to Text":self.image_to_text.image_to_text
        }
        
        # Streamlit UI
        st.title("Computer Vision")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                sorted(options_functions_cv.keys()),
                                placeholder="Select a subcategory")
        # Call the selected function
        if select in options_functions_cv:
            options_functions_cv[select]()

            