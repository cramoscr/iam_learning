# main.py
# ----
# Updated: cramos 26/oct/2022
#
# Produces a BLOG web page, using FLASK and consuming data from
# public API
#

# [ Notes: ]
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
def home_page():
    return render_template("index.htm")

@app.route("/blog")
def blog_page():
	blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
	api_response = requests.get(blog_api)
	all_posts = api_response.json()

	return render_template("blog_page.htm", pBlog_posts=all_posts)

if __name__ == "__main__":
	app.run(debug=True)
