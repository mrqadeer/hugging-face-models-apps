import requests
import streamlit as st

class TextAudio:
    def __init__(self) -> None:
        pass
    
    def text_to_audio_api(text):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.content

            audio_bytes = query({
                "inputs": text,
            })
            # You can access the audio with IPython.display for example
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

    def text_to_audio(self):
        st.subheader("Text to Audio")
        with st.expander("Model Description"):
            st.markdown("""This model is a TTS model (facebook/musicgen-small) that is used to convert text into audio. 
                                Provide a text to convert into instrumental audio file. You can also download the output audio file.""")
        st.divider()
        text = st.text_area("Enter your Text", placeholder="liquid drum and bass, atmospheric synths, airy sounds")
        audio_button_clicked = st.button("Get Audio")
        if audio_button_clicked:
            text_to_audio_output=self.text_to_audio_api(text)
            st.audio(text_to_audio_output)
            st.download_button(label="Download Audio", data=text_to_audio_output, file_name="audio_output.mp3", mime="audio/flac")  