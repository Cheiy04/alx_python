# Write a Python script that takes in a letter and sends
# a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

'''Import requests and sys packages'''

import requests
import sys

'''Variable to store our url and letter'''
url = sys.argv[1]
q = "" if len(sys.argv) < 2 else sys.argv[2]

'''data to be sent to our url'''
data_to_send = {
    'q': q
}

'''Post to the url'''
response = requests.post(url=url, data=data_to_send)

try:
    check_json = response.json()
    if not check_json:
        print("No result")
    else:
        id = check_json.get("id")
        name = check_json.get("name")
        print(f"[{id}] {name}")
except ValueError:
    print("Not a valid JSON")