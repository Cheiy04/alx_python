# Write a Python script that takes in a URL and an email address,
# sends a POST request to the passed URL with the email as a parameter, 
# and finally displays the body of the response.

'''Importing the requests package and the sys'''
import sys
import requests

'''Variables to Store a URL and an email address'''
url = sys.argv[1]
email = sys.argv[2]
data = {
    'email':email
}

'''Sending a post request to the url with the email'''
respone = requests.post(url=url, data=data)
print(respone.text)
