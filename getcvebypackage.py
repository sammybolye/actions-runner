#!/usr/bin/env python3

import requests
from getCVSSScore import get_cvss_score
#from gettopcve import get_top_cves
from createtabindoc import create_table_in_word


# List of OpenSSL versions to retrieve CVEs for
#openssl_versions = ['1.0.2u', '1.1.0', '1.1.1k']
openssl_versions = ['1.1.0k']

# Iterate over OpenSSL versions and retrieve related CVEs
for version in openssl_versions:
    # Construct API query URL
    api_url = f'https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:2.3:a:openssl:openssl:{version}:*'
    
    
    # Send API request and retrieve JSON response
    response = requests.get(api_url)
    response_json = response.json()
    
    print(response_json)
    
    # Extract relevant CVE information from response
    cve_items = response_json['result']['CVE_Items']
    
    cve_list = []
    cve_list_slim = []

    for cve_item in cve_items:
        cve_id = cve_item['cve']['CVE_data_meta']['ID']
        cve_description = cve_item['cve']['description']['description_data'][0]['value']
        cve_distro = cve_item['cve']
        
        #cve_impactV3 = cve_item['impact']['baseMetricV3']['cvssV3']['baseScore']
        #cve_impactV2 = cve_item['impact']['baseMetricV2']['cvssV2']['baseScore']

        cvssv2_score, cvssv2_severitiy  = get_cvss_score(cve_id, "V2")
        cvssv3_score, cvssv3_severitiy  = get_cvss_score(cve_id, "V3")       
       
        cve_list.append((cve_id, cve_description, cvssv3_score, cvssv2_score, cvssv3_severitiy))
        cve_list_slim.append((cve_id, cvssv2_score,cvssv2_score,cvssv2_severitiy,version))
        

        
        #print(f" The V2 score of {cve_id} is {cvssv2_score} {cvssv2_severitiy}")
        #print(f" The V3 score of {cve_id} is {cvssv3_score} {cvssv3_severitiy}")
    
    #Print CVEs for the current OpenSSL version
    #print(f'\nCVEs for OpenSSL version {version}:\n--------------------------------')
    for cve_id, cve_description, cvssv3_score, cvssv2_score, cvssv3_severitiy in cve_list:
        pass
        #print(f'{cve_id} | {cvssv2_score} | {cvssv3_score} | {cvssv3_severitiy}' )
        #print(f'{cve_id} | {cvssv2_score} | {cvssv3_score} | {cvssv3_severitiy} | {cve_description}' )
    print(cve_list_slim)
    #res = get_top_cves(cve_list_slim)
    #print(res)
    #create_table_in_word(res)