'''Importing requests and sys'''
import sys
import requests




url = sys.argv[1]

response = requests.get(url=url)
value = response.json()['X-Request-Id']
# value = response['X-Request-Id="School"']

print(value)