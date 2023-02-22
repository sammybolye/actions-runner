def get_top_cves(cve_results):
    # Convert the string scores to floats
    cve_results = [(cve, float(base), float(exploit), severity,version) for cve, base, exploit, severity, version in cve_results]

    # Sort the results by the exploitability score in descending order
    sorted_results = sorted(cve_results, key=lambda x: x[2], reverse=True)

    # Select the top result based on the exploitability score
    top_result = max(sorted_results, key=lambda x: x[2])

    # Extract the relevant fields from the top result and create a list of all the CVE identifiers
    top_base_score = str(top_result[1])
    top_exploit_score = str(top_result[2])
    top_severity = top_result[3]
    top_version = top_result[4]
    cve_list = [result[0] for result in sorted_results]

    # Construct the output as a single tuple
    output = (top_severity, top_base_score, top_exploit_score, top_version, cve_list)


    return output



# results = [('CVE-2022-1292', '10.0', '10.0', 'HIGH', '1.0.2u'), ('CVE-2022-2068', '10.0', '10.0', 'HIGH', '1.0.2u'), ('CVE-2021-23841', '4.3', '4.3', 'MEDIUM', '1.0.2u'), ('CVE-2021-3712', '5.8', '5.8', 'MEDIUM', '1.0.2u'), ('CVE-2020-1968', '4.3', '4.3', 'MEDIUM', '1.0.2u'), ('CVE-2021-4160', '4.3', '4.3', 'MEDIUM', '1.0.2u'), ('CVE-2022-0778', '5.0', '5.0', 'MEDIUM', '1.0.2u'), ('CVE-2021-23839', '4.3', '4.3', 'MEDIUM', '1.0.2u'), ('CVE-2020-1971', '4.3', '4.3', 'MEDIUM', '1.0.2u'), ('CVE-2021-23840', '5.0', '5.0', 'MEDIUM', '1.0.2u')]
results =   [('CVE-2023-0286', None, None, None, '1.0.2y'), ('CVE-2023-0215', None, None, None, '1.0.2y'), ('CVE-2022-1292', '10.0', '10.0', 'HIGH', '1.0.2y'), ('CVE-2022-2068', '10.0', '10.0', 'HIGH', '1.0.2y'), ('CVE-2021-3712', '5.8', '5.8', 'MEDIUM', '1.0.2y'), ('CVE-2021-4160', '4.3', '4.3', 'MEDIUM', '1.0.2y'), ('CVE-2022-0778', '5.0', '5.0', 'MEDIUM', '1.0.2y')]
print(get_top_cves(results))