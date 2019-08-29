import requests

fetch_url = "http://wyre.pythonanywhere.com/load_readings/"

print(requests.get(fetch_url).json())