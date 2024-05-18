import requests
import pathlib
import streamlit as st
from PIL import Image
from io import BytesIO
curr_path=pathlib.Path(__file__)
root_dir=curr_path.parent.parent.parent
class ObjectDetector:
    def __init__(self) -> None:
        """
        Initializes the ObjectDetector class with no parameters and returns None.
        """
        pass
    
    def object_detector_api(self,image):
        """
        Function to perform object detection using the input image.

        Parameters:
            image: The image for object detection.

        Returns:
            The output of the object detection process.
        """
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
        """
        A function to perform object detection using the input image.
        
        Parameters:
            None
        
        Returns:
            None
        """
        st.subheader("Object Detection")
        with st.expander("Model Description"):
            st.markdown("""This model is an Object Detection model (facebook/detr-resnet-50) that is used to detect the objects in an image.
                            Provide an image to detect the objects. The model predicts the labels and their bounding boxes.""")
        st.divider()
        path=root_dir / 'data'
        pathlib.Path.mkdir(path,exist_ok=True)
        with st.expander("Upload Image"):
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            if image is not None:
                st.image(image)
            
        with st.expander("Enter Image URL"):
            url=st.text_input("Enter image URL")
            if len(url)>=1:
            
                image_data=self.image_downlaod(url)
                if image_data is not None:
                    st.image(Image.open(BytesIO(image_data)))
                    image_path=path/'image.png'
                    
                    with open(image_path,'wb') as f:
                        f.write(image_data)
            
           
        describe_button_clicked = st.button("Describe")
        if describe_button_clicked:
            if image is not None:
                
                image_name=path/image.name
                with open(image_name,'wb') as f:
                    f.write(image.getbuffer())
                output=self.object_detector_api(image_name)
            
            elif len(url)>=1:
                
                output=self.object_detector_api(image_path)
            else:
                st.stop()
            if output is not None:
                try:
                    for item in output:
                        st.info(f"{item['label']}: {item['score']:.2%}")
                except:
                    st.info(output)
    @staticmethod
    def image_downlaod(url):
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
            print("Failed to download image.")
            return None