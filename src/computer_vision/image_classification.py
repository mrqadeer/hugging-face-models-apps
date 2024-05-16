import requests
import streamlit as st

class ImageClassifier:
    def __init__(self) -> None:
        pass
    
    def image_classifier_api(image):
            Access_Token = st.session_state.access_token
            try:
                API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
                headers = {"Authorization": f"Bearer {Access_Token}"}

                def query(filename):
                    with open(filename, "rb") as f:
                        data = f.read()
                    # data=filename
                    response = requests.post(API_URL, headers=headers, data=data)
                    return response.json()

                output = query("/content/downloaded_image.jpg")
                output = output[0]
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
                
    def image_classifier(self):
        st.subheader("Image Classification")
        with st.expander("Model Description"):
            st.markdown("""This model is an Image Classification model (google/vit-base-patch16-224) that is used to classify the image into different categories.
                            Provide an image to classify the image. The model predicts the labels and their scores.""")
        st.divider()
        image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
        classify_button_clicked = st.button("Classify")
        if classify_button_clicked:
            self.image_classifier_api(image)