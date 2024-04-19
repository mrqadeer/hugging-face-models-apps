import requests
import streamlit as st
class ZeroShotClassification:
    def __init__(self) -> None:
        pass
    def zero_shot_classification_api(text,labels:list):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
                "parameters": {"candidate_labels": labels},
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
    def zero_shot_classification(self):
        
        st.subheader("")
        st.divider()
        
        text=st.text_area("Enter your Text", 
                              placeholder="I have a problem with my iphone that needs to be resolved asap",
                              )
            
        labels=st.text_area("Enter your labels separated by comma",
                                    placeholder="urgent ,not urgent,phone, tablet, computer",
                                    )
        if not (len(labels)>1 and len(text)>1):
            button_action=True
        else:
            button_action=False
        zc_button_clicked = st.button("Zero-Shot",disabled=button_action)
        if zc_button_clicked:
            output = self.zero_shot_classification_api(text,labels.split(","))
            if output is not None:
                zipped=sorted(zip(output['labels'],output['scores']),key=lambda x:x[1],reverse=True)
                sequence=output['sequence']
                st.info(sequence)
                st.info(f"Best suited label: {zipped[0][0]}")
            else:
                st.warning("Sorry I was unable to classify your text")
        else:
            st.write("Click the button for zero-shot classification.")