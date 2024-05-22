# Import necessary libraries
import requests
import streamlit as st

# Define the class
class SentenceSimilarity:
    def __init__(self) -> None:
        """
        Initializes the object of the class with no parameters and returns None.
        """
        pass
    
    # Defining method to check similarity between sentences 
    def sentence_similarity_api(self,source_sentence:str, list_of_sentences:list):
        """
        Function to query the Hugging Face API for sentence similarity based on a source sentence and a list of sentences.
        
        Parameters:
            source_sentence (str): The source sentence for which similarity is to be calculated.
            list_of_sentences (list): A list of sentences to compare against the source sentence.
        
        Returns:
            JSON: The JSON response containing the similarity scores between the source sentence and each sentence in the list.
        """
        # Getting acess token from session state
        Access_Token = st.session_state.access_token
        try:   
            # Specify the Hugging Face model API URL         
            API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
            # Specify the header for the API request
            headers = {"Authorization": f"Bearer {Access_Token}"}

            # Defining the query function to send the post request (text) to the API
            def query(payload):
                # Send the post request to the API
                response = requests.post(API_URL, headers=headers, json=payload)
                # Return the response in JSON format
                return response.json()

            # Call the query function with the text as the argument
            output = query({
                "inputs": {
                    "source_sentence": source_sentence,
                    "sentences": list_of_sentences
                },
            })
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
            
    # Defining the method to check similarity between sentences
    def sentence_similarity(self):
        """
        A function that handles the sentence similarity process. It prompts the user to enter a source sentence and a list of sentences for comparison. 
        It then calls the 'sentence_similarity_api' method to find the similarity between the source sentence and each sentence in the list.
        
        Parameters:
            text (str): The input text for feature extraction.
            
        Returns:
            dict: The extracted features based on the input text.
        """
        # Adding subheader to the streamlit app
        st.subheader("Sentence Similarity")
        # Adding expander for model description
        with st.expander("Model Description"):
            st.write("""This model is a MiniLM model (sentence-transformers/all-MiniLM-L6-v2) that is fine-tuned on the STS Benchmark dataset. 
                     It is used to find the similarity between two sentences. Provide a source sentence and a list of sentences to compare.""")
        st.divider()
        # Adding text area for user input for sentence to be check for similarity
        source_text=st.text_area("Enter your Text", placeholder="I love to play soccer")
        st.divider()
        # Adding text area for user input for sentences to be compared
        sentences=st.text_area(r"Enter Sentences to compare. Use '|' for more than one sentences",
                               placeholder='I like football | I love to play cricket.').split("|")
        # Checking if the sencences are provided or not
        done=False if len(source_text)>1 and len(sentences)>0 else True
        
        # Adding a button to find the similarity
        find_button_clicked = st.button("Find Similarity",disabled=done)
        # Checking if the Find Similarity button is clicked
        if find_button_clicked:
            try:
                # Call the sentence_similarity_api function with the source text and sentences as the arguments
                output=self.sentence_similarity_api(source_text,sentences)
                # Iteterating over the sentences and similarity scores simultaneously
                for i,j in zip(sentences,output):
                    # Display info or each pair of sentence (i) and similarity score (j)
                    # The message contains the sentence and similarity score  as percentage with 2 decimal points
                    st.info(f"{i.strip()} is {j:.2%} similar to {source_text}")
            except:
                # Display error message if similarity is not found
                st.info("Sorry I was unable to find the similarity")
        else:
            # Display message if no text is provided for comparision
            st.write("Please provide text and sentences for comparision to find similarity.")