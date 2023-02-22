#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup

def get_cvss_score(cve_id, version):
    # Define the URL for the NVD website
    url = f"https://nvd.nist.gov/vuln/detail/{cve_id}"

    if version == 'V2':
        search_tag = "a#Cvss2CalculatorAnchor"
    elif version == 'V3':
        search_tag = "a#Cvss3NistCalculatorAnchor"    

    # Make a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the CVSSv3 score and severity
        cvss_element = soup.select_one(search_tag)
        if cvss_element:
            cvss_score = cvss_element.text.strip().split()[0]
            cvss_severity = cvss_element.text.strip().split()[1]
        else:
            cvss_score = 0
            cvss_severity = 0

        # Return the results
        return cvss_score, cvss_severity
    else:
        # Return None if the request was not successful
        return 0, 0

#Example usage
# cve_id = "CVE-2019-1543"
# cvssv2_score, cvssv2_severity = get_cvss_score(cve_id, 'V2')
# cvssv3_score, cvssv3_severity = get_cvss_score(cve_id, 'V3')
# print(f"CVSSv2 score for {cve_id}: {cvssv2_score} ({cvssv2_severity})")
# print(f"CVSSv3 score for {cve_id}: {cvssv3_score} ({cvssv3_severity})")
