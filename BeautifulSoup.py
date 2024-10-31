import requests
from bs4 import BeautifulSoup

# Specify the URL to scrape
url = 'https://example.com'

# Fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract all links on the page
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
