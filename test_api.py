import json
import requests

headers = {
    'Content-Type':'application/json'
}

data = {
    'name':'Obama'
}

resp = requests.post('http://localhost:8000/api/hello_view', 
                    data = json.dumps(data), 
                    headers=headers)

print(resp.text)
