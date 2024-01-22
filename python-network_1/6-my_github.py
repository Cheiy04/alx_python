# Python script that takes your GitHub credentials 
# (username and password) and uses the GitHub API to display your id

'''Importing the requests and sys'''
import sys
import requests

'''Variables to take the username and password'''
user_name = input("Enter your username: ") if len(sys.argv) < 2 else sys.argv[1]
password = input("Enter your password: ") if len(sys.argv) < 3 else sys.argv[2]

'''Variable to take in the github api'''

git_api = "https://api.github.com/user"

'''Getting the id from the username and password'''
response = requests.get(url=git_api, auth=(user_name, password))

'''Checking for succesful response'''
if response.status_code == 200:
    if response.json()['login'] == user_name:
        user_id = response.json()['id']
        print("Your id is {}".format(user_id))
    else:
        print("Could not find this user")
else:
    print("Error in getting a response")

# print(response.json())