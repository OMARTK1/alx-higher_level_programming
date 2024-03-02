#!/usr/bin/python3
"""
This Script uses the GitHub API to display the user id
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)

    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
