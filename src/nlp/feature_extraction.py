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
        with st.expander("Model Description"):
            st.markdown("""This model is a GPT-2 model that is fine-tuned on the OpenAI community dataset. 
                     It is used to extract features from a given text.""")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="Today is a sunny day and I will get some ice cream.")
        extract_button_clicked = st.button("Extract",key='fe')
        if extract_button_clicked:
            output=self.feature_extraction_api(text)
            if output is not None:
                st.write(output)
        else:
            st.write("Click the button to extract features")