# import the necessary libraries
import requests
import streamlit as st

# Define the class
class ZeroShotClassification:
    def __init__(self) -> None:
        """
        Initializes the ZeroShotClassification object with no parameters and returns None.
        """
        pass
    # Define the method to perform zero-shot classification
    def zero_shot_classification_api(self,text,labels:list):
        """
        Executes zero-shot classification on the input text with a list of candidate labels.
        
        Parameters:
            self: The object instance.
            text: The input text to classify.
            labels: A list of candidate labels for classification.
        
        Returns:
            The output of the zero-shot classification.
        """
        # Gettting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
            # Specify the header for the API request
            headers = {"Authorization": f"Bearer {Access_Token}"}
            # Define the query function to send the post request (text) to the API
            def query(payload):
                # Send the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Return the response in JSON format
                return response.json()
            # Call the query function with the text as the argument
            output = query({ "inputs": text, "parameters": {"candidate_labels": labels},})
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
    # Define the method to perform zero-shot classification
    def zero_shot_classification(self):
        # Adding subheader to the streamlit app
        st.subheader("Zero Shot Classification")
        # Adding an expander to describe the model
        with st.expander("Model Description"):
            st.write("""This model is a BART model (facebook/bart-large-mnli) that is fine-tuned on the MNLI dataset. 
                     It is used to classify a given text into a set of labels. Provide a text and labels to classify.""")
        st.divider()
        # Adding text area for user to provide text input
        text=st.text_area("Enter your Text", 
                              placeholder="Dune is the best movie ever",
                              )
        # Adding text area for user to enter lables 
        labels=st.text_area("Enter your labels separated by comma",
                                    placeholder="CINEMA, ART, MUSIC",
                                    )
        # Checking if the text and labels are not empty
        if not (len(labels)>1 and len(text)>1):
            # Enabling the button
            button_action=True
        else:
            # Disabling the button
            button_action=False
        # Creating a button to perform zero-shot classification
        zc_button_clicked = st.button("Zero-Shot",disabled=button_action)
        # Checking if the Zero-Shot button is clicked
        if zc_button_clicked:
            # Call the zero_shot_classification_api function with the text and labels as the arguments
            # The lables are split by comma to create a list
            output = self.zero_shot_classification_api(text,labels.split(","))
            # Checking if the output is not empty
            if output is not None:
                # Sorting the labels and scores in descending order
                zipped=sorted(zip(output['labels'],output['scores']),key=lambda x:x[1],reverse=True)
                # Getting the sequence from the output
                sequence=output['sequence']
                # Displaying the sequence and the best suited label
                st.info(sequence)
                # Label with the highest score
                st.info(f"Best suited label: {zipped[0][0]}")
            else:
                st.warning("Sorry I was unable to classify your text")
        else:
            st.write("Click the button for zero-shot classification.")