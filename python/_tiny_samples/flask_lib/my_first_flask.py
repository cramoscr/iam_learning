# my_first_flask.py
# --------------
# Updated: cramos 10/oct/2022
#
# Based on TheLondonApp : 100DaysOfCode
#
# Notes:
#   Requires the installation of Flask library
#     python -m pip install flask
#   For running the minimal app, (Windows CMD):
#      set FLASK_APP=my_first_flask.py
#      python -m flask run

# Sample 1
#    This is the minimun code for running a web page using Flask library

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye_bye():
    return 'GoodBye Yellow Brick road !'
