# import necessary libraries
import requests
import streamlit as st

# Defining the class
class TextAudio:
    def __init__(self) -> None:
        """
        Initializing the object of the class with no parameters and returns None.
        """
        pass
    
    # Defining the method to convert text to audio
    def text_to_audio_api(text):
        """
        Funvtion to convert text to audio using the Hugging Face API.
        
        Parameters:
            text (str): The text prompt to convert to audio.

        Returns:
            audio_bytes (bytes): The output audio bytes.
        """
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
            # Specify the headers for API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Defining the query function to send the post request (text) to the API
            def query(payload):
                # Sending the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Returning the response content
                return response.content
            # Calling the query function with the text as the argument
            audio_bytes = query({
                "inputs": text,
            })
            # You can access the audio with IPython.display for example
            # from IPython.display import Audio
            return audio_bytes
        
        # Handling the exceptions
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

    # Defining the method to convert text to audio
    def text_to_audio(self):
        # Adding a subheader to the streamlit app
        st.subheader("Text to Audio")
        # Adding an expander to describe the model
        with st.expander("Model Description"):
            st.markdown("""This model is a TTS model (facebook/musicgen-small) that is used to convert text into audio. 
                                Provide a text to convert into instrumental audio file. You can also download the output audio file.""")
        st.divider()
        # Adding a text area to get the text input
        text = st.text_area("Enter your Text", placeholder="liquid drum and bass, atmospheric synths, airy sounds")
        # Adding a button to get the audio output from the model
        audio_button_clicked = st.button("Get Audio")
        # Checking if the button is clicked
        if audio_button_clicked:
            # Calling the text_to_audio_api method with the text as the argument
            text_to_audio_output=self.text_to_audio_api(text)
            # Displaying the audio output
            st.audio(text_to_audio_output)
            # Creating a download button to download the audio output
            st.download_button(label="Download Audio", data=text_to_audio_output, file_name="audio_output.mp3", mime="audio/flac")  