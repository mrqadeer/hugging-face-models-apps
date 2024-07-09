# Hugging Face Model Showcase - A Gold Mine

Welcome to the Hugging Face Model Showcase app! This app demonstrates the power and versatility of Hugging Face models across multiple domains, including NLP, Audio, Computer Vision and Multimodal. The app utilizes models offering serverless APIs for seamless responses.
## Deployment
### On Streamlit Cloud
Check it out [Hugging Face Models Apps](https://hugging-face-models-apps-qrtn5wius38afgfqghjats.streamlit.app/)
### On Render
Check it out [Hugging Face Models Apps](https://hugging-face-models-apps.onrender.com/)
## Table of Contents

- [Hugging Face Model Showcase - A Gold Mine](https://huggingface.co)
  - [Deployments](#deployment)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Features](#features)
    - [Audio](#audio)
    - [Computer Vision](#computer-vision)
    - [Multimodal](#multimodal)
    - [NLP](#nlp)
  - [Getting Your Hugging Face Access Token](#getting-your-hugging-face-access-token)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. Clone the repository:
   Open your terminal and run command

   ```
   git clone https://github.com/mrqadeer/hugging-face-models-apps.git
   ```
2. Go to the project folder
   ```bash 
   cd hugging-face-models-apps
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv huggingface
   ```
   Activate on Windows
   ```bash
   huggingface\Scripts\activate
   ```
   Activate on Linux/Mac
   ```bash
   source huggingface/bin/activate
   ```
4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:

   ```
   streamlit run app.py
   ```
2. If your streamlit app doesn't open in your web browser then go to ```http://localhost:8501``` 
to access the app.
3. Provide Hugging Face Access Token (API Key) to get your access key follow the link [https://huggingface.co/settings/tokens]()
4. Navigate through different categories (Audio, Computer Vision, Multimodal and NLP) to explore the capabilities of various Hugging Face models.

## Features

### Audio

* **Audio Classification** : Classify audio files into predefined categories
* **Automatic Speech Recognition (ASR)** : Convert speech to text
* **Denoise Audio** : Remove noise from audio recordings
* **Text to Audio** : Generate instrumental audio from text
* **Text to Speech (TTS)** : Convert text into spoken words

### Computer Vision

* **Image Classification** : Categorize images into predefined labels
* **Image to Text** : Generate descriptive text from images
* **Object Detection** : Identify and locate objects within images
* **Text to Image** : Generate images from textual descriptions

### Multimodal

* **Document Q/A** : Answer questions based on the content of documents

### NLP

* **Fill Mask** : Predict the missing word in a sentence
* **Named Entity Recognition (NER)** : Identify entities in text (e.g., names, places, organization)
* **Sentence Similarity** : Measure the similarity between sentences
* **Sentiment Analysis** : Determine the sentiment of text
* **Table Question Answering** : Answer questions based on table data
* **Text Generation** : Generate text based on a given prompt
* **Text Summarization** : Summarize long pieces of text
* **Translation** : Translate text from one language to another at time app entertains only 9 languages
* **Zero-shot Classification** : Classify text into categories without specific training

## Getting Your Hugging Face Access Token

1. Sign up or log in to your Hugging Face account at [Hugging Face](https://huggingface.co/).
2. Go to your account settings and create a new access token.
3. Copy the token and paste it into the app when prompted.

## Contributing

We welcome contributions! Please read [Contribution](CONTRIBUTE.md) file for more detail.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.