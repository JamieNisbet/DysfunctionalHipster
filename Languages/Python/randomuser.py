import requests

r = requests.get("https://randomuser.me/api/")

data = r.json()

for user in data['results']:
    print(user['name']['first'])