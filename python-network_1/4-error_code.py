# Write a Python script that takes in a URL, 
# sends a request to the URL and displays the body of the response.

'''Importig the requests and system packages'''
import requests
import sys

'''Variable to take in the url'''
url = sys.argv[1]

'''Sending a request to the url and also checking for errors'''
response = requests.get(url=url)
if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print(response.text)
