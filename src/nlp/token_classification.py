import requests
import streamlit as st

class TokenClassification:
    def __init__(self) -> None:
        pass
    def token_classification_api(self,text):

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
        st.subheader("Name Entity Recognition")
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