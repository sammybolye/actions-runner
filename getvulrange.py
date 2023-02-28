from bs4 import BeautifulSoup
from getversionsaffected import  get_versions_between

html = '<div data-v-7b1e4942="" class="menu p-0" style="border: unset !important;"><ul data-v-7b1e4942="" class="menu-list mt-1"><li data-v-7b1e4942=""><span data-v-7b1e4942=""><span data-v-7b1e4942="">affected <span data-v-7b1e4942="" class="">from </span><span data-v-7b1e4942="" class="cve-version">3.0.0 </span><span data-v-7b1e4942="" class="">before </span><span data-v-7b1e4942="" class="cve-version">3.0.8 </span></span></span></li></ul><ul data-v-7b1e4942="" class="menu-list mt-1"><li data-v-7b1e4942=""><span data-v-7b1e4942=""><span data-v-7b1e4942="">affected <span data-v-7b1e4942="" class="">from </span><span data-v-7b1e4942="" class="cve-version">1.1.1 </span><span data-v-7b1e4942="" class="">before </span><span data-v-7b1e4942="" class="cve-version">1.1.1t </span></span></span></li></ul><ul data-v-7b1e4942="" class="menu-list mt-1"><li data-v-7b1e4942=""><span data-v-7b1e4942=""><span data-v-7b1e4942="">affected <span data-v-7b1e4942="" class="">from </span><span data-v-7b1e4942="" class="cve-version">1.0.2 </span><span data-v-7b1e4942="" class="">before </span><span data-v-7b1e4942="" class="cve-version">1.0.2zg </span></span></span></li></ul></div>'

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find the div element with class 'menu'
div_element = soup.find('div', {'class': 'menu'})

# find all ul elements under the div element
ul_elements = div_element.find_all('ul')

# create an empty list to store the version information
version_info = []

# loop through each ul element and extract the version information
for ul in ul_elements:
    # find the cve-version class within the ul element and extract the version number
    version_numbers = ul.find_all('span', {'class': 'cve-version'})
    from_version = version_numbers[0].text.strip()
    before_version = version_numbers[1].text.strip()
    version_info.append(f'Affected from {from_version} before {before_version}')
    affected_versions = get_versions_between(from_version,before_version)
    print(affected_versions)

# print the version information as a list
print(version_info)
