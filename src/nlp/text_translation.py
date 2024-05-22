# Import necessary libraries
from itertools import permutations
import requests
import streamlit as st 

# @st.cache_resource
# Define the Class
class TextTranslation:
    def __init__(self) -> None:
        """
        Initializes the TextTranslation object with a dictionary of languages and their 
        corresponding translations, as well as APIs for various language translation models.
        """
        # Define a dictionary of languages and their corresponding translations
        self.all_languages={
            
            'Chinese': ['English', 'German','Swedish'],
            'French': ['English', 'Arabic', 'Russian', 'German', 'Spanish', 'Swedish'],
            'Spanish': ['English', 'Russian', 'German', 'French','Arabic'],
            'German': ['English', 'Spanish', 'French', 'Chinese','Arabic'],
            'Russian': ['English', 'Spanish', 'French','Swedish','Arabic'],
            'English': ['Chinese', 'French', 'Spanish', 'German', 'Russian',"Swedish",'Arabic','Italian'],
            'Swedish': ['English', 'Russian', 'French', 'Chinese'],
            'Arabic':['English','French','Spanish','German','Russian'],
            'Italian':['English']            
        }
        
        # APIs of each model for each language
        self.zh_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en"
        self.zh_sv_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-sv"
        self.zh_de_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-de"
        self.fr_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-en"
        self.fr_ar_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-ar"
        self.fr_es_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-es"
        self.fr_de_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-de"
        self.fr_ru_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-ru"
        self.fr_sv_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-sv"
        self.es_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-en"
        self.es_ru_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-ru"
        self.es_de_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-de"
        self.es_fr_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-fr"
        self.es_ar_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-ar"
        self.de_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-de-en"
        self.de_fr_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-de-fr"
        self.de_es_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-de-es"
        self.de_zh_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-de-ZH"
        self.de_ar_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-de-ar"
        self.ru_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ru-en"
        self.ru_es_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ru-es"
        self.ru_ar_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ru-ar"
        self.ru_fr_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ru-fr"
        self.ru_sv_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ru-sv"
        self.en_zh_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-zh"
        self.en_es_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-es"
        self.en_de_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-de"
        self.en_fr_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr"
        self.en_sv_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-sv"
        self.en_ru_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ru"
        self.en_ar_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ar"
        self.en_it_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-it"
        self.sv_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-sv-en"
        self.sv_ru_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-sv-ru"
        self.sv_fr_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-sv-fr"
        self.sv_zh_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-sv-ZH"
        self.it_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-it-en"
        self.ar_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ar-en"
        self.ar_fr_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ar-fr"
        self.ar_es_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ar-es"
        self.ar_de_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ar-de"
        self.ar_ru_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ar-ru"
        
    # Define the method to translate text
    def text_translation_api(self,text:str,API_URL:str)->str:
        """
        This function is used to translate text from one language to another using the Hugging Face model API.
        
        Parameters:
            text (str): This function accepts text as input to translate in other languages.
            API_URL (str): This function will get model api url of hugging face as input.

        Returns:
            str: This function return translated text.
        """
        # Get the access token from the session state
        Access_Token = st.session_state.access_token
        try:
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
                "inputs": text
            })
            # Return the translated text
            return output[0]['translation_text']
        
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
            st.warning("Please Try Again!")
        except (Exception, ValueError) as e:
            st.error("Unknown error")
            
    # @st.cache(suppress_st_warning=True)  # Cache the API response
    # Define the method to perform text translation
    def text_translation(self)->None:
        """
        The function to perform text translation using the Hugging Face model API for all specified languages
        Args:
            No arguments accepted. Just do the translations.
        Return:
            No return value. Just do the translations.
        """
        # Adding subheader to the streamlit app
        st.subheader("Translation")
        # Adding a expander for the model description
        with st.expander("Model Description"):
            st.markdown("""This model is a translation model (Helsinki-NLP/opus-mt) that is fine-tuned on the OpenAI community dataset. 
                     It is used to translate text from one language to another. This model supports translation of nine languages including English, Chinese, Germen, Swedish,
                     French, Spanish, Russian, Arabic and Italian.""")
        st.divider()
        # Define the columns for the streamlit app
        cols=st.columns([4,2,4])
        # sort list of languages in alphabetical order
        sorted_languages=sorted(self.all_languages.keys(),reverse=False)
        # Create a column layout for the source and output languages
        with cols[0]:
            # Create dropdown for user to select source language
            source_language=st.selectbox("Select a language",sorted_languages,key='sr')
            
            # Check if the source language is in the list of all languages
            if source_language in self.all_languages:
                # Get the output languages list based on the source language
                output_language_list=self.all_languages[source_language]
            # Create text area for user to enter text to be translated
            text=st.text_area("Enter your Text", placeholder="Type your text...")
        
        # Create a column layout for the second column 
        with cols[1]:
            pass
        # Create a column layout for the output language
        with cols[2]:
            # Create dropdown for user to select output language
            output_language=st.selectbox("Select a language",sorted(output_language_list),key='ol')
        
        # Define a dictionary to map language pairs to API endpoints
        language_map = {
        ('Chinese', 'English'): self.zh_en_api,
        ('Chinese', 'Swedish'): self.zh_sv_api,
        ('Chinese', 'German'): self.zh_de_api,
        ('English', 'Chinese'): self.en_zh_api,
        ('English', 'Spanish'): self.en_es_api,
        ('English', 'German'): self.en_de_api,
        ('English', 'French'): self.en_fr_api,
        ('English', 'Russian'): self.en_ru_api,
        ('English', 'Swedish'): self.en_sv_api,
        ('English', 'Arabic'): self.en_ar_api,
        ('English', 'Italian'): self.en_it_api,
        ('Spanish', 'English'): self.es_en_api,
        ('Spanish', 'Russian'): self.es_ru_api,
        ('Spanish', 'German'): self.es_de_api,
        ('Spanish', 'French'): self.es_fr_api,
        ('Spanish', 'Arabic'): self.es_ar_api,
        ('German', 'English'): self.de_en_api,
        ('German', 'Spanish'): self.de_es_api,
        ('German', 'French'): self.de_fr_api,
        ('German', 'Chinese'): self.de_zh_api,
        ('German', 'Arabic'): self.de_ar_api,
        ('French', 'English'): self.fr_en_api,
        ('French', 'Arabic'): self.fr_ar_api,
        ('French', 'Spanish'): self.fr_es_api,
        ('French', 'German'): self.fr_de_api,
        ('French', 'Russian'): self.fr_ru_api,
        ('French', 'Swedish'): self.fr_sv_api,
        ('Russian', 'English'): self.ru_en_api,
        ('Russian', 'Spanish'): self.ru_es_api,
        ('Russian', 'French'): self.ru_fr_api,
        ('Russian', 'Swedish'): self.ru_sv_api,
        ('Russian', 'Arabic'): self.ru_ar_api,
        ('Swedish', 'English'): self.sv_en_api,
        ('Swedish', 'Russian'): self.sv_ru_api,
        ('Swedish', 'French'): self.sv_fr_api,
        ('Swedish', 'Chinese'): self.sv_zh_api,
        ('Arabic', 'English'): self.ar_en_api,
        ('Arabic', 'French'): self.ar_fr_api,
        ('Arabic', 'Spanish'): self.ar_es_api,
        ('Arabic', 'German'): self.ar_de_api,
        ('Arabic', 'Russian'): self.ar_ru_api,
        ('Italian', 'English'): self.it_en_api,
    }

        # Check if the selected language pair is in the language map
        if (source_language, output_language) in language_map:
        
            # to disable and enable button
            done=False if len(text)>=1  else True

            # Create a button to translate the text
            translate_button = st.button("Translate",disabled=done)
            
            # Check if the Translate button is clicked
            if translate_button:
                # calling the function to hit api of model
                translated_text = self.text_translation_api(text, language_map[(source_language, output_language)])
                
                # Check if the translated text is not None
                if translated_text is not None:
                    with cols[2]:
                        # Display the translated text in a text area
                        translated_text_holder=st.text_area("Translated Text",key='translated1',
                                                    value=translated_text)
            #If the translation button is not clicked    
            else:
                # Display a message to the user
                st.write("If you don't get translation then press Translate button again and again.")
        else:
            # If the language pair is not supported, display a message
            st.write("Translation not supported for this language pair.")
