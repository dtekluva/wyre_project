import requests

fetch_url = "http://wyre.pythonanywhere.com/load_readings/"

response = requests.get(fetch_url)
print(response.json())