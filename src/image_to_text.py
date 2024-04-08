import requests
import streamlit as st

def image_to_text(image):
    Access_Token = "" # Add your access token here
    try:
        API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
        headers = {"Authorization": f"Bearer {Access_Token}"}

        def query(filename):
            with open(filename, "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query(image)
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
