import requests
import streamlit as st

def table_question_answering(text, table):
    Access_Token = "" # Add your access token here
    try:
        API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({"inputs": {"query": text, "table": table}})
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