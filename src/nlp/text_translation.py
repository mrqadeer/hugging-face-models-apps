from itertools import permutations
import requests
import streamlit as st 
# @st.cache_resource
class TextTranslation:
    def __init__(self) -> None:
        
        self.all_languages={
                'Chinese': ['English', 'Russian', 'German', 'Spanish', 'French'],
            'French': ['English', 'Russian', 'German', 'Spanish', 'Chinese'],
            'Spanish': ['English', 'Russian', 'German', 'French', 'Chinese'],
            'German': ['English', 'Russian', 'Spanish', 'French', 'Chinese'],
            'Russian': ['English', 'German', 'Spanish', 'French', 'Chinese'],
            'English': ['Chinese', 'French', 'Spanish', 'German', 'Russian'],
        }
        # self.all_languages={perm[0]: [key] + list(perm[1:]) for key, v in self.languages.items() for perm in permutations(v)}
        # self.all_languages.update(self.languages)
        self.zh_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en"
    def text_translation_api(self,text,API_URL):
        Access_Token = st.session_state.access_token
        
        try:
            # API_URL = "https://api-inference.huggingface.co/models/google-t5/t5-small"
            # API_URL = "https://api-inference.huggingface.co/models/google-t5/t5-base"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                 
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": text
            })
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
    # @st.cache(suppress_st_warning=True)  # Cache the API response
    def text_translation(self):
        translated=""
        st.subheader("Translation")
        st.divider()
    
        cols=st.columns([4,2,4])
        sorted_languages=sorted(self.all_languages.keys(),reverse=False)
        with cols[0]:
            source_language=st.selectbox("Select a language",sorted_languages,key='sr')
            if source_language in self.all_languages:
                output_language_list=self.all_languages[source_language]
            text=st.text_area("Enter your Text", placeholder="Type your text...")
            
        with cols[1]:
            pass
        with cols[2]:
            output_language=st.selectbox("Select a language",output_language_list,key='ol')
        
            
        if source_language=='Chinese' and output_language=='English':
            translated_text=self.text_translation_api(text,self.zh_en_api)
                
                
        done=False if len(text)>1  else True
        translate_button_clicked = st.button("Translate",disabled=done)
        
        if translate_button_clicked:
            translated=translated_text[0]['translation_text']
                
        else:
            st.write("Please type your text to translate.")
        with cols[2]:
            translated_text_holder=st.text_area("Translated Text",key='translated1',
                                                value=translated)
    