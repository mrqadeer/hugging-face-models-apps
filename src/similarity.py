import requests
import streamlit as st

def sentence_similarity(source_sentence, list_of_sentences):
    Access_Token = "" # Add your access token here
    try:            
        API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
        headers = {"Authorization": f"Bearer{Access_Token}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({"inputs": source_sentence + list_of_sentences})
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