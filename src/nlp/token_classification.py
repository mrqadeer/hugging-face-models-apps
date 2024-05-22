# Import necessary libraries
import requests
import streamlit as st

# Define the class
class TokenClassification:
    def __init__(self) -> None:
        """
        Initializes the TokenClassification object with no parameters and returns None.
        """
        pass
    
    # Define the method for token classification
    def token_classification_api(self,text:str):
        """
        Method to interact with the Hugging Face model API for token classification.

        Parameters:
            text (str): The input text to classify tokens.

        Returns:
            dict: The classification results for the input text.
        """
        # Get the access token from the session state
        Access_Token = st.session_state.access_token
        
        try: 
            # Specify the Hugging Face model API URL   
            API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
            # Specify the header for the API request
            headers = {"Authorization": f"Bearer {Access_Token}"}
            # Define the query function to send the post request (text) to the API
            def query(payload):
                # Send the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Return the response in JSON format
                return response.json()

            # wrap the text input in a list
            output = query({"inputs": [text]})
            # return the results
            results = output[0]
            return results
        
        # Handling exceptions    
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
    
    # Define the method to perform token classification
    def token_classification(self):
        """
        Function to perform Name Entity Recognition.

        Parameters:
            text (str): The input text to classify tokens.

        Returns:
            dict: The classification results for the input text.
        """
        # Adding subheader to the streamlit app
        st.subheader("Name Entity Recognition")
        # Adding expander for model description
        with st.expander("Model Description"):
            st.markdown("""This model is a BERT model (dslim/bert-base-NER) that is fine-tuned on the CoNLL-2003 dataset. 
                     It is used to identify the entities in a given text. The entities can be a person name, location name, company name or any other entity.""")
        st.divider()
        # Adding text area for user input
        text=st.text_area("Enter your Text", placeholder="My name is Sarah Jessica Parker but you can call me Jessica")
        done=True
        # Check if the text is not empty
        done=False if len(text)>1 else True
        
        # Create a button to trigger the identification process
        identify_button_clicked = st.button("Identify",disabled=done)
        # Check if the button is clicked
        if identify_button_clicked:
            # Call the token_classification_api method with the text as the argument
            output=self.token_classification_api(text)
            # Check if the output 
            if output is not None:
                # Check if the output is not empty
                if len(output)>0:
                    # Loop through the output to check the entity group and setting the entity type
                    for item in output:
                        if item['entity_group'] == 'PER':
                            entity_type = 'Person name'
                        elif item['entity_group'] == 'LOC':
                            entity_type = 'Location Name'
                        elif item['entity_group'] == 'ORG':
                            entity_type = 'Company Name'
                        else:
                            entity_type = 'Unknown Entity'
                        # Display the entity type and the word with the score
                        st.info(f"{entity_type}: {item['word'] } with score: {item['score']:.2%}")
            else:
                st.warning("Sorry I was unable to recognize your text")
        else:
            st.write("Click the button to identify the entities in your text")