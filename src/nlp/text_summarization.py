import requests
import streamlit as st
class TextSummarization:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    def text_summarization_api(self,text:str)->str:
        """
        Performs text summarization API call using the given text input.
        
        Parameters:
            text (str): The input text to be summarized.
        
        Returns:
            str: The summarized text.
        """
        
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
            return output[0]['summary_text']
        
        except requests.ConnectionError as e:
            st.error("Connection error")
        except requests.ConnectTimeout as e:
            st.error("Connection timeout")
        except requests.RequestException as e:
            st.error("Request exception")
        except requests.HTTPError as e:
            st.error("HTTP error")
        except KeyError as e:
            st.warning("Could not generate.")
        except (Exception, ValueError) as e:
            st.error("Unknown error")
    def text_summarization(self):
        """
        A function that handles the text summarization process by interacting with the 'text_summarization_api' method based on user input text. 
        It displays the model description, takes user input, triggers the summarization process on button click, and shows the summarized text or a warning message.
        """
        st.subheader("Text Summarization")
        with st.expander("Model Description"):  
            st.markdown("""This model is a T5 model (Falconsai/text_summarization) that is fine-tuned on the CNN/DailyMail dataset. 
                     It is used to summarize the long text input provided by the user.""")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="""The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris.""")
        done=False if len(text)>1 else True
        summarize_button_clicked = st.button("Summarize",disabled=done)
            
        if summarize_button_clicked:
            output=self.text_summarization_api(text)
            if len(output)>0:
                st.info(output)
            else:
                st.warning("Sorry I was unable to summarize your text")
        else:
            st.write("Click the button to summarize text.")
                