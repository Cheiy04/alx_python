'''import flask server'''
from flask import Flask
'''Creating an instance of the class'''
app = Flask(__name__)

'''routing to designated url'''
@app.route("/",strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"

'''routing to /hbnb'''
@app.route("/hbnb")
def HBNB():
    return "HBNB"

'''routing to /c'''
@app.route("/c/<text>")
def C_fun(text):
    '''In the text the underscore should be replaced by a space'''
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

'''Routing to both instances where a text is present and if not it defaults to a given value'''
@app.route("/python/<text>")
@app.route("/python/")
def python_fun(text='is cool'):
    '''In the text the underscore should be replaced by a space'''
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

'''Routing to /number '''
@app.route("/python/<int:n>")
def number(n):
    return f"{n} is a number"


'''runs if it is the main script and not while imported'''
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)