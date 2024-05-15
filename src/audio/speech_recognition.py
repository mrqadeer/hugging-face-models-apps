import requests
import streamlit as st

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
  