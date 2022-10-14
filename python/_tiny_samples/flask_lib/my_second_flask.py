# my_second_flask.py
# ---------------
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

#   Using flask with debug mode on
#      + allows automatic reloading
#      + activates the debugger

# Sample 2
#    Using URL variables and decorators

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Helloooooo, World!'

@app.route("/bye")
def bye_bye():
    return 'GoodBye Yellow Brick road !'

@app.route("/<myname>")
def greeting(myname):
    return f'Welcome {myname + 12} !'

@app.route("/tags")
def html_tags():
    return '<h1 style="text-align: center"> This is a html tag! </h1>' \
    '<p>This is a paragraph.</p>'


print(f'This is the value of __name__: {__name__}')

if __name__ == "__main__":
    app.run(debug=True)
