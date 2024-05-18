import pathlib
import os
import requests
import streamlit as st
from audio_recorder_streamlit import audio_recorder
current_path=pathlib.Path(__file__)
root_path=current_path.parent.parent.parent
class AudioClassifier:
    def __init__(self) -> None:
        pass
    
    def audio_classifier_api(self, filename):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/MIT/ast-finetuned-audioset-10-10-0.4593"
            headers = {"Authorization": f"Bearer {Access_Token}"}
    
            def query(filename):
                with open(filename, "rb") as f:
                    data = f.read()
                response = requests.post(API_URL, headers=headers, data=data)
                return response.json()

            output = query(filename)
            return output
        
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

    def audio_classifier(self):
        file_folder = root_path / 'data'
        pathlib.Path.mkdir(file_folder,exist_ok=True)
        st.subheader("Audio Classification")
        with st.expander("Model Description"):
            st.markdown("""This model is an Audio Classification model (MIT/ast-finetuned-audioset-10-10) that is used to classify the audio into different categories.
                                Provide an audio file to classify the audio. The model predicts the labels and their scores.""")
        st.divider()
        with st.expander("Upload Audio"):
            filename = st.file_uploader(type=[".flac", ".wav", ".mp3"], label="Upload Audio")
            if filename is not None:
                # Save the uploaded file to the data folder
                file_path = file_folder / filename.name
                with open(file_path, 'wb') as f:
                    f.write(filename.read())
        with st.expander("Record Audio",expanded=True):
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
            
        
            
        classify_button_clicked = st.button("Classify")
        if classify_button_clicked:
            
            if filename is not None:
                audio_classifier_output=self.audio_classifier_api(file_path)
            elif audio is not None:
                audio_classifier_output=self.audio_classifier_api(audio_path)
            else:
                st.error("Please upload or record an audio file.")
            # st.text_area("Recognized Text", value=audio_classifier_output)
            if audio_classifier_output is not None:
                try:
                    for item in audio_classifier_output:
                        st.write(f"{item['label']} : {item['score']:.2%}")
                except TypeError:
                    st.info(audio_classifier_output)
                    
                    