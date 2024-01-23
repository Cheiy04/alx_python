'''Importing Flask class from the flask module'''
from flask import Flask

app = Flask(__name__)


@app.route("/")
#function
def hello():

    return "Hello HBNB!"

print(hello())

app.run()
