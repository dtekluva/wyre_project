import requests

fetch_url = "http://localhost:8000/load_readings/"

try:
    response = requests.get(fetch_url)
    print(response.json())

except:
    print("Error: Site might be down")