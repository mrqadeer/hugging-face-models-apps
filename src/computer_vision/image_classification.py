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
            # Getting the access token from the session state
            Access_Token = st.session_state.access_token
            try:
                # Specify the Hugging Face model API URL
                API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
                # Specify the headers for API request
                headers = {"Authorization": f"Bearer {Access_Token}"}

                # Define the query function to send the post request (image) to the API
                def query(filename):
                    # Open the file in read-binary mode
                    with open(filename, "rb") as f:
                        # Read the file data
                        data = f.read()
                    # Send the post request to the API
                    response = requests.post(API_URL, headers=headers, data=data)
                    # Return the response in JSON format
                    return response.json()
                # Call the query function and sort the output
                output = query(image)
                # return the first output from the sorted list of outputs
                output = output[0]
                return output
            
            # Handling the exceptions
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
    
    # Defining the method to classify the image            
    def image_classifier(self):
        """
        Executes image classification using the specified image.
        
        Parameters:
            self: The object instance.
        
        Returns:
            None
        """
        # Adding a subheader to the streamlit app
        st.subheader("Image Classification")
        # Creating a folder to store the image file
        path=root_path / 'data'
        # Creating the folder if it does not exist
        pathlib.Path.mkdir(path,exist_ok=True)
        # Adding an expander for the model description
        with st.expander("Model Description"):
            st.markdown("""This model is an Image Classification model (google/vit-base-patch16-224) that is used to classify the image into different categories.
                            Provide an image to classify the image. The model predicts the labels and their scores.""")
        st.divider()
       
        # Adding an expander to upload the image
        with st.expander("Upload Image",expanded=True):
            # Uploading the image
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            # Checking if the image is uploaded
            if image is not None:
                # Display the image
                st.image(image)
         
        # Adding an expander to enter the image URL    
        with st.expander("Enter Image URL",expanded=True):
            # Getting the image URL from user
            url=st.text_input("Enter image URL")
            # Checking if the URL is not empty
            if len(url)>=1:
                # Downloading the image from the URL
                image_data=self.image_downlaod(url)
                # Checking if the image is downloaded
                if image_data is not None:
                    # Display the image
                    st.image(Image.open(BytesIO(image_data)))
                    # Save the image to the data folder
                    image_path=path/'image.png'
                    # Open the file in write binary mode
                    with open(image_path,'wb') as f:
                        f.write(image_data)
            
        # Adding a button to describe the image  
        describe_button_clicked = st.button("Describe")
        # Checking if the describe button is clicked
        if describe_button_clicked:
            # Checking if the image is uploaded or the URL is entered
            if image is not None:
                # Save the image to the data folder
                image_name=path/image.name
                # Open the file in write binary mode
                with open(image_name,'wb') as f:
                    # Write the image data to the file
                    f.write(image.getbuffer())
                # Calling function with image path
                output=self.image_classifier_api(image_name)
            
            # If an image is not uploaded but a URL is entered
            elif len(url)>=1:
                # Call the method with the image path downloaded from the URL
                output=self.image_classifier_api(image_path)
            else:
                # If image or url is not entered stop the execution of script
                st.stop()
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
    def image_downlaod(url:str):
        """
        A function that downloads an image from a given URL using requests library.

        Parameters:
            url: The URL of the image to download.

        Returns:
            The content of the downloaded image if the download is successful, otherwise None.
        """
        # send a get request to the provided url
        response = requests.get(url)
        # Check if the status code of the response is 200 i.e OK
        if response.status_code == 200:
            # If status is OK return content of the response
            return response.content
        else:
            # If the status code is not 200 display error message and return none
            st.error("Failed to download image.")
            return None
                        