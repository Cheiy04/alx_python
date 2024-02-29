'''Importing required libs'''
import csv
import requests
import sys
from urllib import response

'''Creating a function to export the data into the csv file'''

def export_to_CSV(user_id):
    """ The task define export to the CSV format"""

    # Variables
    allTasks = []

    url = "https://jsonplaceholder.typicode.com"

    # get requests for both endpoints
    user_response = requests.get("{}/users/{}".format(url, user_id))
    todo_response = requests.get("{}/users/{}/todos".format(url, user_id))

    # Get the json from responses
    name = user_response.json()['username']
    todosJson = todo_response.json()

    # Save the employee Name -- Loop the tasks and save
    for task in todosJson:
        taskRow = []
        taskRow.append(user_id)
        taskRow.append(name)
        taskRow.append(task['completed'])
        taskRow.append(task['title'])
        allTasks.append(taskRow)
    '''Creating a csv file and giving it the user information'''
    with open("{}.csv".format(user_id), "w") as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvWriter.writerows(allTasks)

    return 0


if __name__ == '__main__':
    export_to_CSV(int(sys.argv[1]))

