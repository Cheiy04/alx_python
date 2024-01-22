'''Importing Flask class from the flask module'''
from flask import Flask

'''Creating an instance of the Flask class'''
app = Flask(__name__)

'''Setting a URL route to execute our function and defining a function that prints an output'''
@app.route("/")
#function
def hello():
    '''
    Function to handle requests to the root URL ("/").
    
    Returns:
        str: A simple greeting string.
    '''
    '''Returns the following string'''
    return "Hello HBNB!"

# Calling the hello function
print(hello())

# Running our Flask application on a server
app.run()
