'''Importing requests and sys'''
import sys
import requests



'''Taking a Url from the command line arguments using the sys'''
url = input("Enter URL") if len(sys.argv) < 2 else sys.argv[1]

'''Returning the response from the server'''
response = requests.get(url=url)

'''Checking whether the variable X-Request-ID is in the respone header'''
if 'X-Request-Id' in response.headers:
    value = response.headers['X-Request-Id']
    print(value)