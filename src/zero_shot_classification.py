import requests
import streamlit as st

def zero_shot_classification(text):
    Access_Token = st.session_state.access_token
    try:
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
        headers = {"Authorization": f"Bearer {Access_Token}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
            "parameters": {"candidate_labels": ["refund", "legal", "faq"]},
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
  