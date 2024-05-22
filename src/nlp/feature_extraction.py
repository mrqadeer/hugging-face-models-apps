# import the necessary libraries
import requests
import streamlit as st

# Define the class
class FeatureExtraction:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    
    # Define the method to extract features using the Hugging Face model API
    def feature_extraction_api(self,text):
        """
        This function performs feature extraction using the Hugging Face GPT-2 model.
        
        Args:
            text (str): The input text for feature extraction.
            
        Returns:
            dict: The extracted features based on the input text.
        """
        # Get the access token from the session state
        Access_Token = st.session_state.access_token
        
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
            # Specify the header for the API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Define the query function to send the post request (text) to the API
            def query(payload):
                # Send the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Return the response in JSON format
                return response.json()
            
            # Call the query function with the text as the argument
            output = query({
                "inputs": text,
            })
            return output
        
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
            
    # Define the method to handle the feature extraction process
    def feature_extraction(self):
        """
        A function that handles the feature extraction process. It prompts the user to enter text, extracts features using the 'feature_extraction_api' function, 
        and displays the extracted features if available. 
        """
        # Adding subheader to the streamlit app
        st.subheader("Feature Extraction")
        # Adding expander for model description
        with st.expander("Model Description"):
            st.markdown("""This model is a GPT-2 model that is fine-tuned on the OpenAI community dataset. 
                     It is used to extract features from a given text.""")
        st.divider()
        text=st.text_area("Enter your Text", placeholder="Today is a sunny day and I will get some ice cream.")
        
        # Adding a button to extract features
        extract_button_clicked = st.button("Extract",key='fe')
        # Checking if the Extract button is clicked
        if extract_button_clicked:
            # Call the feature_extraction_api function with the text as the argument
            output=self.feature_extraction_api(text)
            # Checking if the output is not None
            if output is not None:
                # Display the extracted features
                st.write(output)
        else:
            st.write("Click the button to extract features")