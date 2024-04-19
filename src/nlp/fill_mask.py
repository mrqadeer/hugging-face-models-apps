import requests
import streamlit as st
class FillMask:
    def __init__(self) -> None:
        pass
    def fill_mask_api(self,text):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/google-bert/bert-base-uncased"
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
        
    def fill_masK(self):
        st.subheader("Fill Mask")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="The answer to the universe is [MASK].")
        mask_button_clicked = st.button("FillMask")
        if mask_button_clicked:
            self.fill_mask_api(text)
        else:
            st.write("Click the button to make a prediction.")