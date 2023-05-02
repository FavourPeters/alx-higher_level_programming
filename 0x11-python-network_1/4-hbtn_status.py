#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("http://0.0.0.0:5050/status")
    print("Body response:")
    print("\t- type: <class 'str'>".format(type(r.text)))
    print("\t- content: Custom status".format(r.text))
