# importing the required libraries
import pathlib
import os
import requests
import streamlit as st
from audio_recorder_streamlit import audio_recorder

# Getting the path of the current file
current_path=pathlib.Path(__file__)
# Getting the root path of the project
root_path=current_path.parent.parent.parent

#Defining Class
class AudioClassifier:
    
    """Initializing the object of the class with no parameters and returns None."""
    def __init__(self) -> None:
        pass
    
    
    def audio_classifier_api(self, filename):
        """
        Function to classify the audio using the Hugging Face API.

        Parameter: filename (str): The path of the audio file to classify.

        Returns: output (dict): The output of the audio classification model.
        
        """
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
            # Specify the headers for API request
            headers = {"Authorization": f"Bearer {Access_Token}"}
    
            # Defining the query function to send the post request (audio file) to the API
            def query(filename):
                # Opening the file in read-binary mode
                with open(filename, "rb") as f:
                    # Reading the file data
                    data = f.read()
                # Sending the post request to the API
                response = requests.post(API_URL, headers=headers, data=data)
                # Returning the response in JSON format
                return response.json()
            
            # Calling the query function with the filename as the parameter
            output = query(filename)
            return output
        
        # Handling the exceptions
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

    # Deining a method for the audio classification process
    def audio_classifier(self):
        # Defining the folder to save the uploaded audio file
        file_folder = root_path / 'data'
        # Creating the folder if it does not exist
        pathlib.Path.mkdir(file_folder,exist_ok=True)
        # Adding a subheader to the Streamlit app
        st.subheader("Audio Classification")
        # Adding an expander for the model description
        with st.expander("Model Description"):
            st.markdown("""This model is an Audio Classification model (MIT/ast-finetuned-audioset-10-10-0.4593) that is used to classify the audio into different categories.
                                Provide an audio file to classify the audio. The model predicts the labels and their scores.""")
        st.divider()
        # Adding an expander for uploading audio file
        with st.expander("Upload Audio"):
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            # Checking if the file was uploaded
            if filename is not None:
                # Defining the path to save the uploaded file
                file_path = file_folder / filename.name
                # Saving the uploaded file 
                with open(file_path, 'wb') as f:
                    f.write(filename.read())
        # Adding an expander for recording audio
        with st.expander("Record Audio",expanded=True):
            audio=audio_recorder(text="Click Icon to Record",
            recording_color="#e8b62c",
            neutral_color="#6aa36f",
            icon_name="microphone",
            icon_size="2x",
            
            )
            # Checking if audio was recorded
            if audio is not None:
                # Adding the recorded audio file 
                st.audio(audio)
                # Defining the path to save the recorded audio file
                audio_path = os.path.join(root_path/'data', 'audio_file.wav')
                # Saving the recorded audio file
                with open(audio_path, 'wb') as f:
                    f.write(audio)
                # Displaying a success message
                st.success("Thanks for recording your voice!")
                audio_path=root_path/'data'/'audio_file.wav'
            
        # Adding a button to classify the audio
        classify_button_clicked = st.button("Classify")
        # Checking if the classify button was clicked
        if classify_button_clicked:
            # Checking if the file was uploaded or an audio was recorded
            if filename is not None:
                # Calling the audio classification function API with the uploaded file
                audio_classifier_output=self.audio_classifier_api(file_path)
            elif audio is not None:
                # Calling the audio classification function API with the recorded audio
                audio_classifier_output=self.audio_classifier_api(audio_path)
            else:
                # Displaying an error message if no audio file was uploaded or recorded
                st.error("Please upload or record an audio file.")
            # st.text_area("Recognized Text", value=audio_classifier_output)
            if audio_classifier_output is not None:
                try:
                    # Displaying the labels and scores of the audio classification output
                    for item in audio_classifier_output:
                        st.write(f"{item['label']} : {item['score']:.2%}")
                except TypeError:
                    st.info(audio_classifier_output)
                    
                    