# Import necessary libraries
import requests
import streamlit as st

# Define the class
class SentimentAnalysis:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    
    # Define the method to analyze the sentiment of the text
    def sentiment_analysis_api(self,text:str):
        """
        Function to analyze the sentiment of the input text using the Hugging Face model API.
        
        Parameters:
            text (str): The input text to analyze.
            
        Returns:
            dict: The sentiment analysis output in JSON format.
        """
        # Get the access token from the session state
        Access_Token = st.session_state.access_token
        
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
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
            # Return the first label from the output (from first index of the list)
            return output[0][0]['label'].title()
            
        # Handling exceptions
        except requests.ConnectionError as e:
            st.error("Connection error")
        except requests.ConnectTimeout as e:
            st.error("Connection timeout")
        except requests.RequestException as e:
            st.error("Request exception")
        except KeyError as e:
            st.warning("Please Try again...")
        except requests.HTTPError as e:
            st.error("HTTP error")
        except (Exception, ValueError) as e:
            st.error("Unknown error")
      
    # Defining method to perform sentiment analysis  
    def sentiment_analysis(self):
        """
        Perform sentiment analysis on the input text using a RoBERTa model fine-tuned on the Twitter dataset.
        
        Parameters:
        - self: the object instance
        - text: the input text for sentiment analysis
        
        Returns:
            label: the sentiment label (Positive, Negative, or Neutral)
        """
        # Adding subheader to the streamlit app
        st.subheader("Sentiment Analysis")
        # Adding expander for model description
        with st.expander("Model Description"):
            st.markdown("""This model is a RoBERTa model (cardiffnlp/twitter-roberta-base-sentiment) that is fine-tuned on the Twitter dataset. 
                     It is used to find the sentiment of a given text if it is "Positive", "Negative" or "Neutral".""")
        st.divider()
        # Adding text area for user input
        text=st.text_area("Enter your Text", placeholder="Universe is full of wonders.")
        
        done=True
        done=False if len(text)>1 else True
        
        # Adding button to analyze the text
        analyse_button_clicked = st.button("Analyze",disabled=done)
        # Checking if the button is clicked
        if analyse_button_clicked:
            try:
                # Call the sentiment_analysis_api function with the text as the argument
                output=self.sentiment_analysis_api(text)

                # Checking the output and displaying the result if start with 'N'
                if output.startswith('N'):
                    # Display the output with warning message
                    st.warning(output)
                else:
                    # Display the output with results
                    st.success(output)
            # If no text recieved from the API
            except Exception as e:
                st.error("Something went wrong...")
        else:
            st.warning("Analyze the text")