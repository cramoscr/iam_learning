# github_api_sample.py
# -----------------
# updated: cramos 10/07/2023
# Inspired in Python CrashCourse book

# How to run:
#   $ python github_api_sample.py

import requests

# Make an API call and store the response
vUrl = 'https://api.github.com/search/repositories?q=language:python&sort-starts'
vHeaders = {'Accept': 'application/vnd.github.v3+json'}

vRequest = requests.get(vUrl, headers=vHeaders)

print(f"Status Code: {vRequest.status_code}")

# Store API response in a variable
vResponseDict = vRequest.json()

# Process results
print(vResponseDict.keys())

print(f"Total repositories: {vResponseDict['total_count']}")

# Explore information about the repoositories
vRepoDicts = vResponseDict['items']
print(f"Repositories returned: {len(vRepoDicts)}")

# Top Repositories returned
for repo_dict in vRepoDicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")



