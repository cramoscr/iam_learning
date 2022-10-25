# main.py
# ----
# Updated: cramos 18/oct/2022
#
# Personal portfolio web page
#    [ Based on TheLondonApp : 100DaysOfCode ]
#
# Notes:
#   Requires the installation of Flask library
#     python -m pip install flask

#   For running the app, (Windows CMD):
#       Option A.
#          set FLASK_APP=main.py
#          python -m flask run
#       Option B.
#          python my_portfolio.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.htm")

if __name__ == "__main__":
	app.run(debug=True)
