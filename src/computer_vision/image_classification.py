import requests
import streamlit as st

def image_classifier(image):
        Access_Token = st.session_state.access_token
        try:
            API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
            headers = {"Authorization": f"Bearer {Access_Token}"}

            def query(filename):
                with open(filename, "rb") as f:
                    data = f.read()
                # data=filename
                response = requests.post(API_URL, headers=headers, data=data)
                return response.json()

            output = query("/content/downloaded_image.jpg")
            output = output[0]
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