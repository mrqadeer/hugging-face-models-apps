import requests
import streamlit as st
import pandas as pd
class TableQuestionAnswer:
    def __init__(self) -> None:
        pass
    def table_question_answering_api(self,text, table):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
            headers = {"Authorization": f"Bearer {Access_Token}"}

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
            
    def table_question_answering(self):
        st.subheader("Table Answer Question")
        st.divider()
        done=False
        with st.expander("Upload Data"):
            data=st.file_uploader("Upload CSV file",type='csv')
            if data is not None:
                data=pd.read_csv(data)
                for col in data:
                    data[col]=data[col].astype(str)
                st.dataframe(data)
                table=data.to_dict(orient='list')
                done=True
        text_disabled = not done
        text=st.text_area("Enter your query", placeholder=
                                                        "Tell me about data")
            
            
        extract_button_clicked = st.button("Extract",disabled=text_disabled)
        if extract_button_clicked:
            output=self.table_question_answering_api(text,table)
            if output is not None:
                try:
                    if len(output)>0:
                            
                        st.info(output['cells'][0])
                except Exception as e:
                    st.error("I could not understand your text")
        else:
            st.write("Please upload CSV file and enter query to extract the information from the table")
            