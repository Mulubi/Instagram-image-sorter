import requests

api_url = 'https://www.instagram.com/leomessi'
response = requests.get(api_url)
print(response.status_code)

print(response.json())