'''Importing Flask class from flask module'''
from flask import Flask

'''creating an instance of the class'''
app = Flask(__name__)

'''setting a url to execute our function and a function that prints an output'''
@app.route("/")
def hello():
    return "Hello HBNB!"

print(hello())

'''Running our application on a server'''
app.run()
