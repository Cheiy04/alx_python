'''Importing requests and sys'''
import sys
import requests




url = input("Enter URL") if len(sys.argv) < 2 else sys.argv[1]

response = requests.get(url=url)
value = response.headers['X-Request-Id']

if 'X-Request-Id' in value:
    print(value)