# import necessary libraries
import requests
import streamlit as st
import pathlib
import requests
from PIL import Image
from io import BytesIO

# Getting the path of the current file
current_path=pathlib.Path(__file__)
# Getting the root path of the project
root_path=current_path.parent.parent.parent

# Defining the class
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
            text (str): The generated text from the image.
        """
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
            # Specify the headers for API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Define the query function to send the post request (image) to the API 
            def query(filename):
                # Open the file in read-binary mode
                with open(filename, "rb") as f:
                    # Read the file data
                    data = f.read()
                # Send post request to the API
                response = requests.post(API_URL, headers=headers, data=data)
                # Return the response in jason format
                return response.json()
            # Call the query function and sort the output
            output = query(image)
            # return the first output from the sorted list of outputs
            return output[0]['generated_text']
        
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
            st.warning("Try again...")
        except (Exception, ValueError) as e:
            st.error("Unknown error")

    # Defining the method to describe the image
    def image_to_text(self):
        """
        A function that handles the process of converting an image to text. It allows the user to upload an image or provide an image URL. The function then processes the image to extract text content. If an image is uploaded, it retrieves the image data and passes it to the image_to_text_api to generate the text content. If an image URL is provided, it downloads the image data, saves it locally, and then uses the image_to_text_api to generate the text content. Finally, the function displays the generated text to the user.

        Parameters:
            self: The object instance.

        Returns:
            None
        """
        # Adding a subheader to the streamlit app
        st.subheader("Image to Text")
        # Adding an expander for the model description
        with st.expander("Model Description"):
            st.markdown("""This model is an Image to Text model (microsoft/layoutlmv2-base-uncased) that is used to extract the text from an image.
                            Provide an image to extract the text. The model extracts the text from the image.""")
        st.divider()
        # Creating a folder to store the image file
        path=root_dir / 'data'
        # Creating the folder if it does not exist 
        pathlib.Path.mkdir(path,exist_ok=True)
        
        # Adding an expander to upload the image
        with st.expander("Upload Image"):
            # Uploading the image
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            # Checking if the image is uploaded
            if image is not None:
                # Display the image
                st.image(image)
         
        # Adding an expander to enter the url    
        with st.expander("Enter Image URL"):
            # Getting the image url from the user
            url=st.text_input("Enter image URL")
            # Checking if url is not empty
            if len(url)>=1:
                # Downloading image from the url
                image_data=self.image_downlaod(url)
                # Checking if image is downloaded
                if image_data is not None:
                    # Display the image
                    st.image(Image.open(BytesIO(image_data)))
                    # Save image to data folder
                    image_path=path/'image.png'
                    # Open file in write binary mode
                    with open(image_path,'wb') as f:
                        f.write(image_data)
            
        # Adding button to describe the image   
        describe_button_clicked = st.button("Describe")
        # Checking if the Describe button is clicked
        if describe_button_clicked:
            # Checking if the image is uploaded or the URL is entered
            if image is not None:
                # Save the image to data folder
                image_name=path/image.name
                # Open the file in write binary mode
                with open(image_name,'wb') as f:
                    # write the image data to the file
                    f.write(image.getbuffer())
                # Calling the function with image path   
                output=self.image_to_text_api(image_name)
                
            # Checking if an image is not uploaded but a URL is entered
            elif len(url)>=1:
                 # Call the method with the image path downloaded from the URL
                output=self.image_to_text_api(image_path)
            else:
                # If image or url is not entered stop the execution of script
                st.stop()
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
        # send a get request to the provided url
        response = requests.get(url)
        # Check if the status code of the response is 200 i.e OK
        if response.status_code == 200:
            # If status is OK return content of the response
            return response.content
        else:
            # If the status code is not 200 display error message and return none
            print("Failed to download image.")
            return None