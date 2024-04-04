import streamlit as st 
from src.sentiment_analysis import sentiment_analysis

class ModelZone:
    def __init__(self) -> None:
        pass
    def nlp(self):
        st.title("NLP App for Anila Baji")
        with st.sidebar:
            select=st.selectbox("What do you want to perform",
                                ["Sentiment Analysis","NER","Table Question Answer"]
                                ,placeholder="Select a subcategory")
        if select=="Sentiment Analysis":
            st.subheader("Sentiment Analysis")
            st.divider()
            text=st.text_area("Enter your Text",placeholder="I like you, I love you")
            do_sentiment=st.button("Analyze")
            if do_sentiment:
                token=st.session_state
                output=sentiment_analysis(text,token)
                st.info(output)
    
            