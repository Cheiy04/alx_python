'''Importing required libs'''
from urllib import response
import requests
import sys
'''Getting the url'''
url = "https://jsonplaceholder.typicode.com/users"
user_id = sys.argv[1]
endpoint1 = url + "/{}".format(user_id)
endpoint2 = url + "/{}".format(user_id) + '/todos'

response1 = requests.get(url=endpoint1 )
response2 = requests.get(url=endpoint2 )

data1 = response1.json()
data2 = response2.json()

name = data1['name']

total_tasks = len(data2)
completed = [task['title'] for task in data2 if task['completed']]
completed_tasks = len(completed)


print(f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):")
for i in completed:
    print(f"\t{i}")


