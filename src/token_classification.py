import requests

API_URL = "https://api-inference.huggingface.co/models/tsmatz/xlm-roberta-ner-japanese"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": "My name is Sarah Jessica Parker but you can call me Jessica",
})