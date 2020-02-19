
import requests
import json

"""
This function builds an interface with github repo
"""
def github_api():
    """Gathering data from Github and representing it in printed statement"""

    # Get the github ID
    git_id = "iamikenna"
    commit_list, output = [], []  
    resp = requests.get(f"https://api.github.com/users/{git_id}/repos") #Github API key for getting data on repo
    resp_new = json.loads(resp.text)
    output.append(f"User: {git_id}")

    try:
        resp_new[0] ['name']
    except (TypeError, KeyError, IndexError):
        return 'unable to fetch repos from user'

    try:
        for todo_item in resp_new:
            me = todo_item['name']
            resp2 = requests.get(f"https://api.github.com/repos/{git_id}/{me}/commits") #Github API key for getting data on commits
            repo_info = json.loads(resp2.text)
            output.append((f"Repo: {me} Number of commits: "))
    except (TypeError, KeyError, IndexError):
        return 'unable to fetch commits from repo'
    return output



if __name__ == '__main__':
    for entry in github_api():
        print(entry)



