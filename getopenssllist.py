#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# URL to the RHEL Package Database search page
url = "https://access.redhat.com/packages"

# Query parameters to search for OpenSSL packages for RHEL
params = {
    "name": "openssl",
    "product": "Red Hat Enterprise Linux",
    "search_text": "",
    "repository": "",
    "architecture": "",
    "show": "all",
    "showAdvanced": False,
    "sort": "package",
    "type": "package",
    "version": "",
    "channel": "",
    "errata": "",
    "is_visible": "1"
}

# Send a GET request to the RHEL Package Database search page
response = requests.get(url, params=params)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table that contains the package versions
table = soup.find("table", class_="table table-striped table-hover table-bordered")

if table is None:
    # Print the HTML response to help diagnose the issue
    print(response.content)
    print("Unable to find table element")
else:
    # Extract the package versions from the table
    versions = []
    for row in table.tbody.find_all("tr"):
        cols = row.find_all("td")
        version = cols[1].a.string
        versions.append(version)

    # Print the list of OpenSSL versions
    print(versions)

