'''Importing requests and sys'''
import requests
import sys

url =  input("Enter URL:") if len(sys.argv) < 2 else sys.argv[1]

response = requests.get(url)
# value = response['X-Request-Id="School"']

# print(response.status_code)