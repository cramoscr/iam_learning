# main.py
# --------
# Updated: cramos 28/oct/2022
# Blog web page (based on Flask)
#   [ inspired in TheLondonApp 100DaysofCode ]

# Notes:
#   Requires the installation of Flask library
#     python -m pip install flask

#   For running the app, (Windows CMD):
#       Option A.
#          set FLASK_APP=main.py
#          python -m flask run
#       Option B.
#          python main.py
# Imports section
import requests

from flask import Flask, render_template

# Main function
app = Flask(__name__)

@app.route('/')
def home_page():
    blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
    api_response = requests.get(blog_api)
    all_posts = api_response.json()

    return render_template("index.htm", pBlog_Posts=all_posts)

@app.route("/blog_detail/<pTitle>:<pSubtitle>:<pBody>")
def blog_page(pTitle, pSubtitle, pBody):
    print(f'pTitle: {pTitle} pSubtitle: {pSubtitle}')
    return render_template("blog_detail.htm", pBlogTitle=pTitle, pBlogSubtitle=pSubtitle, pBlogBody=pBody)

if __name__ == "__main__":
    app.run(debug=True)
