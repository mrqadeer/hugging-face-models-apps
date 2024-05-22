# Import necessary libraries
import requests
import streamlit as st
import base64
import pathlib
from PIL import Image 
from io import BytesIO

# Getting the path of the current file
current_path=pathlib.Path(__file__)
# Getting the root path of the project
root_path=current_path.parent.parent.parent

# Defining the class
class DocumentQuaestionAnswering:
    
    def __init__(self) -> None:
        """
        Initializes the object of the class. 
        No parameters are taken, and the function returns None.
        """
        pass
    
    # Defining the method to convert text to image
    def document_question_answering_api(self,text:str, image):
        """
        This function handles the document question answering API.
        It takes in the text and image as parameters and returns the output after querying the Hugging Face model API.
        """
        # Getting access token from the session state
        Access_Token = st.session_state.access_token
        
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/impira/layoutlm-document-qa"
            # Specify the header for API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Define the query function to send the post request (text) to the API
            def query(payload):
                # Open the image file in read binary mode
                with open(payload['inputs']['image'], "rb") as f:
                    # Read the image data
                    img = f.read()
                    # Encode the image data in base64 format
                    # Decode the base64 encoded image data to string format
                    # Assign it back to the image key in the payload
                    payload['inputs']['image'] = base64.b64encode(img).decode("utf-8")  
                # Send the post request to the API and store the response
                response = requests.post(API_URL, headers=headers, json=payload)
                # Return the response in JSON format
                return response.json()
            # Call the query function with the text as the argument
            output = query({"inputs": {"image": image,
		                    "question": text}
                            })
            return output
        
        # Handling exceptions
        except requests.ConnectionError as e:
            st.error("Connection error")
        except requests.ConnectTimeout as e:
            st.error("Connection timeout")
        except requests.RequestException as e:
            st.error("Request exception")
        # except (Exception, ValueError) as e:
        #     st.error("Unknown error")
        except requests.HTTPError as e:
            st.error("HTTP error")
        
    def document_question_answering(self):
        """
        This function handles the document question answering. It interacts with the Streamlit library to prompt the user to upload an image, enter a query, and process the query using the 'document_question_answering_api' method. It displays the answer and its corresponding score.
        """
        # Adding subheader for the document question answering in streamlit app
        st.subheader("Document Question Answering")
        # Adding expander for model description
        with st.expander("Model Description"):
            st.markdown("""This model is a Document Question Answering model (impira/layoutlm-document-qa) that is used to 
                            extract the answer from the tabular data in the provided document. The model accepts an image to extract the text and then answer the question.""")
        st.divider()
        
        st.divider()
        # Getting the root directory path
        path=root_path / 'data'
        # Creating the directory if it does not exist
        pathlib.Path.mkdir(path,exist_ok=True)
        # Adding expander for the user to upload an image
        with st.expander("Upload Image",expanded=True):
            # Adding file uploader to upload an image
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            # Checking if the image is uploaded
            if image is not None:
                # Displaying the image
                st.image(image)
        
        # Adding expander for the user to enter the image URL    
        with st.expander("Enter Image URL",expanded=True):
            # Adding text input to enter the image URL
            url=st.text_input("Enter image URL")
            # Checking if the URL is not empty
            if len(url)>=1:
                # Downloading the image from the URL
                image_data=self.image_downlaod(url)
                # Checking if the image data is downloaded 
                if image_data is not None:
                    # Display the downloaded image
                    st.image(Image.open(BytesIO(image_data)))
                    # Specify the path to save the image
                    image_path=path/'image.png'
                    # Open the fine write binary mode
                    with open(image_path,'wb') as f:
                        # Write the image data to the file
                        f.write(image_data)
            
        # Adding button to process the image   
        process_button = st.button("Process")
        # Checking if the Process button is clicked
        if process_button:
            # Checking if the image is uploaded
            if image is not None:
                # Specify the path to save the image
                image_name=path/image.name
                # Open the file in write binary mode
                with open(image_name,'wb') as f:
                    # Write the image data to the file
                    f.write(image.getbuffer())
                # Call the document_question_answering_api function with the image path
                output=self.document_question_answering_api(image_name)
            # Checking if the URL is entered
            elif len(url)>=1:
                # Call the document_question_answering_api function with the image path
                output=self.document_question_answering_api(image_path)
            else:
                # Display error message if no image is uploaded or URL is entered
                st.stop()
            try:
                # Iterate over the output and display the label and score
                for item in output:
                    # Display the label and score in percentage with 2 decimal points
                    st.info(f"{item['label']}: {item['score']:.2%}")
            except:
                # If an error occurs, display the output
                st.info(output)
   
    # Define the static method to download the image           
    @staticmethod
    def image_downlaod(url:str):
        """
        A function that downloads an image from a given URL using requests library.

        Parameters:
            url: The URL of the image to download.

        Returns:
            The content of the downloaded image if the download is successful, otherwise None.
        """
        # Send a get request to the URL
        response = requests.get(url)
        # Check if the response status code is 200 i.e successful/OK
        if response.status_code == 200:
            # If the status code is 200, return the content of the image
            return response.content
        else:
            # If status code is not 200, display message
            st.error("Failed to download image.")
            return None