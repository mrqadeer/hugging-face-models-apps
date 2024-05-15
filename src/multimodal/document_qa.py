import requests
import streamlit as st
import base64

def document_question_answering(text, image):
    Access_Token = st.session_state.access_token
    
    try:
        # API_URL = "https://api-inference.huggingface.co/models/naver-clova-ix/donut-base-finetuned-docvqa"
        API_URL = "https://api-inference.huggingface.co/models/impira/layoutlm-document-qa"
        headers = {"Authorization": f"Bearer {Access_Token}"}

        def query(payload):
            with open(payload["inputs"]["image"], "rb") as f:
                img = f.read()
                payload["inputs"]["image"] = base64.b64encode(img).decode("utf-8")
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": {
                "image": image,
                "question": text
            },
        })
        
        return output
    except requests.ConnectionError as e:
        st.error("Connection error")
    except requests.ConnectTimeout as e:
        st.error("Connection timeout")
    except requests.RequestException as e:
        st.error("Request exception")
    # except (Exception, ValueError) as e:
    #     st.error("Unknown error")
    except requests.HTTPError as e:
        st.error("HTTP error")