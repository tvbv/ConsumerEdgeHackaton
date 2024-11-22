import requests
import json

def generate_text(model_name, system_content, user_content, temperature=0.7, max_tokens=-1):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [
            { "role": "system", "content": system_content },
            { "role": "user", "content": user_content }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False 
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Failed to get a response from the server."
