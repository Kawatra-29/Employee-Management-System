import requests
from django.shortcuts import render
url = "http://127.0.0.1:8000/api/dashboard/"
headers = {
    "Authorization": "Token f1633fd99190402551fd2b9bd750020908a188bb"
}

response = requests.get(url, headers=headers)
print(response.request.headers)