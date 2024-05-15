import streamlit as st
import requests

def text_to_speech(text):
    Access_Token = st.session_state.access_token
    try:
        API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
        headers = {"Authorization": f"Bearer {Access_Token}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        audio_bytes = query({"inputs": text})

        from IPython.display import Audio
        Audio(audio_bytes)
        
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
  