
import requests
import streamlit as st
from gradio_client import Client
class TextGeneration:
    def __init__(self) -> None:
        pass
    
    def text_generation_api(self,text):
        try:
            Access_Token = st.session_state.access_token
            client = Client("ysharma/Chat_with_Meta_llama3_8b")
            result = client.predict(
                    message=text,
                    request=0.5,
                    param_3=512,
                    api_name="/chat")
            return result.strip("assistant\n\n")
            
        except client.ConnectionError as e:
            st.error("Connection error")
        
     

    def text_generation(self):
        st.subheader("Text Generation")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="Write a story about unicorns and rainbows.")
        done=False if len(text)>1 else True
        generate_button_clicked = st.button("Generate",disabled=done)
        if generate_button_clicked:
            output=self.text_generation_api(text)
            if output is not None:
                st.info(output)
            else:
                st.warning("Sorry I was unable to generate your text")
        else:
            st.write("Click the button to generate content.")