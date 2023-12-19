'''Importing requests and sys'''
import requests
import sys

url =  sys.argv[1]

response = requests.get(url)
# value = response['X-Request-Id="School"']

# print(response.status_code)