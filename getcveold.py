#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup
import re
from getCVSSScore import get_cvss_score
from getversionsaffected import  get_versions_between

url = 'https://www.openssl.org/news/vulnerabilities.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

cve_list = []
rows = []
for row in soup.select('#content > div > article > dl > dt'):
    col1 = row.text.strip()
    col2 = row.find_next("dd").text.strip()
    
    col3_list = row.find_next("dd").find_next("ul").find_all("li")
    
    col3 = []
    for li in col3_list:
        col3_text = li.text.strip().replace('OpenSSL', '').replace('(', ',').strip(')')
        gitstring = ",git commit) ,"
        premsupp = ",premium support) "
        
        for part in col3_text.split(','):
            if 'Fixed in' in part:
                thisfixedin = part.replace('Fixed in','').strip()
            elif 'Affected since' in part:
                thisaffectedsince = part.replace('Affected since','').strip()  
                  
            
        
        # print(f'fixed in is: {thisfixedin}')
        # print(f'affected since is: {thisaffectedsince}')
        
        # affected_versions = get_versions_between(thisaffectedsince,thisfixedin)
        # print(affected_versions) 
        col3_text = col3_text.replace(gitstring, '').replace(premsupp, "")
        col3.append(col3_text)
        #print(col3)
    #col3 = '|'.join(col3)   
    
    #print(f'{col1},{col3} ')


    cve_ref = re.search(r'CVE-(\d{4})-(\d+)', col1)
    if cve_ref:
        cve_ref = cve_ref.group()
        cve_date = col1.split()[-3] + " " + col1.split()[-2] + " " + col1.split()[-1].replace(':','').strip(' ')
        severity = re.search(r'\[(.*?)\]', col1)
        if severity:
            severity = severity.group(1)
            short_desc = col1.replace(cve_ref,'').replace(cve_date,'').replace('[' + severity + ']','').rstrip(':').strip()
        else:
            short_desc = col1.replace(cve_ref,'').replace(cve_date,'').rstrip(':').strip()
            severity = 'N/A'
    else:
        cve_ref = ""
        cve_date = ""
        severity = ""
        short_desc = col1.strip()
        
    cvssv2_score, cvssv2_severitiy  = get_cvss_score(cve_ref, "V2")
    cvssv3_score, cvssv3_severitiy  = get_cvss_score(cve_ref, "V3")      
        
    print(f'{cve_ref} |{cvssv3_severitiy} |{cvssv2_score}| {cvssv3_score}| {col3}')    
