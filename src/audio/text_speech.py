# import necessary libraries
import streamlit as st
import requests

# Defining the class
class TextSpeech:
    def __init__(self) -> None:
        """
        Initializing the object of the class with no parameters and returns None.
        """
        pass
    
    # Defining the method to convert text to speech
    def text_to_speech_api(self,text):
        """
        Function to convert text to speech using the Hugging Face API.

        Parameters:
            text (str): The text to convert to speech.

        Returns:
            audio_bytes (bytes): The output audio bytes.
        """
        
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            #Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/speechbrain/mtl-mimic-voicebank"
            # Specify the headers for API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Defining the query function to send the post request (text) to the API
            def query(payload):
                # Sending the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Returning the response content
                return response.content
            # Calling the query function with the text as the argument
            audio_bytes = query({"inputs": text})

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
    
    # Defining the method to convert text to speech
    def text_to_speech(self):
        # Adding a subheader to the streamlit app
        st.subheader("Text to Speech")
        # Adding an expander to describe the model
        with st.expander("Model Description"):
            st.markdown("""This model is a TTS model (facebook/mms-tts-eng) that is used to convert text into speech. 
                                Provide a text to convert into speech. You can also download the output audio.""")
        st.divider()
        text = st.text_area("Enter your Text", placeholder="The universe is vast and mysterious and holds countless wonders waiting to be discovered")
        # Creating a button to get the converted speech
        speak_button_clicked = st.button("Get Speech")
        # Checking if the button is clicked
        if speak_button_clicked:
            # Calling the text_to_speech_api method with the text as the argument
            audio_output=self.text_to_speech_api(text)
            # Decoding output file
            temp=audio_output.decode()
            
            # Checking if the output is not an error
            if not 'error' in temp:
                # Displaying the audio output
                st.audio(audio_output)
                # Creating a download button to download the audio output
                st.download_button(label="Download Audio", data=audio_output, file_name="audio_output.mp3", mime="audio/flac")
            else:
                # Warning message if the output is an error
                st.warning("Try again...")
        else:
            st.write("Click the button to convert your text into speech")  