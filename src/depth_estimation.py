import requests
from PIL import Image
import streamlit as st
from transformers import pipeline

def depth_estimator(image):
    try:
        pipe = pipeline(task="depth-estimation", model="Intel/dpt-large")

        image_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'  # Example image
        image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
        result = pipe(image)
        output = result["depth"].save("depth_map.jpg")
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