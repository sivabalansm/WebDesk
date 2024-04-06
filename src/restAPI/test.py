#! /bin/python3

import requests

BASE = "http://127.0.0.1:5000/"

user_id = 0
response = requests.put(BASE + "rest/" + str(user_id), {"name": "Cyrus", "machine_type": "Linux"})
print(response.json())
response = requests.get(BASE + "rest/" + str(user_id))
print(response.json())
response = requests.patch(BASE + "rest/" + str(user_id))
print(response.json())
response = requests.delete(BASE + "rest/" + str(user_id))
print(response)
