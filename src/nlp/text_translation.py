
import requests
import streamlit as st 
class TextTranslation:
    def __init__(self) -> None:
        pass
    def text_translation_api(self,text,target_lang):
        Access_Token = st.session_state.access_token
        
        try:
            API_URL = "https://api-inference.huggingface.co/models/google-t5/t5-small"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload,target_lang=target_lang):
                payload["translation"] = target_lang 
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": text
            },target_lang=target_lang)
            return output
        
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
    def text_translation(self):
        st.subheader("Translation")
        st.divider()
        language_codes = {
                'English': 'en',
                'French': 'fr',
                'Spanish': 'es',
                'German': 'de',
                'Urdu': 'ur',
                'Hindi': 'hi',
                # Add more languages as needed
            }


        cols=st.columns([4,2,4])
        with cols[0]:
            text=st.text_area("Enter your Text", placeholder="Меня зовут Вольфганг и я живу в Берлине")
        with cols[1]:
            st.markdown("Output Language")
            selected_language=st.selectbox("Select a language",language_codes.keys())
        with cols[2]:
                # st.markdown("Translated Text")
            translated_text=st.text_area("Translated Text", placeholder="Меня зовут Вольфганг и я живу в Берлине",key='translated')
        done=False if len(text)>1  else True
        translate_button_clicked = st.button("Translate",disabled=done)
        if translate_button_clicked:
            translated=self.text_translation_api(text,language_codes[selected_language])
            if translated is not None:
                translated_text=translated[0]['translation_text']
                st.info(translated_text)
        else:
            st.write("Click the button to translate.")
    