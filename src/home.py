import streamlit as st
if 'access' not in st.session_state:
    st.session_state.access=False 
class Home:
    def __init__(self):
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    def home(self):
        """
        The home function displays the HuggingFace Models webpage, prompts the user for a token input, 
        and provides information about Hugging Face company.
        """
        if 'access_token' not in st.session_state:
            st.session_state.access_token=None
                   
        st.title("HuggingFace Models")

        token=st.text_input("Hugging Face Token",type='password')
        st.markdown("Click here to get your [HuggingFace Access Token](https://huggingface.co/settings/tokens)")
        
        if len(token)>0:
            submit=st.button("Submit")
            if submit:
                st.info("Thanks for providing Access Token")
                st.session_state.access_token=token
                

        st.image("https://huggingface.co/front/assets/huggingface_logo.svg")
        st.subheader('A gold mine of models, datasets and tools.')
        
        st.markdown("""Hugging Face is a company that provides a large collection of pre-trained models and tools 
                 for Natural Language Processing (NLP), Computer Vision, Multimodal, Audio, and other domains.""")

