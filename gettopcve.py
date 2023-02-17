def get_top_cves(cve_results):
    # Convert the string scores to floats
    cve_results = [(cve, float(base), float(exploit), severity) for cve, base, exploit, severity in cve_results]

    # Sort the results by the exploitability score in descending order
    sorted_results = sorted(cve_results, key=lambda x: x[2], reverse=True)

    # Select the top result based on the exploitability score
    top_result = max(sorted_results, key=lambda x: x[2])

    # Extract the relevant fields from the top result and create a list of all the CVE identifiers
    top_base_score = str(top_result[1])
    top_exploit_score = str(top_result[2])
    top_severity = top_result[3]
    cve_list = [result[0] for result in sorted_results]

    # Construct the output as a single tuple
    output = (top_severity, top_base_score, top_exploit_score, cve_list)


    return output



results = [('CVE-2022-1292', '10.0', '9.8', 'Critical'),
           ('CVE-2022-2068', '10.0', '9.8', 'Critical'),
           ('CVE-2021-23841', '4.3', '5.9', 'Medium'),
           ('CVE-2021-3712', '5.8', '7.4', 'High'),
           ('CVE-2020-1968', '4.3', '3.7', 'Low'),
           ('CVE-2021-4160', '4.3', '5.9', 'Medium'),
           ('CVE-2022-0778', '5.0', '7.5', 'High'),
           ('CVE-2021-23839', '4.3', '3.7', 'Low'),
           ('CVE-2020-1971', '4.3', '5.9', 'Medium'),
           ('CVE-2021-23840', '5.0', '7.5', 'High')]

#print(get_top_cves(results))

