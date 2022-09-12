#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Trivial script to test Python requests.
"""

import sys
import requests


def main(site):
    """
    Performs a GET request on the supplied website.
    """

    # Issue HTTP GET request, check for success, and print body
    resp = requests.get(site)

    # If not "ok", raise HTTPError, otherwise do nothing
    # Code: ~/environments/pyreq/lib/python3.6/site-packages/requests/models.py
    resp.raise_for_status()
    print(resp.text)


if __name__ == "__main__":

    # Ensure there are at least 2 arguments; extract the
    # second one (first one after the script name)
    if len(sys.argv) >= 2:
        main(sys.argv[1])

    # Insufficient CLI args supplied; use author's homepage by default
    else:
        main("http://njrusmc.net")
