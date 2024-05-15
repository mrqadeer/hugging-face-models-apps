import shutil
import pathlib
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
from src.computer_vision.depth_estimation import depth_estimator
from src.computer_vision.image_classification import image_classifier
from src.computer_vision.object_detection import object_detector
from src.computer_vision.text_to_image import text_to_image
from src.computer_vision.image_to_text import image_to_text


current_path=pathlib.Path(__file__)
root_path=current_path.parent.parent


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
        # st.title("Naural Language Processing (NLP)")
        # Define a dictionary mapping select options to functions
        options_functions = {
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
                                sorted(options_functions.keys()),
                                placeholder="Select a subcategory")

        # Call the selected function
        if select in options_functions:
            options_functions[select]()
        





        
       
           

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
            with st.expander("Model Description"):
                st.markdown("""This model is a TTS model (facebook/mms-tts-eng) that is used to convert text into speech. 
                            Provide a text to convert into speech. You can also download the output audio.""")
            st.divider()
            text = st.text_area("Enter your Text", placeholder="The universe is vast and mysterious and holds countless wonders waiting to be discovered")
            speak_button_clicked = st.button("Get Speech")
            if speak_button_clicked:
                audio_output=text_to_speech(text)
                st.audio(audio_output)
                st.download_button(label="Download Audio", data=audio_output, file_name="audio_output.mp3", mime="audio/flac")
            else:
                st.write("Click the button to convert your text into speech")
                
        if select=="Text to Audio":
            st.subheader("Text to Audio")
            with st.expander("Model Description"):
                st.markdown("""This model is a TTS model (facebook/musicgen-small) that is used to convert text into audio. 
                            Provide a text to convert into instrumental audio file. You can also download the output audio file.""")
            st.divider()
            text = st.text_area("Enter your Text", placeholder="liquid drum and bass, atmospheric synths, airy sounds")
            audio_button_clicked = st.button("Get Audio")
            if audio_button_clicked:
                text_to_audio_output=text_to_audio(text)
                st.audio(text_to_audio_output)
                st.download_button(label="Download Audio", data=text_to_audio_output, file_name="audio_output.mp3", mime="audio/flac")
                
        
        if select=="Automatic Speech Recognition":
            st.subheader("Automatic Speech Recognition")
            with st.expander("Model Description"):
                st.markdown("""This model is a Speech Recognition model (facebook/wav2vec2-large-960h-lv60-self) that is used to recognize the text from an audio file.
                            The model predicts transcriptions in the same language as the audio. Provide an audio file to recognize the text.""")
            st.divider()
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            if filename is not None:
                file_folder = root_path / 'data'
                pathlib.Path.mkdir(file_folder,exist_ok=True)
                # Save the uploaded file to the data folder
                file_path = file_folder / filename.name
                with open(file_path, 'wb') as f:
                    f.write(filename.read())
                
                
                recognize_button = st.button("Recognize")
                if recognize_button:
                    # Call your speech recognition function using the file path
                    speech_recognition_output = speech_recognition(file_path)
                    st.text_area("Recognized Text", value=speech_recognition_output)
                    
                    
                
        if select=="Audio Classification":
            st.subheader("Audio Classification")
            with st.expander("Model Description"):
                st.markdown("""This model is an Audio Classification model (MIT/ast-finetuned-audioset-10-10) that is used to classify the audio into different categories.
                            Provide an audio file to classify the audio. The model predicts the labels and their scores.""")
            st.divider()
            
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            if filename is not None:
                
                file_folder = root_path / 'data'
                pathlib.Path.mkdir(file_folder,exist_ok=True)
                # Save the uploaded file to the data folder
                file_path = file_folder / filename.name
                with open(file_path, 'wb') as f:
                    f.write(filename.read())
            classify_button_clicked = st.button("Classify")
            if classify_button_clicked:
                audio_classifier_output=audio_classifier(file_path)
                if audio_classifier_output is not None:
                    for item in audio_classifier_output:
                        st.write(f"{item['label']} : {item['score']:.2%}")
                
            
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
            with st.expander("Model Description"):
                st.markdown("""This model is a Document Question Answering model (impira/layoutlm-document-qa) that is used to 
                            extract the answer from the tabular data in the provided document. The model accepts an image to extract the text and then answer the question.""")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            st.divider()
            url=st.text_input("Enter Image URL")
            if image is not None or url is not None:
                text = st.text_area("Enter your querry", placeholder="")
                process_button_clicked = st.button("Process")
                if process_button_clicked:
                    
                    qa_output=document_question_answering(text, image)
                    # qa_output=document_question_answering(text, url)
                    for item in qa_output:
                        st.write(f"{item['answer']} : {item['score']:.2%}")
                    
class ComputerVision:
    def __init__(self) -> None:
        pass
    def computer_vision(self): 
        
        st.title("Computer Vision")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                ["Depth Estimation", "Image Classification",
                                  "Object Detection", "Text to Image", "Image to Text"],
                                placeholder="Select a subcategory")
        if select=="Depth Estimation":
            st.subheader("Depth Estimation")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            estimate_button_clicked = st.button("Estimate")
            if estimate_button_clicked:
                depth_estimator(image)
            
        if select =="Image Classification":
            st.subheader("Image Classification")
            with st.expander("Model Description"):
                st.markdown("""This model is an Image Classification model (google/vit-base-patch16-224) that is used to classify the image into different categories.
                            Provide an image to classify the image. The model predicts the labels and their scores.""")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            classify_button_clicked = st.button("Classify")
            if classify_button_clicked:
                image_classifier(image)
        
        if select =="Object Detection":
            st.subheader("Object Detection")
            with st.expander("Model Description"):
                st.markdown("""This model is an Object Detection model (facebook/detr-resnet-50) that is used to detect the objects in an image.
                            Provide an image to detect the objects. The model predicts the labels and their bounding boxes.""")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            detect_button_clicked = st.button("Detect")
            if detect_button_clicked:
                object_detector(image)
            
        if select =="Text to Image":
            st.subheader("Text to Image")
            with st.expander("Model Description"):
                st.markdown("""This model is a Text to Image model (openai/dall-e-13-3) that is used to generate an image from the given text.
                            Provide a text to generate an image. The model generates an image based on the text.""")
            st.divider()
            text = st.text_area("Enter your querry", placeholder="Astronaut riding a horse")
            create_button_clicked = st.button("Create Image")
            if create_button_clicked:
                text_to_image(text)
            
        if select =="Image to Text":
            st.subheader("Image to Text")
            with st.expander("Model Description"):
                st.markdown("""This model is an Image to Text model (microsoft/layoutlmv2-base-uncased) that is used to extract the text from an image.
                            Provide an image to extract the text. The model extracts the text from the image.""")
            st.divider()
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            describe_button_clicked = st.button("Describe")
            if describe_button_clicked:
                image_to_text(image)