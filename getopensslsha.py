import requests

import requests

def get_openssl_sha(version):
    owner = "openssl"
    repo = "openssl"

    # Replace dots with underscores in the version number
    if version.startswith("3."):
        version = version.replace(".", "_")
        version = f"openssl-{version}"
    else:
        version = version.replace(".", "_")
        version = f"OpenSSL_{version}"

    # Get the SHA-1 commit hash for the specified version
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/git/refs/tags/{version}")
    try:
        sha = response.json()["object"]["sha"]
    except KeyError:
        raise ValueError(f"Version {version} not found in the {owner}/{repo} repository.")

    return sha




version = "3.0.0"
sha = get_openssl_sha(version)
print(f"The SHA-1 commit hash of OpenSSL version {version} is {sha}")

