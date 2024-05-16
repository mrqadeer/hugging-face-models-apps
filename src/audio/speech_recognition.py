import pathlib
import requests
import streamlit as st

current_path=pathlib.Path(__file__)
root_path=current_path.parent.parent

class SpeechRecognition:
    def __init__(self) -> None:
        pass

    def speech_recognition(filename):
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
        st.subheader("Automatic Speech Recognition")
        with st.expander("Model Description"):
            st.markdown("""This model is a Speech Recognition model (facebook/wav2vec2-large-960h-lv60-self) that is used to recognize the text from an audio file.
                                The model predicts transcriptions in the same language as the audio. Provide an audio file to recognize the text.""")
        st.divider()
        filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
        if filename is not None:
            file_folder = root_path / 'data'
            pathlib.Path.mkdir(file_folder,exist_ok=True)
                
            # Save the uploaded file to the data folder
            file_path = file_folder / filename.name
            with open(file_path, 'wb') as f:
                f.write(filename.read())
                        
            recognize_button = st.button("Recognize")
            if recognize_button:
                # Call your speech recognition function using the file path
                speech_recognition_output =self.speech_recognition_api(file_path)
                st.text_area("Recognized Text", value=speech_recognition_output)