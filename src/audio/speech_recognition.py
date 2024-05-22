# Import necessary libraries
import pathlib
import requests
import os
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import tempfile

# Getting the path of the current file
current_path=pathlib.Path(__file__)
# Getting the root path of the project
root_path=current_path.parent.parent.parent

# Defining the class
class SpeechRecognition:
    # Initializing the object of the class with no parameters and returns None.
    def __init__(self) -> None:
        pass
  
    def speech_recognition_api(self,filename):
        """
        Function to convert audio to audio using the Hugging Face API.
        Parameters:
            filename (str): The path of the audio file to convert.
        Returns:
            output (dict): The output of the audio conversion model.
        """
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
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
            # Calling the query function and sorting the output
            output = query(filename)
            # Returning the text from the output
            return output['text']
        
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
            st.error("Could not generate.")
        except (Exception, ValueError) as e:
            st.error("Unknown error")

    # Defining the method to convert audio to audio
    def speech_recognition(self):
        # Creating a folder to store the audio file
        file_folder = root_path / 'data'
        # Creating the folder if it does not exist
        pathlib.Path.mkdir(file_folder,exist_ok=True)
        # Adding a subheader to the Streamlit app
        st.subheader("Automatic Speech Recognition")
        # Adding an expander for the model description
        with st.expander("Model Description"):
            st.markdown("""This model is a Speech Recognition model (facebook/wav2vec2-large-960h-lv60-self) that is used to recognize the text from an audio file.
                                The model predicts transcriptions in the same language as the audio. Provide an audio file to recognize the text.""")
        st.divider()
        # Adding an expander for the audio file upload
        with st.expander("Upload Audio File", expanded=True):
            # Adding a file uploader to upload the audio file
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            # Checking if the file is uploaded
            
            if filename is not None:
                # Save the uploaded file to the data folder
                file_path = file_folder / filename.name
                # Save the uploaded file to the data folder
                with open(file_path, 'wb') as f:
                    f.write(filename.read())
        # Adding an expander for recording audio            
        with st.expander("Record Audio", expanded=True):
            # Adding an audio recorder to record the audio
            audio=audio_recorder(text="Click Icon to Record",
            recording_color="#e8b62c",
            neutral_color="#6aa36f",
            icon_name="microphone",
            icon_size="2x",
            
            )
            # Checking if the audio is recorded
            if audio is not None:
                st.audio(audio)
                # Save the recorded audio file to the data folder
                audio_path = os.path.join(root_path/'data', 'audio_file.wav')
                # Save the recorded audio file to the data folder
                with open(audio_path, 'wb') as f:
                    f.write(audio)
                st.success("Thanks for recording your voice!")
                # Updating the audio path
                audio_path=root_path/'data'/'audio_file.wav'
            
        # Adding a button to recognize the audio                
        recognize_button = st.button("Recognize")
        # Checking if the recognize button is clicked
        if recognize_button:
            # Checking if the file is uploaded or the audio is recorded
            if filename is not None:
                # Calling the speech recognition function API 
                speech_recognition_output =self.speech_recognition_api(file_path)
             # Checking if the audio is recorded   
            elif audio is not None:
                # Calling the speech recognition function API
                speech_recognition_output =self.speech_recognition_api(audio_path)
            else:
                st.error("Please upload or record an audio file.")
            # Displaying the recognized text
            st.text_area("Recognized Text", value=speech_recognition_output)