
import requests
import streamlit as st
class TextGeneration:
    def __init__(self) -> None:
        pass
    
    def text_generation_api(self,text):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
            # API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"
            # API_URL = "https://api-inference.huggingface.co/models/microsoft/phi-1_5"
            # API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
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
     

    def text_generation(self):
        st.subheader("Text Generation")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="Write a story about unicorns and rainbows.")
        done=False if len(text)>1 else True
        generate_button_clicked = st.button("Generate",disabled=done)
        if generate_button_clicked:
            output=self.text_generation_api(text)
            if output is not None:
                st.info(output[0]['generated_text'])
            else:
                st.warning("Sorry I was unable to generate your text")
        else:
            st.write("Click the button to generate content.")