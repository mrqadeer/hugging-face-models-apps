from itertools import permutations
import requests
import streamlit as st 
# @st.cache_resource
class TextTranslation:
    def __init__(self) -> None:
        
        self.all_languages={
            
            'Chinese': ['English', 'German','Swedish'],
            'French': ['English', 'Russian', 'German', 'Spanish'],
            'Spanish': ['English', 'Russian', 'German', 'French','Swedish'],
            'German': ['English', 'Spanish', 'French', 'Chinese'],
            'Russian': ['English', 'Spanish', 'French'],
            'English': ['Chinese', 'French', 'Spanish', 'German', 'Russian',"Swedish",'Arabic','Italian'],
            'Swedish': ['English', 'Russian', 'German', 'Spanish', 'French'],
            'Arabic':['English','French','Spanish','German','Russian'],
            'Italian':['English']
            
        }
        # self.all_languages={perm[0]: [key] + list(perm[1:]) for key, v in self.languages.items() for perm in permutations(v)}
        # self.all_languages.update(self.languages)
        self.zh_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en"
        self.en_zh_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-zh"
        self.en_es_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-es"
        self.es_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-en"
        self.de_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-de-en"
        self.en_de_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-de"
        self.fr_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-en"
        self.en_fr_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr"
        self.ru_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ru-en"
        self.en_ru_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ru"
        self.sv_en_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-sv-en"
        self.en_sv_api="https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-sv"
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
                
        if source_language=='English' and output_language=='Chinese':
            translated_text=self.text_translation_api(text,self.en_zh_api)
        if source_language=='English' and output_language=='Spanish':
            translated_text=self.text_translation_api(text,self.en_es_api)
        if source_language=='Spanish' and output_language=='English':
            translated_text=self.text_translation_api(text,self.es_en_api)
            
        if source_language=='German' and output_language=='English':
            translated_text=self.text_translation_api(text,self.de_en_api)
        if source_language=='English' and output_language=='German':
            translated_text=self.text_translation_api(text,self.en_de_api)
        if source_language=='French' and output_language=='English':
            translated_text=self.text_translation_api(text,self.fr_en_api)
        if source_language=='English' and output_language=='French':
            translated_text=self.text_translation_api(text,self.en_fr_api)
        if source_language=='Russian' and output_language=='English':
            translated_text=self.text_translation_api(text,self.ru_en_api)
        if source_language=='English' and output_language=='Russian':
            translated_text=self.text_translation_api(text,self.en_ru_api)
        done=False if len(text)>1  else True
        # translate_button_clicked = st.button("Translate",disabled=done)
        
        # if translate_button_clicked:
        #     translated=translated_text[0]['translation_text']
                
        # else:
        #     st.write("Please type your text to translate.")
        # with cols[0]:
        #     translated_text_holder=st.text_area("Translated Text",key='translated',
        #                                         value=translated)
        # cols=st.columns([4,2,4])
        # with cols[1]:
        #     pass
        done=False if len(text)>1  else True
        translate_button_clicked = st.button("Translate",disabled=done)
        
        if translate_button_clicked:
            if len(translated_text)>0:
                
                translated=translated_text[0]['translation_text']
            else:
                st.write("Please try again.")
        else:
            st.write("Please type your text to translate.")
        with cols[2]:
            translated_text_holder=st.text_area("Translated Text",key='translated1',
                                                value=translated)
    