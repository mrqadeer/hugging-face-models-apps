import requests
import pathlib
import streamlit as st
curr_path=pathlib.Path(__file__)
root_dir=curr_path.parent.parent.parent
from PIL import Image
from io import BytesIO
class ImageClassifier:
    def __init__(self) -> None:
        """
        Initializes the object of the class. 
        No parameters are taken, and the function returns None.
        """
        pass
    
    def image_classifier_api(self,image):
            """
            Executes image classification using the specified image.
            
            Parameters:
                self: The object instance.
                image: The image for classification.
            
            Returns:
                The classification output for the image.
            """
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

                output = query(image)
                output = output[0]
                return output
            except requests.ConnectionError as e:
                st.error("Connection error")
            except requests.ConnectTimeout as e:
                st.error("Connection timeout")
            except requests.RequestException as e:
                st.error("Request exception")
            except requests.HTTPError as e:
                st.error("HTTP error")
            except KeyError as e:
                st.warning('Try again...')
            except (Exception, ValueError) as e:
                st.error("Unknown error")
                
    def image_classifier(self):
        """
        Executes image classification using the specified image.
        
        Parameters:
            self: The object instance.
        
        Returns:
            None
        """
        st.subheader("Image Classification")
        with st.expander("Model Description"):
            st.markdown("""This model is an Image Classification model (google/vit-base-patch16-224) that is used to classify the image into different categories.
                            Provide an image to classify the image. The model predicts the labels and their scores.""")
        st.divider()
        with st.expander("Upload Image"):
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            if image is not None:
                st.image(image)
            
        with st.expander("Enter Image URL"):
            url=st.text_input("Enter image URL")
            if len(url)>=1:
            # Remove any leading backslashes
                if url.startswith("\\"):
                    image_url = url[1:]
                image_data=self.image_downlaod(url)
                if image_data is not None:
                    st.image(Image.open(BytesIO(image_data)))
                    path=root_dir / 'data'
                    image_path=path/'image.png'
                    
                    with open(image_path,'wb') as f:
                        f.write(image_data)
            
           
        describe_button_clicked = st.button("Describe")
        if describe_button_clicked:
            if image is not None:
                path=root_dir / 'data'
                image_name=path/image.name
                with open(image_name,'wb') as f:
                    f.write(image.getbuffer())
                output=self.image_classifier_api(image_name)
            
            elif len(url)>=1:
                
                output=self.image_classifier_api(image_path)
            else:
                st.stop()
            try:
                for item in output:
                    st.info(f"{item['label']}: {item['score']:.2%}")
            except:
                st.info(output)
    @staticmethod
    def image_downlaod(url:str):
        """
        A function that downloads an image from a given URL using requests library.

        Parameters:
            url: The URL of the image to download.

        Returns:
            The content of the downloaded image if the download is successful, otherwise None.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            st.error("Failed to download image.")
            return None
                        