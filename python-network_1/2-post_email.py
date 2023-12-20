# Write a Python script that takes in a URL and an email address,
# sends a POST request to the passed URL with the email as a parameter, 
# and finally displays the body of the response.

'''Importing the requests package and the sys'''
import sys
import requests

'''Variables to Store a URL and an email address'''
url_to_use = input("Enter URL: ") if len(sys.argv) < 2 else sys.argv[1]
email = input("Enter Email: ") if len(sys.argv) < 3 else sys.argv[2]
data_to_be_sent = {
    'email':email
}

'''Sending a post request to the url with the email'''
response = requests.post(url=url_to_use, data=data_to_be_sent)
print(response.text)
