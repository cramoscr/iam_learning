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

import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.htm")

@app.route("/guess/<p_name>")
def guess(p_name):
	gender_url = f"https://api.genderize.io?name={p_name}"
	gender_response = requests.get(gender_url)
	gender_data = gender_response.json()
	v_gender = gender_data["gender"]

	age_url = f"https://api.agify.io?name={p_name}"
	age_response = requests.get(age_url)
	age_data = age_response.json()
	v_age = age_data["age"]

	return render_template("guess_age_gender.htm", person_name=p_name, gender=v_gender, age=v_age)

if __name__ == "__main__":
	app.run(debug=True)
