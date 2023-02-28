import re

with open('nmap_output.txt', 'r') as file:
    lines = file.readlines()

vuln_patterns = {
    'SSL/TLS MITM vulnerability (CCS Injection)': r'SSL/TLS MITM vulnerability \(CCS Injection\)',
    'SSL POODLE information leak': r'SSL POODLE information leak',
    'Slowloris DOS attack': r'Slowloris DOS attack',
    'Diffie-Hellman Key Exchange Insufficient Group Strength': r'Diffie-Hellman Key Exchange Insufficient Group Strength',
    'Authentication bypass by HTTP verb tampering': r'Authentication bypass by HTTP verb tampering\.',
}

ports_by_vuln = {v: [] for v in vuln_patterns.keys()}

port_pattern = r'^(\d+/\w+)\s+(.+)\s+(.+)'
vuln_pattern = r'\|_\w*:.*'

i = 0
while i < len(lines):
    # look for a line containing port/protocol information
    match = re.search(port_pattern, lines[i])
    if match:
        port = match.group(1).split('/')[0]
        i += 1
        # iterate over all lines that belong to this port
        while i < len(lines):
            # check if we have reached the next port line
            if re.search(port_pattern, lines[i]):
                break
            # check if this line contains vulnerability information
            for vuln_name, vuln_regex in vuln_patterns.items():
                if re.search(vuln_regex, lines[i]):
                    ports_by_vuln[vuln_name].append(port)
            i += 1
    else:
        i += 1

# print the captured ports by vulnerability
for vuln_name, ports in ports_by_vuln.items():
    if ports:
     print(f"{vuln_name} - {','.join(ports)}")
