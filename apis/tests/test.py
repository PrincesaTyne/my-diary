import requests, json

response = requests.get("/entries")
print (json.dumps(response.json(), indent=4))
