import requests
import streamlit as st
import base64
import pathlib
from PIL import Image 
from io import BytesIO
curr_path=pathlib.Path(__file__)
root_dir=curr_path.parent.parent.parent
class DocumentQuaestionAnswering:
    
    def __init__(self) -> None:
        """
        Initializes the object of the class. 
        No parameters are taken, and the function returns None.
        """
        pass
    
    def document_question_answering_api(self,text:str, image):
        """
        This function handles the document question answering API. It takes in the text and image as parameters and returns the output after querying the Hugging Face model API.
        """
        
        Access_Token = st.session_state.access_token
        
        try:
            API_URL = "https://api-inference.huggingface.co/models/impira/layoutlm-document-qa"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(payload):
                with open(payload['inputs']['image'], "rb") as f:
                    img = f.read()
                    payload['inputs']['image'] = base64.b64encode(img).decode("utf-8")  
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs": {
		    "image": image,
		"question": text
	    }
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
        
    def document_question_answering(self):
        """
        This function handles the document question answering. It interacts with the Streamlit library to prompt the user to upload an image, enter a query, and process the query using the 'document_question_answering_api' method. It displays the answer and its corresponding score.
        """
        st.subheader("Document Question Answering")
        with st.expander("Model Description"):
            st.markdown("""This model is a Document Question Answering model (impira/layoutlm-document-qa) that is used to 
                            extract the answer from the tabular data in the provided document. The model accepts an image to extract the text and then answer the question.""")
        st.divider()
        
        st.divider()
        path=root_dir / 'data'
        pathlib.Path.mkdir(path,exist_ok=True)
        with st.expander("Upload Image"):
            image = st.file_uploader(type=[".png", ".jpeg", ".jpg"], label="Upload Image")
            if image is not None:
                st.image(image)
            
        with st.expander("Enter Image URL"):
            url=st.text_input("Enter image URL")
            if len(url)>=1:
            
                image_data=self.image_downlaod(url)
                if image_data is not None:
                    st.image(Image.open(BytesIO(image_data)))
                    image_path=path/'image.png'
                    
                    with open(image_path,'wb') as f:
                        f.write(image_data)
            
           
        process_button = st.button("Process")
        if process_button:
            if image is not None:
                
                image_name=path/image.name
                with open(image_name,'wb') as f:
                    f.write(image.getbuffer())
                output=self.document_question_answering_api(image_name)
            
            elif len(url)>=1:
                
                output=self.document_question_answering_api(image_path)
            else:
                st.stop()
            try:
                for item in output:
                    st.info(f"{item['label']}: {item['score']:.2%}")
            except:
                st.info(output)
    @staticmethod
    def image_downlaod(url:str):
        """
        A function that downloads an image from a given URL using requests library.

        Parameters:
            url: The URL of the image to download.

        Returns:
            The content of the downloaded image if the download is successful, otherwise None.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            st.error("Failed to download image.")
            return None