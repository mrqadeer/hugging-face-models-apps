import requests
import streamlit as st
class FeatureExtraction:
    def __init__(self) -> None:
        pass
    def feature_extraction_api(self,text):
        Access_Token = st.session_state.access_token
        
        try:
            API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": text,
            })
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
    def feature_extraction(self):
        st.subheader("Feature Extraction")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="Today is a sunny day and I will get some ice cream.")
        extract_button_clicked = st.button("Extract")
        if extract_button_clicked:
            self.feature_extraction_api(text)
        else:
            st.write("Click the button to extract features")