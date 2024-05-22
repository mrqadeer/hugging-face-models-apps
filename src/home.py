# Import streamlit library
import streamlit as st
# Checking if the access token is present in the session state
if 'access' not in st.session_state:
    # If not present, set the access to False
    st.session_state.access=False 
    
# Define the Home class
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
        # Checking if the access token is not present in the session state
        if 'access_token' not in st.session_state:
            # If not present, set the access token to None
            st.session_state.access_token=None
        
        # Display the title of the Streamlit app      
        st.title("Hugging Face Models Showcase")

        # Prompt the user to enter the Hugging Face Access Token
        token=st.text_input("Hugging Face Access Token",type='password')
        # Provide a link to the user to get the access token
        st.markdown("Click here to get your [HuggingFace Access Token](https://huggingface.co/settings/tokens)")
        
        # Check if the user has entered the access token
        if len(token)>0:
            # If they have display the submit button
            submit=st.button("Submit")
            # If the submit button is clicked display the message
            if submit:
                st.info("Thanks for providing Access Token")
                # Store the access token in session state
                st.session_state.access_token=token
                
        # Display the Hugging Face logo
        st.image("https://huggingface.co/front/assets/huggingface_logo.svg")
        # Display the subheader
        st.subheader('A gold mine of models, datasets and tools.')
        # Display information about Hugging Face
        st.markdown("""Hugging Face is a company that provides a large collection of pre-trained models and tools 
                 for Natural Language Processing (NLP), Computer Vision, Multimodal, Audio, and other domains.""")

