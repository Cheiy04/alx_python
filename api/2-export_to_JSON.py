'''importing required libs'''
import json
import requests
from sys import argv


def task_to_json(user_id):
    # Variables
    userDict = {}

    url = "https://jsonplaceholder.typicode.com"

    '''Get requests from both endpoints'''
    user_response = requests.get("{}/users/{}".format(url, user_id))
    todo_response = requests.get("{}/users/{}/todos".format(url, user_id))

    '''Getting the respone in json format'''
    username = user_response.json()['username']
    todosJson = todo_response.json()

    '''Save the employee name'''
    userDict[user_id] = []

    '''Creating for loop to iterate the tasks and save'''
    for task in todosJson:
        taskDict = {}
        taskDict['task'] = task['title']
        taskDict['username'] = username
        taskDict['completed'] = task['completed']

        userDict[user_id].append(taskDict)

    '''Creating a csv file to store user info'''
    with open("{}.json".format(user_id), "w") as jsonFile:
        json.dump(userDict, jsonFile)

'''Exextuing if this is the main script'''
if __name__ == "__main__":
    task_to_json(argv[1])