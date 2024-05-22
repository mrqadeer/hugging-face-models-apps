# Import necessary libraries
import requests
import pathlib
import streamlit as st
from PIL import Image
from io import BytesIO

# Getting the path of the current file
current_path=pathlib.Path(__file__)
# Getting the root path of the project
root_path=current_path.parent.parent.parent


# Defining the class
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
        # Getting the access token from the session state  
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
            # Specify the headers for API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Define the query function to send the post request (image) to the API 
            def query(filename):
                # Open the file in read binary mode
                with open(filename, "rb") as f:
                    # Read the file data
                    data = f.read()
                # Send post request to the API
                response = requests.post(API_URL, headers=headers, data=data)
                # Return the response in jason format
                return response.json()
           
            # Call the query function
            output = query(image)
            return output
        
        # Handling exceptions
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
    
    # Defining method to detect objects in provided image
    def object_detector(self):
        """
        A function to perform object detection using the input image.
        
        Parameters:
            None
        
        Returns:
            None
        """
        # Adding a subheader to the streamlit app
        st.subheader("Object Detection")
        # Adding expander to describe the model
        with st.expander("Model Description"):
            st.markdown("""This model is an Object Detection model (facebook/detr-resnet-50) that is used to detect the objects in an image.
                            Provide an image to detect the objects. The model predicts the labels and their bounding boxes.""")
        st.divider()
        # Creating a folder to store the image file
        path=root_path / 'data'
        # Creating the folder if it does not exist 
        pathlib.Path.mkdir(path,exist_ok=True)
        
        # Adding an expander to upload the image
        with st.expander("Upload Image",expanded=True):
            # Uploading the image
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            # Checking if the image is uploaded
            if image is not None:
                # Display the image
                st.image(image)
        
        # Adding an expander to enter the url     
        with st.expander("Enter Image URL",expanded=True):
            # getting image url from the user
            url=st.text_input("Enter image URL")
            # Checking if the image url is not empty
            if len(url)>=1:
                # Downloading image from the url
                image_data=self.image_downlaod(url)
                # Checking if the image is downloaded
                if image_data is not None:
                    # Display the image
                    st.image(Image.open(BytesIO(image_data)))
                    # Save image to data folder
                    image_path=path/'image.png'
                    # Open file in write binary mode
                    with open(image_path,'wb') as f:
                        f.write(image_data)
            
        # Adding button to dettect objects in the image
        detect_button_clicked = st.button("Detect")
        # Checking if detect button is clicked
        if detect_button_clicked:
            # Checking if the image is uploaded or the URL is entered
            if image is not None:
                # Save the image to data folder
                image_name=path/image.name
                # Open the file in write binary mode
                with open(image_name,'wb') as f:
                    # write the image data to the file
                    f.write(image.getbuffer())
                # Calling the function with image path   
                output=self.object_detector_api(image_name)
            # Checking if an image is not uploaded but a URL is entered
            elif len(url)>=1:
                # Call the method with the image path downloaded from the URL
                output=self.object_detector_api(image_path)
            else:
                # If image or url is not entered stop the execution of script
                st.stop()
                
            if output is not None:
                try:
                    # Iterate over the output dictionary representing label and its corresponding score
                    for item in output:
                        # Display the label and score (formated as percentage with 2 decimal places)
                        st.info(f"{item['label']}: {item['score']:.2%}")
                except:
                    # If an error occurs during the itteration display output in info message
                    st.info(output)
                    
    # Define a static method that downloads as image from a given url 
    @staticmethod
    def image_downlaod(url):
        """
        A function that downloads an image from a given URL using requests library.

        Parameters:
            url: The URL of the image to download.

        Returns:
            The content of the downloaded image if the download is successful, otherwise None.
        """
        # send get request to provided url
        response = requests.get(url)
        # Check if the status code of the response is 200 i.e OK
        if response.status_code == 200:
            # If status is OK return content of the response
            return response.content
        else:
            # If the status code is not 200 display error message and return none
            print("Failed to download image.")
            return None