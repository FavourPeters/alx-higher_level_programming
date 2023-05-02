#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: <class 'str'>".format(type(r.text)))
    print("\t- content: Custom status".format(r.text))
