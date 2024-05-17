import requests
import streamlit as st

class TokenClassification:
    def __init__(self) -> None:
        """
        Initializes the TokenClassification object with no parameters and returns None.
        """
        pass
    def token_classification_api(self,text:str):
        """
        Method to interact with the Hugging Face model API for token classification.

        Parameters:
            text (str): The input text to classify tokens.

        Returns:
            dict: The classification results for the input text.
        """

        Access_Token = st.session_state.access_token
        
        try:    
            API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            # wrap the text input in a list
            output = query({"inputs": [text]})
            
            results = output[0]
            return results
            
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
    def token_classification(self):
        """
        Function to perform Name Entity Recognition.

        Parameters:
            None

        Returns:
            None
        """
        st.subheader("Name Entity Recognition")
        with st.expander("Model Description"):
            st.markdown("""This model is a BERT model (dslim/bert-base-NER) that is fine-tuned on the CoNLL-2003 dataset. 
                     It is used to identify the entities in a given text. The entities can be a person name, location name, company name or any other entity.""")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="My name is Sarah Jessica Parker but you can call me Jessica")
        done=True
        done=False if len(text)>1 else True
        identify_button_clicked = st.button("Identify",disabled=done)
        if identify_button_clicked:
            output=self.token_classification_api(text)
            if output is not None:
                if len(output)>0:
                    for item in output:
                        if item['entity_group'] == 'PER':
                            entity_type = 'Person name'
                        elif item['entity_group'] == 'LOC':
                            entity_type = 'Location Name'
                        elif item['entity_group'] == 'ORG':
                            entity_type = 'Company Name'
                        else:
                            entity_type = 'Unknown Entity'

                        st.info(f"{entity_type}: {item['word'] } with score: {item['score']:.2%}")
            else:
                st.warning("Sorry I was unable to recognize your text")
        else:
            st.write("Click the button to identify the entities in your text")