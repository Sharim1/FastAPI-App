import requests as req
import os


def call_text_analytics_api(headers, document, endpoint):
    response = req.post(os.getenv('ENDPOINT') + endpoint, headers=headers, json=document)
    return response.json()