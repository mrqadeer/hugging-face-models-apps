# Import necessary libraries
import requests
import streamlit as st
import pandas as pd

# Define the class
class TableQuestionAnswer:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    
    # Define the method to perform question answering on a table
    def table_question_answering_api(self,text:str, table):
        """
        Performs question answering on a table using the TAPAS model.
        
        Parameters:
            text (str): The query text to be answered.
            table: The table data to query.
        
        Returns:
            The output of the question answering process.
        """
        # Getting the access token from the session state
        Access_Token = st.session_state.access_token
        try:
            # Specify the Hugging Face model API URL
            API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
            # Specify the header for the API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Define the query function to send the post request (text) to the API
            def query(payload):
                # Send the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Return the response in JSON format
                return response.json()
            # Call the query function with the table and question as the arguments
            output = query({"inputs": {"query": text, "table": table}})
            return output

        # Handling exceptions
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
     
    # Define the method to handle the table question answering process        
    def table_question_answering(self):
        """
        Performs question answering on a table using the TAPAS model.
        
        Returns:
            The output of the question answering process.
        """
        # Adding subheader to the streamlit app
        st.subheader("Table Answer Question")
        # Adding expander to describe the model
        with st.expander("Model Description"):
            st.markdown("""This model is a TAPAS model (google/tapas-base-finetuned-wtq) that is fine-tuned on the WikiTableQuestions dataset. 
                     It is used to answer questions asked on a provided table. Currently this model only supports CSV files.""")
        st.divider()
        done=False
        
        # Adding expander to upload the data
        with st.expander("Upload Data"):
            # Uploading the CSV file
            data=st.file_uploader("Upload CSV file",type='csv')
            # Checking if the data is uploaded
            if data is not None:
                # Read the csv file into dataframe
                data=pd.read_csv(data)
                # Convert all the columns to string type
                for col in data:
                    data[col]=data[col].astype(str)
                # Display the dataframe
                st.dataframe(data)
                # Convert the dataframe to dictionary
                table=data.to_dict(orient='list')
                done=True
        # Disable the text area if the data is not uploaded
        text_disabled = not done
        # Adding text area for user to enter query
        text=st.text_area("Enter your query", placeholder=
                                                        "Tell me about data")
            
        # Adding button to extract the information    
        extract_button_clicked = st.button("Extract",disabled=text_disabled)
        # Checking if the Extract button is clicked
        if extract_button_clicked:
            # Call function to perform question answering on the table 
            output=self.table_question_answering_api(text,table)
            # Checking if the output is returned
            if output is not None:
                try:
                    if len(output)>0:
                        # Display the output
                        st.info(output['cells'][0])
                except Exception as e:
                    
                    st.error("I could not understand your text")
        else:
            st.write("Please upload CSV file and enter query to extract the information from the table")
            