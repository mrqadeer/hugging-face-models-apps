import requests
import streamlit as st
import base64

class DocumentQuaestionAnswering:
    
    def __init__(self) -> None:
        pass
    
    def document_question_answering_api(text, image):
        Access_Token = st.session_state.access_token
        
        try:
            API_URL = "https://api-inference.huggingface.co/models/impira/layoutlm-document-qa"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                with open(payload["image"], "rb") as f:
                    img = f.read()
                    payload["image"] = base64.b64encode(img).decode("utf-8")  
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({"inputs": image,
                    "question": text})
            
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
        
    def document_question_answering(self):
        st.subheader("Document Question Answering")
        with st.expander("Model Description"):
            st.markdown("""This model is a Document Question Answering model (impira/layoutlm-document-qa) that is used to 
                            extract the answer from the tabular data in the provided document. The model accepts an image to extract the text and then answer the question.""")
        st.divider()
        image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
        st.divider()
        url=st.text_input("Enter Image URL")
        if image is not None or url is not None:
            text = st.text_area("Enter your querry", placeholder="")
            process_button_clicked = st.button("Process")
            
            if process_button_clicked: 
                qa_output=self.document_question_answering_api(text, image)
                # qa_output=document_question_answering(text, url)
                for item in qa_output:
                    st.write(f"{item['answer']} : {item['score']:.2%}")