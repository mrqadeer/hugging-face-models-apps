import requests
import streamlit as st
class FillMask:
    def __init__(self) -> None:
        pass
    def fill_mask_api(self,text):
        """
        Fills the mask in the given text using the DistilBERT model.
        
        Parameters:
            text (str): The text with a mask to be filled.
            
        Returns:
            dict: The output of filling the mask.
        """
        Access_Token = st.session_state.access_token
        try:
            # API_URL = "https://api-inference.huggingface.co/models/google-bert/bert-base-uncased"
            API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased"
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
        except requests.HTTPError as e:
            st.error("HTTP error")
        except KeyError as e:
            st.warning("Could not generate.")
        except (Exception, ValueError) as e:
            st.error("Unknown error")
            
        
    def fill_mask(self):
        """
        A function that handles filling the mask based on user input text using the fill_mask_api method.
        """
        st.subheader("Fill Mask")
        with st.expander("Model Description"):
            st.markdown("""This model is a BERT model (google-bert/bert-base-uncased) that is fine-tuned on the Google dataset. 
                     It is used to fill the mask in a given text. Provide a text with a " - " inplace of word to be MASK.""")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="For filling mask put - inplace of word.")
        text=text.replace("-", "[MASK]")
        
        mask_button_clicked = st.button("FillMask")
        if mask_button_clicked:
            output=self.fill_mask_api(text)
            if output is not None:
                st.write(output)
                
        else:
            st.write("Click the button to make a prediction.")