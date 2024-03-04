# Requirement libraries
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.select('.headline-class')

        for headline in headlines:
            print(headline.text)
            
    else:
        print(f"Failed to retrieve headlines from {url}. Status code: {response.status_code}")


get_headlines('https://example.com')