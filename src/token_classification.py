import requests
import streamlit as st
import keras
from transformers import pipeline
def token_classification(text):

    
    Access_Token = st.session_state.access_token
    
    try:    
        API_URL = "https://api-inference.huggingface.co/models/tsmatz/xlm-roberta-ner-japanese"
        headers = {"Authorization": f"Bearer {Access_Token}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({"inputs": text})
        return output
        
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
  