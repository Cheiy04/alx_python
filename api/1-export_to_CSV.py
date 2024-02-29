'''Importing required libs'''
import csv
import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response_employee = requests.get(employee_url)
    employee_data = response_employee.json()

    # Get employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    # Create CSV file
    csv_file_path = f'{employee_id}.csv'
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write tasks
        for task in todo_list:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_data['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


if __name__ == '__main__':
   get_employee_info(int(sys.argv[1]))

