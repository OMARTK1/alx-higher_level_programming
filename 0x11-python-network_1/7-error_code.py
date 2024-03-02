#!/usr/bin/python3
"""
This Script takes in a URL, sends a request to the URL, and displays the body
of the response. If the HTTP status code is greater than or equal to 400,
prints the HTTP status code
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
