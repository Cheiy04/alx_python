'''Import request '''
import requests

'''Takes the url and request it using the get method'''

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(url)))
print("\t- content: {}".format(response))




