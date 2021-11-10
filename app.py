#Import Dependency
from flask import Flask

#Create new flask App Instance
app = Flask(__name__)

#Create flask route
@app.route('/')
def hello_world():
    return 'Hello World'