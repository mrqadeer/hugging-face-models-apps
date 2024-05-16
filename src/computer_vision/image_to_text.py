import requests
import streamlit as st

class ImageToTextGenerator:
    def __init__(self) -> None:
        pass
    
    def image_to_text_api(image):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(filename):
                with open(filename, "rb") as f:
                    data = f.read()
                response = requests.post(API_URL, headers=headers, data=data)
                return response.json()

            output = query(image)
            return output
        
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

    def image_to_text(self):
        st.subheader("Image to Text")
        with st.expander("Model Description"):
            st.markdown("""This model is an Image to Text model (microsoft/layoutlmv2-base-uncased) that is used to extract the text from an image.
                            Provide an image to extract the text. The model extracts the text from the image.""")
        st.divider()
        image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
        describe_button_clicked = st.button("Describe")
        if describe_button_clicked:
            self.image_to_text_api(image)