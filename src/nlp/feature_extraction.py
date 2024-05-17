import requests
import streamlit as st
class FeatureExtraction:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    def feature_extraction_api(self,text):
        """
        This function performs feature extraction using the Hugging Face GPT-2 model.
        
        Args:
            text (str): The input text for feature extraction.
            
        Returns:
            dict: The extracted features based on the input text.
        """
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
        """
        A function that handles the feature extraction process. It prompts the user to enter text, extracts features using the 'feature_extraction_api' function, 
        and displays the extracted features if available. 
        """
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