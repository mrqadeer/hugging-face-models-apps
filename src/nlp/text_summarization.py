import requests
import streamlit as st
class TextSummarization:
    def __init__(self) -> None:
        pass
    def text_summarization_api(self,text):
        
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
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
    def text_summarization(self):
        st.subheader("Text Summarization")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="""The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris.""")
        done=False if len(text)>1 else True
        summarize_button_clicked = st.button("Summarize",disabled=done)
            
        if summarize_button_clicked:
            output=self.text_summarization_api(text)
            if output is not None:
                st.info(output[0]['summary_text'])
            else:
                st.warning("Sorry I was unable to summarize your text")
        else:
            st.write("Click the button to summarize text.")
                