import requests
import streamlit as st
class SentenceSimilarity:
    def __init__(self) -> None:
        pass
    def sentence_similarity_api(self,source_sentence, list_of_sentences):
        Access_Token = st.session_state.access_token
        try:            
            API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": {
                    "source_sentence": source_sentence,
                    "sentences": list_of_sentences
                },
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
    def sentence_similarity(self):
        st.subheader("Sentence Similarity")
        with st.expander("Model Description"):
            st.write("""This model is a MiniLM model (sentence-transformers/all-MiniLM-L6-v2) that is fine-tuned on the STS Benchmark dataset. 
                     It is used to find the similarity between two sentences. Provide a source sentence and a list of sentences to compare.""")
        st.divider()
        source_text=st.text_area("Enter your Text", placeholder="")
        st.divider()
        sentences=st.text_area(r"Enter Sentences to compare. Use '|' for more than one sentences").split("|")
        done=False if len(source_text)>1 and len(sentences)>0 else True
        find_button_clicked = st.button("Find Similarity",disabled=done)
        if find_button_clicked:
            output=self.sentence_similarity_api(source_text,sentences)
            for i,j in zip(sentences,output):
                st.info(f"{i.strip()} is {j:.2%} similar to {source_text}")
        else:
            st.write("Please provide text and sentences for comparision to find similarity.")