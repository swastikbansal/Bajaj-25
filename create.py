import requests

url = 'https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON'
payload = {
    "name": "Swastik Bansal" ,
    "regNo": "REG1030" ,
    "email": "swastikbansal220461@acropolis.in"
}

ans = requests.post(url, json=payload)

if ans.status_code == 200:
    print(ans.text)
