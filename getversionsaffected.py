#!/usr/bin/env python3
import subprocess


def get_openssl_sha(version):
    # Determine the format of the version number
    if not version.startswith("3."):
        version = f"OpenSSL_{version.replace('.', '_')}"
    else:
        version = f"openssl-{version}"
    
    command = f"git ls-remote --tags https://github.com/openssl/openssl.git | grep {version}$ | awk '{{print $1}}'"
    output = subprocess.check_output(command, shell=True).decode("utf-8").strip()
    if not output:
        raise ValueError(f"Version {version} not found in the openssl/openssl repository.")
    return output

def get_versions_between(affected_version, fixed_version):
    affected_sha = get_openssl_sha(affected_version)
    fixed_sha = get_openssl_sha(fixed_version)

    command = "git ls-remote --tags https://github.com/openssl/openssl.git | grep -i openssl | egrep -v 'alpha|beta|pre'"
    output = subprocess.check_output(command, shell=True).decode("utf-8").strip()
    lines = output.split("\n")
    
    

    affected_line_number = None
    for i, line in enumerate(lines):
        if line.startswith(affected_sha):
            affected_line_number = i
            break

    if affected_line_number is None:
        raise ValueError(f"SHA-1 {affected_sha} not found in the openssl/openssl repository.")

    tags = []
    for line in lines[affected_line_number:]:
        if line.startswith(fixed_sha):
            break
        tag = line.split("refs/tags/")[1]
        if not all(c.isalnum() or c == "_" or c == "." or c == "-" for c in tag):
            continue
        tags.append(tag)
    
    return tags

versions = get_versions_between("1.1.1", "1.1.1t")
print(versions)

