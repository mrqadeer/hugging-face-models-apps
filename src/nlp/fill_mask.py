# Import necessary libraries
import requests
import streamlit as st

# Define the class
class FillMask:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    
    # Define the method to fill the mask using the Hugging Face model API
    def fill_mask_api(self,text):
        """
        Fills the mask in the given text using the DistilBERT model.
        
        Parameters:
            text (str): The text with a mask to be filled.
            
        Returns:
            dict: The output of filling the mask.
        """
        # Get the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            # API_URL = "https://api-inference.huggingface.co/models/google-bert/bert-base-uncased"
            API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased"
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
        except requests.HTTPError as e:
            st.error("HTTP error")
        except KeyError as e:
            st.warning("Could not generate.")
        except (Exception, ValueError) as e:
            st.error("Unknown error")
            
    # Define the method to fill the mask
    def fill_mask(self):
        """
        A function that handles filling the mask based on user input text using the fill_mask_api method.
        
        """
        # Adding subheader to the streamlit app
        st.subheader("Fill Mask")
        # Adding expander for model description
        with st.expander("Model Description"):
            st.markdown("""This model is a BERT model (google-bert/bert-base-uncased) that is fine-tuned on the Google dataset. 
                     It is used to fill the mask in a given text. Provide a text with a " - " inplace of word to be MASK.""")
        st.divider()
        # Adding text area for user input
        text=st.text_area("Enter your Text", placeholder="For filling mask put - inplace of word.")
        # Replacing "-" in the user input text with "[MASK]"
        text=text.replace("-", "[MASK]")
        
        # Creating a button to make a predict missing word
        mask_button_clicked = st.button("FillMask")
        # Checking if the FillMask button is clicked
        if mask_button_clicked:
            # Call the fill_mask_api function with the text as the argument
            output=self.fill_mask_api(text)
            # Checking if the output is not None
            if output is not None:
                # Display the output
                st.write(output)   
        else:
            st.write("Click the button to make a prediction.")