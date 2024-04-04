import requests
import streamlit as st

def table_answer_question(query, table):
    Access_Token = "" # Add your access token here
    try:        
        API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
        headers = {"Authorization": f"Bearer {Access_Token}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": {
                "query": "How many stars does the transformers repository have?",
                "table": {
                    "Repository": ["Transformers", "Datasets", "Tokenizers"],
                    "Stars": ["36542", "4512", "3934"],
                    "Contributors": ["651", "77", "34"],
                    "Programming language": [
                        "Python",
                        "Python",
                        "Rust, Python and NodeJS"
                    ]
                }
            },
        })
    
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
    else:
        return output