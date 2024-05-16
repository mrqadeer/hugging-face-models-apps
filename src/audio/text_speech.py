import streamlit as st
import requests

class TextSpeech:
    def __init__(self) -> None:
        pass
    def text_to_speech_api(text):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.content

            audio_bytes = query({"inputs": text})

            return audio_bytes
            
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

    def text_to_speech(self):
        st.subheader("Text to Speech")
        with st.expander("Model Description"):
            st.markdown("""This model is a TTS model (facebook/mms-tts-eng) that is used to convert text into speech. 
                                Provide a text to convert into speech. You can also download the output audio.""")
        st.divider()
        text = st.text_area("Enter your Text", placeholder="The universe is vast and mysterious and holds countless wonders waiting to be discovered")
        speak_button_clicked = st.button("Get Speech")
        if speak_button_clicked:
            audio_output=self.text_to_speech_api(text)
            st.audio(audio_output)
            st.download_button(label="Download Audio", data=audio_output, file_name="audio_output.mp3", mime="audio/flac")
        else:
            st.write("Click the button to convert your text into speech")  