# github_api_chart.py
# ----------------
# updated: cramos 10/07/2023
# Inspired in Python CrashCourse book

# How to run:
#   $ python github_api_sample.py

import requests

from plotly.graph_objs import Bar
from plotly  import offline

# Make an API call and store the response
vUrl = 'https://api.github.com/search/repositories?q=language:python&sort-starts'
vHeaders = {'Accept': 'application/vnd.github.v3+json'}

vRequest = requests.get(vUrl, headers=vHeaders)

print(f"Status Code: {vRequest.status_code}")


# Store API response in a variable
vResponseDict = vRequest.json()

# Process results
vRepoDicts = vResponseDict['items']

vRepoNames, vStars = [], []

# Top Repositories returned
for repo_dict in vRepoDicts:
    print(f"\nName: {repo_dict['name']}")
    vRepoNames.append(repo_dict['name'])
    vStars.append(repo_dict['stargazers_count'])

# Make visualizations
vData = [{
    'type': 'bar',
    'x': vRepoNames,
    'y': vStars
}]

vLayout = {
    'title': 'Most Starred Python Projects',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

vFigure = {'data': vData, 'layout': vLayout}

offline.plot(vFigure, filename='python_repos.html')

# Print results
print(f'\n Check the produced python_repos.html file...')