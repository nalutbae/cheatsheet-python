# Requirement libraries
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def scrape_product_information(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        product_containers = soup.find('div', {'class': 'product-container'})
        for product in product_containers.find_all('div', {'class': 'product'}):
            # product_name = product.find('h2', {'class': 'product-name'}).text.strip()
            # product_price = product.find('span', {'class': 'price'}).text.strip()
            product_name = product.select_one('h2.product-name').text.strip()
            product_price = product.select_one('span.price').text.strip()
            print(f"Product: {product_name}, Price: {product_price}")
            
    else:
        print(f"Failed to retrieve headlines from {url}. Status code: {response.status_code}")


scrape_product_information('https://example.com')