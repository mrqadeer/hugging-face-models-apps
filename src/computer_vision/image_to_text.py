import requests
import streamlit as st
import pathlib
import requests
from PIL import Image
from io import BytesIO
curr_path=pathlib.Path(__file__)
root_dir=curr_path.parent.parent.parent
class ImageToTextGenerator:
    def __init__(self) -> None:
        """
        Initializes the object of the class. 
        No parameters are taken, and the function returns None.
        """
        pass
    
    def image_to_text_api(self,image):
        """
        Executes image to text conversion using the specified image.
        
        Parameters:
            self: The object instance.
            image: The image for text conversion.
        
        Returns:
            The generated text from the image.
        """
        Access_Token = st.session_state.access_token
        try:
            
            API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
            
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(filename):
                with open(filename, "rb") as f:
                    data = f.read()
                response = requests.post(API_URL, headers=headers, data=data)
                return response.json()

            output = query(image)
            return output[0]['generated_text']
        
        except requests.ConnectionError as e:
            st.error("Connection error")
        except requests.ConnectTimeout as e:
            st.error("Connection timeout")
        except requests.RequestException as e:
            st.error("Request exception")
        except requests.HTTPError as e:
            st.error("HTTP error")
        except KeyError as e:
            st.warning("Try again...")
        except (Exception, ValueError) as e:
            st.error("Unknown error")

    def image_to_text(self):
        """
        A function that handles the process of converting an image to text. It allows the user to upload an image or provide an image URL. The function then processes the image to extract text content. If an image is uploaded, it retrieves the image data and passes it to the image_to_text_api to generate the text content. If an image URL is provided, it downloads the image data, saves it locally, and then uses the image_to_text_api to generate the text content. Finally, the function displays the generated text to the user.

        Parameters:
            self: The object instance.

        Returns:
            None
        """
        st.subheader("Image to Text")
        with st.expander("Model Description"):
            st.markdown("""This model is an Image to Text model (microsoft/layoutlmv2-base-uncased) that is used to extract the text from an image.
                            Provide an image to extract the text. The model extracts the text from the image.""")
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
                output=self.image_to_text_api(image_name)
            
            elif len(url)>=1:
                
                output=self.image_to_text_api(image_path)
            else:
                st.stop()
            
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