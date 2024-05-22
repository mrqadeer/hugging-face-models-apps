# Import necessary libraries
import pathlib
import requests
import os
import base64
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import tempfile

# Getting the path of the current file
current_path=pathlib.Path(__file__)
# Getting the root path of the project
root_path=current_path.parent.parent.parent



# Defining the class
class AudioToAudio:
    """ Initializing the object of the class with no parameters and returns None."""
    def __init__(self) -> None:
        pass
    #Defining method to convert audio to audio
    def audio_to_audio_api(self,filename):
        """ Function to convert audio to audio using the Hugging Face API.
        Parameters:
            filename (str): The path of the audio file to convert.
        Returns:
            output (dict): The output of the audio conversion model."""
            
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            # API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
            API_URL = "https://api-inference.huggingface.co/models/speechbrain/mtl-mimic-voicebank"
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
            # Returning the blob from the output
            return output[0]['blob']
        
        # Handling the exceptions
        except requests.ConnectionError as e:
            st.error("Connection error")
        except requests.ConnectTimeout as e:
            st.error("Connection timeout")
        except requests.RequestException as e:
            st.error("Request exception")
        except requests.HTTPError as e:
            st.error("HTTP error")
        # except KeyError as e:
        #     st.error("Try again...")
        # except (Exception, ValueError) as e:
        #     st.error("Unknown error")

    # Defining the method to convert audio to audio process
    def audio_to_audio(self):
    
        # Creating a folder to store the audio files
        file_folder = root_path / 'data'
        # Creating the folder if it does not exist
        pathlib.Path.mkdir(file_folder,exist_ok=True)
        # Adding the subheader to the streamlit app
        st.subheader("Automatic Speech Recognition")
        # Adding an expander for the model description
        with st.expander("Model Description"):
            st.markdown("""This model is a Speech Recognition model (facebook/wav2vec2-large-960h-lv60-self) that is used to recognize the text from an audio file.
                                The model predicts transcriptions in the same language as the audio. Provide an audio file to recognize the text.""")
        st.divider()

        # Adding an expander for the upload audio file
        with st.expander("Upload Audio File", expanded=True):
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            # Checking if the file was uploaded
            if filename is not None:
                st.audio(filename)
                # Defining the path to save the uploaded file
                file_path = file_folder / filename.name
                # Save the uploaded file to the data folder
                with open(file_path, 'wb') as f:
                    f.write(filename.read())
                    
        # Adding an expander for recording audio            
        with st.expander("Record Audio", expanded=True):
            # Adding an audio recorder
            audio=audio_recorder(text="Click Icon to Record",
            recording_color="#e8b62c",
            neutral_color="#6aa36f",
            icon_name="microphone",
            icon_size="2x",
            )
            # Checking if an audio was recorded
            if audio is not None:
                st.audio(audio)
                # Defining the path to save the recorded audio file
                audio_path = os.path.join(root_path/'data', 'audio_file.wav')
                # Saving the recorded audio file
                with open(audio_path, 'wb') as f:
                    f.write(audio)
                st.success("Thanks for recording your voice!")
                # Updating the audio path
                audio_path=root_path/'data'/'audio_file.wav'
           
        # Adding a button to denoise the audio         
        denoise_button = st.button("Denoise")
        # Checking if the denoise button was clicked
        if denoise_button:
            # Checking if the file was uploaded or an audio was recorded
            if filename is not None:
                # Calling the audio to audio API function using the file path
                audio_output =self.audio_to_audio_api(file_path)
            elif audio is not None:
                # Calling the audio to audio API function using the recorded audio
                audio_output =self.audio_to_audio_api(audio_path)
            else:
                st.error("Please upload or record an audio file.")
                st.stop()
            
            # Checking if the audio output is not None
            if audio_output is not None:
                # Converting the audio output from string to bytes
                audio_output=self.string_to_audio(audio_output)
                # Displaying the audio output
                st.audio(audio_output)
                # Adding a download button to download the audio output
                st.download_button(label="Download Audio", data=audio_output, file_name="audio_output.mp3", mime="audio/flac")
    
    # Defining a static method to convert string to audio
    @staticmethod
    def string_to_audio(text:str):
        """
        Function to convert a string to audio bytes.
        
        Parameters:
            text (str): The text to convert to audio bytes.

        Returns:
            audio_bytes (bytes): The audio bytes converted from the text.
        """
        # Decoding the text from base64 to bytes
        audio_bytes = base64.b64decode(text)
        # Creating a temporary file to store the audio
        file_path = root_path / 'data'/'output_audio.wav'
        
        # Writing the audio bytes to the binary file
        with open(file_path, "wb") as audio_file:
            audio_file.write(audio_bytes)
        # Reading the audio file
        with open(file_path, 'rb') as f:
            audio_bytes = f.read()
        return audio_bytes