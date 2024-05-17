import requests
import streamlit as st


class SentimentAnalysis:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    def sentiment_analysis_api(self,text:str):
        """
        Function to analyze the sentiment of the input text using the Hugging Face model API.
        
        Parameters:
            text (str): The input text to analyze.
            
        Returns:
            dict: The sentiment analysis output in JSON format.
        """
        Access_Token = st.session_state.access_token
        
        
        try:
            API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": text,
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
    def sentiment_analysis(self):
        """
        Perform sentiment analysis on the input text using a RoBERTa model fine-tuned on the Twitter dataset.
        
        Parameters:
        - self: the object instance
        - text: the input text for sentiment analysis
        
        Returns:
        - None
        """
        st.subheader("Sentiment Analysis")
        with st.expander("Model Description"):
            st.markdown("""This model is a RoBERTa model (cardiffnlp/twitter-roberta-base-sentiment) that is fine-tuned on the Twitter dataset. 
                     It is used to find the sentiment of a given text if it is "Positive", "Negative" or "Neutral".""")
        st.divider()

        text=st.text_area("Enter your Text", placeholder="Universe is full of wonders.")
        done=True
        done=False if len(text)>1 else True
        
        analyse_button_clicked = st.button("Analyze",disabled=done)
        if analyse_button_clicked:
            output=self.sentiment_analysis_api(text)
            if len(output)>0:
                output=output[0][0]['label'].title()
                if output.startswith('N'):
                    st.warning(output)
                else:
                    st.success(output)
            else:
                st.warning("Please try again...")