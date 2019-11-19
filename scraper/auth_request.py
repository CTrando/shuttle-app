import os
import sys
import requests

API_KEY = os.environ.get("API_KEY")
SHUTTLE_URL = os.environ.get("SHUTTLE_URL")
if API_KEY is None or SHUTTLE_URL is None:
    sys.exit("Environment variables not set, did you set up direnv?")


def auth_get(url, params=None):
    if params is None:
        params = {}
    headers = {"Accept": "application/json", "Api-Key": API_KEY}
    return requests.get(url, params=params, headers=headers)
