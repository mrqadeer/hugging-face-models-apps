import requests
import io
from PIL import Image
import streamlit as st

class TextToImageGenerator:
    def __init__(self) -> None:
        pass
    
    def text_to_image_api(text):
        Access_Token = st.session_state.access_token 
        try: 
            API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.content
            image_bytes = query({
                "inputs": text,
            })
            
            image = Image.open(io.BytesIO(image_bytes)) 
            return image   
        
        except requests.ConnectionError as e:
            st.error("Connection error")
        except requests.ConnectTimeout as e:
            st.error("Connection timeout")
        except requests.RequestException as e:
            st.error("Request exception")
        except (Exception, ValueError) as e:
            st.error("Unknown error")
        except requests.HTTPError as e:
            st.error("HTTP error")
    
    def text_to_image(self):
        st.subheader("Text to Image")
        with st.expander("Model Description"):
            st.markdown("""This model is a Text to Image model (openai/dall-e-13-3) that is used to generate an image from the given text.
                            Provide a text to generate an image. The model generates an image based on the text.""")
        st.divider()
        text = st.text_area("Enter your querry", placeholder="Astronaut riding a horse")
        create_button_clicked = st.button("Create Image")
        if create_button_clicked:
            self.text_to_image_api(text)