import subprocess

def get_openssl_sha(version):
    # Determine the format of the version number
    if not(version.startswith("3.")):
        version = f"OpenSSL_{version.replace('.', '_')}"
    else:
        version = f"openssl-{version}"
        
        
    print(f"version is: {version}")    

    # Use git ls-remote to retrieve the SHA-1 commit hash for the specified version
    command = f"git ls-remote --tags https://github.com/openssl/openssl.git|grep {version}$ | awk '{{print $1}}'"
    output = subprocess.check_output(command, shell=True).decode("utf-8").strip()
    if not output:
        raise ValueError(f"Version {version} not found in the openssl/openssl repository.")
    return output


affected_version = "1.1.1k"
fixed_version = "3.0.3"

# Get the SHA-1 commit hash for the affected version
affected_sha = get_openssl_sha(affected_version)
print(f"affected_sha is:{affected_sha}")

# Get the SHA-1 commit hash for the fixed version
fixed_sha = get_openssl_sha(fixed_version)
print(f"fixed_sha is:{fixed_sha}")


#command = f"git ls-remote --tags https://github.com/openssl/openssl.git | awk '{{print $1, $2}}' | awk -v start='{affected_sha}' -v end='{fixed_sha}' '$1 > start && $1 < end {{print $2}}' | awk -F '-' '{{print $2}}'"
command = f"git ls-remote --tags https://github.com/openssl/openssl.git | awk '{{print $1, $2}}' | grep -v '{affected_sha}\\|{fixed_sha}' | awk -F '-' '{{print $2}}'"
#command = f"git ls-remote --tags https://github.com/openssl/openssl.git | awk '{{print $1, $2}}' "
print(command)
output = subprocess.check_output(command, shell=True).decode("utf-8").strip()

# Split the output into a list of tags
tags = output.split()

# Remove any junk from the output and format the result to X.X.X format
versions = []
for tag in tags:
    version = tag.strip()
    if not all(c.isdigit() or c.isalpha() or c == "." for c in version):
        continue
    try:
        version_numbers = version.split(".")
        if len(version_numbers) != 3:
            continue
        major, minor, patch = map(int, version_numbers)
        if major < 0 or minor < 0 or patch < 0:
            continue
        versions.append(f"{major}.{minor}.{patch}")
    except ValueError:
        continue

print(versions)