import streamlit as st 
from src.sentiment_analysis import sentiment_analysis

from src.token_classification import token_classification
from src.table_qa import table_question_answering
from src.text_speech import text_to_speech
from src.text_to_audio import text_to_audio
from src.speech_recognition import speech_recognition
from src.audio_classification import audio_classifier
from src.zero_shot_classification import zero_shot_classification
from src.extract_feature import extract_feature
from src.summarization import text_summarizer
from src.translation import text_translator
from src.text_generation import text_generator
from src.fill_mask import fill_mask
#from similarity import sentence_similarity


class ModelZone:
    def __init__(self) -> None:
        pass
    
    def nlp(self):
        st.title("Naural Language Processing (NLP)")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                ["Sentiment Analysis", "Name Entity Recognition", "Table Answer Question",
                                   "Zero-Shot Classification", "Feature Extraction", "Text Summarization",
                                   "Translation", "Text Generation", "Fill Mask", "Sentence Similarity"],
                                placeholder="Select a subcategory")
            
        if select=="Sentiment Analysis":
            st.subheader("Sentiment Analysis")
            st.divider()

            text=st.text_area("Enter your Text",placeholder="I like you, I love you")
            do_sentiment=st.button("Analyze")
            if do_sentiment:
                token=st.session_state
                output=sentiment_analysis(text,token)
                st.info(output)

            text=st.text_area("Enter your Text", placeholder="universe is full of wonders.")
            analyse_button_clicked = st.button("Analyse")
            if analyse_button_clicked:
                sentiment_analysis(text)
            else:
                st.write("Click the button to analyse the sentiment of the text")
            
        if select=="Name Entity Recognition":
            st.subheader("Name Entity Recognition")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="My name is Sarah Jessica Parker but you can call me Jessica")
            identify_button_clicked = st.button("Identify")
            if identify_button_clicked:
                token_classification(text)
            else:
                st.write("Click the button to identify the name entity in the text")
            
        if select=="Table Answer Question":
            st.subheader("Table Answer Question")
            st.divider()
            text=st.text_area("Enter your querry", placeholder={
                                                    "query": "How many stars does the transformers repository have?",
                                                    })
            table=st.text_area("Share the table", placeholder = {
                                                    "Repository": ["Transformers", "Datasets", "Tokenizers"],
                                                    "Stars": ["36542", "4512", "3934"],
                                                    "Contributors": ["651", "77", "34"],
                                                    "Programming language": ["Python","Python","Rust, Python and NodeJS"]})
            extract_button_clicked = st.button("Extract")
            if extract_button_clicked:
                table_question_answering(text,table)
            else:
                st.write("Click the button to extract the information from the table")
            
        if select=="Zero-Shot Classification":
            st.subheader("")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="")
            zc_button_clicked = st.button("Zero-Shot")
            if zc_button_clicked:
                zero_shot_classification(text)
            else:
                st.write("Click the button for zero-shot classification.")
                
        if select=="Feature Extraction":
            st.subheader("Feature Extraction")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="Today is a sunny day and I will get some ice cream.")
            extract_button_clicked = st.button("Extract")
            if extract_button_clicked:
                extract_feature(text)
            else:
                st.write("Click the button to extract features")
                
        if select=="Text Summarization":
            st.subheader("Text Summarization")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.")
            summarize_button_clicked = st.button("Summarize")
            if summarize_button_clicked:
                text_summarizer(text)
            else:
                st.write("Click the button to summarize text.")
                
        if select=="Translation":
            st.subheader("Translation")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="Меня зовут Вольфганг и я живу в Берлине")
            translate_button_clicked = st.button("Translate")
            if translate_button_clicked:
                text_translator(text)
            else:
                st.write("Click the button to translate.")
                
        if select=="Text Generation":
            st.subheader("Text Generation")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="Write a story about unicorns and rainbows.")
            generate_button_clicked = st.button("Generate")
            if generate_button_clicked:
                text_generator(text)
            else:
                st.write("Click the button to generate content.")
                
        if select=="Fill Mask":
            st.subheader("Fill Mask")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="The answer to the universe is [MASK].")
            mask_button_clicked = st.button("FillMask")
            if mask_button_clicked:
                fill_mask(text)
            else:
                st.write("Click the button to")
                

        # if select=="Sentence Similarity":
        #     st.subheader("Sentence Similarity")
        #     st.divider()
        #     source_sentence=st.text_area("Enter sentence", placeholder="That is a happy person")
        #     list_of_sentences=st.text_area("Enter list of sentences", placeholder=[
        #                                                             "That is a happy dog",
        #                                                             "That is a very happy person",
        #                                                             "Today is a sunny day"])
        #     find_button_clicked = st.button("Find Similarity")
        #     if find_button_clicked:
        #         sentence_similarity(source_sentence, list_of_sentences)
        #     else:
        #         st.write("Click the button to check similarity")

        if select=="Sentence Similarity":
            st.subheader("Sentence Similarity")
            st.divider()
            text=st.text_area("Enter your Text", placeholder="")
            find_button_clicked = st.button("Find Similarity")
            if find_button_clicked:
                sentence_similarity(text)
            else:
                st.write("Click the button to")

    
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
            filename = st.file_uploader(type="audio")
            recognize_button_clicked = st.button("Recognize")
            if recognize_button_clicked:
                speech_recognition(filename)
            
        if select=="Audio Classification":
            st.subheader("Audio Classification")
            st.divider()
            audio = st.file_uploader(type="audio")
            classify_button_clicked = st.button("Classify")
            if classify_button_clicked:
                audio_classifier(audio)
            
    def multimodal(self):
        st.title("Multimodal")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                ["Document Q/A", "Depth Estimation", "Image Classification",
                                  "Object Detection", "Text to Image", "Image to Text"],
                                placeholder="Select a subcategory")
    
        # if select=="Document Q/A":
        #     st.subheader("Document Question Answering")
        #     st.divider()
        #     text = st.text_box("Enter your querry", placeholder="")
        #     image = st.file_uploader(type="image")
        #     process_button_clicked = st.button("Process")
        #     if process_button_clicked:
        #         document_question_answering(text, image)
            
        # if select=="Depth Estimation":
        #     st.subheader("Depth Estimation")
        #     st.divider()
        #     image = st.file_uploader(type="image")
        #     estimate_button_clicked = st.button("Estimate")
        #     if estimate_button_clicked:
        #         depth_estimator(image)
            
        # if select =="Image Classification"
        #     st.subheader("Image Classification")
        #     st.divider()
        #     image = st.file_uploader(type="image")
        #     classify_button_clicked = st.button("Classify")
        #     if classify_button_clicked:
        #         image_classifier(image)
        
        # if select =="Object Detection"
        #     st.subheader("Object Detection")
        #     st.divider()
        #     image = st.file_uploader(type="image")
        #     detect_button_clicked = st.button("Detect")
        #     if detect_button_clicked:
        #         object_detector(image)
            
        # if select =="Text to Image"
        #     st.subheader("Text to Image")
        #     st.divider()
        #     text = st.text_box("Enter your querry", placeholder="")
        #     create_button_clicked = st.button("Create Image")
        #     if create_button_clicked:
        #         text_to_image(text)
            
        # if select =="Image to Text"
        #     st.subheader("Image to Text")
        #     st.divider()
        #     image = st.file_uploader(type="image")
        #     describe_button_clicked = st.button("Describe")
        #     if describe_button_clicked:
        #         image_to_text(image)