import requests

URL = "https://anime-facts-rest-api.herokuapp.com/api/v1"
result = requests.get(URL)
data = result.json()
print(data)
