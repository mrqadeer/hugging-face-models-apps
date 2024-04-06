import requests
import streamlit as st

def text_to_audio(text):
    Access_Token = "" # Add your access token here
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
  