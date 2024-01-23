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

'''runs if it is the main script and not while imported'''
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)