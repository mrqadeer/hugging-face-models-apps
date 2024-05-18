import pathlib
import requests
import os
import streamlit as st
from audio_recorder_streamlit import audio_recorder


current_path=pathlib.Path(__file__)
root_path=current_path.parent.parent.parent
import tempfile
class SpeechRecognition:
    def __init__(self) -> None:
        pass

    def speech_recognition_api(self,filename):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(filename):
                with open(filename, "rb") as f:
                    data = f.read()
                response = requests.post(API_URL, headers=headers, data=data)
                return response.json()

            output = query(filename)
            return output['text']
        
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

    def speech_recognition(self):
        file_folder = root_path / 'data'
        pathlib.Path.mkdir(file_folder,exist_ok=True)
        st.subheader("Automatic Speech Recognition")
        with st.expander("Model Description"):
            st.markdown("""This model is a Speech Recognition model (facebook/wav2vec2-large-960h-lv60-self) that is used to recognize the text from an audio file.
                                The model predicts transcriptions in the same language as the audio. Provide an audio file to recognize the text.""")
        st.divider()
        
        with st.expander("Upload Audio File", expanded=True):
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            if filename is not None:
                    
                # Save the uploaded file to the data folder
                file_path = file_folder / filename.name
                with open(file_path, 'wb') as f:
                    f.write(filename.read())
        with st.expander("Record Audio", expanded=True):
        
            audio=audio_recorder(text="Click Icon to Record",
            recording_color="#e8b62c",
            neutral_color="#6aa36f",
            icon_name="microphone",
            icon_size="2x",
            
            )
            if audio is not None:
                st.audio(audio)
                
                audio_path = os.path.join(root_path/'data', 'audio_file.wav')
                with open(audio_path, 'wb') as f:
                    f.write(audio)
                st.success("Thanks for recording your voice!")
                audio_path=root_path/'data'/'audio_file.wav'
            
            
        
        
                        
        recognize_button = st.button("Recognize")
        if recognize_button:
            # Call your speech recognition function using the file path
            if filename is not None:
                speech_recognition_output =self.speech_recognition_api(file_path)
            elif audio is not None:
                speech_recognition_output =self.speech_recognition_api(audio_path)
            else:
                st.error("Please upload or record an audio file.")
            st.text_area("Recognized Text", value=speech_recognition_output)