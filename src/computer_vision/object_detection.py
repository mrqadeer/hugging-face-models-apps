import requests
import streamlit as st

class ObjectDetector:
    def __init__(self) -> None:
        pass
    
    def object_detector_api(image):
        Access_Token = st.session_state.access_token
        
        try:
            API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
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
    
    def object_detector(self):
        st.subheader("Object Detection")
        with st.expander("Model Description"):
            st.markdown("""This model is an Object Detection model (facebook/detr-resnet-50) that is used to detect the objects in an image.
                            Provide an image to detect the objects. The model predicts the labels and their bounding boxes.""")
        st.divider()
        image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
        detect_button_clicked = st.button("Detect")
        if detect_button_clicked:
            self.object_detector_api(image)