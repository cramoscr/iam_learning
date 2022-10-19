# main.py
# ----
# Updated: cramos 18/oct/2022
#
# Based on TheLondonApp : 100DaysOfCode
#
# Notes:
#   Requires the installation of Flask library
#     python -m pip install flask

#   For running the minimal app, (Windows CMD):
#      set FLASK_APP=main.py
#      python -m flask run

#   After the first run, you can run it again using
#      python main.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
