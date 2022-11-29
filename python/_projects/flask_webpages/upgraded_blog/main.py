# main.py
# ----
# Updated: cramos 28/nov/2022
#
# Improved version of flask based Blog page
#    [ Based on TheLondonApp : 100DaysOfCode ]
#
# Notes:
#   Requires the installation of Flask library
#     python -m pip install flask

#   Running the app, (Windows CMD):
#       Option A.
#          set FLASK_APP=main.py
#          python -m flask run
#       Option B.
#          python main.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def blog_main():
    return render_template("index.htm")

if __name__ == "__main__":
	app.run(debug=True, host="localhost", port="5000")
