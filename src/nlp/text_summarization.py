# Import necessary libraries
import requests
import streamlit as st

# Define the class
class TextSummarization:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    
    # Define the method to perform text summarization using the Hugging Face model API
    def text_summarization_api(self,text:str)->str:
        """
        Performs text summarization API call using the given text input.
        
        Parameters:
            text (str): The input text to be summarized.
        
        Returns:
            text (str): The summarized text.
        """
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
            # Specify the header for the API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Define the query function to send the post request (text) to the API
            def query(payload):
                # Send the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Return the response in JSON format
                return response.json()
            # Call the query function with the text as the argument
            output = query({"inputs": text,})
            # Return the summarized text
            return output[0]['summary_text']
        
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
            
    # Define the method to perform text summarization
    def text_summarization(self):
        """
        A function that handles the text summarization process by interacting with the 'text_summarization_api' method based on user input text. 
        It displays the model description, takes user input, triggers the summarization process on button click, and shows the summarized text or a warning message.
        """
        # Add a subheader to the streamlit app
        st.subheader("Text Summarization")
        # Adding expander for model description
        with st.expander("Model Description"):  
            st.markdown("""This model is a T5 model (Falconsai/text_summarization) that is fine-tuned on the CNN/DailyMail dataset. 
                     It is used to summarize the long text input provided by the user.""")
        st.divider()
        # Allow user to enter the text
        text=st.text_area("Enter your Text", placeholder="""The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris.""")
        # Disable the button if the text area is empty
        done=False if len(text)>1 else True
        # Display the summarize button
        summarize_button_clicked = st.button("Summarize",disabled=done)
        # Check if the button is clicked
        if summarize_button_clicked:
            # Call the text_summarization_api method with the text as the argument
            output=self.text_summarization_api(text)
            # Checking if the output is not empty
            if len(output)>0:
                # Display the summarized text
                st.info(output)
            else:
                st.warning("Sorry I was unable to summarize your text")
        else:
            st.write("Click the button to summarize text.")
                