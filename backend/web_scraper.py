import requests
from bs4 import BeautifulSoup

class MedicineScraper:
    def __init__(self):
        self.base_url = "https://example-ecommerce.com/search?q="

    def scrape_products(self, search_term):
        url = f"{self.base_url}{search_term}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')

            products = []
            for item in soup.select('.product-item'):
                # Use `.text.strip()` to remove leading/trailing spaces
                name = item.select_one('.product-title').text.strip() if item.select_one('.product-title') else 'No Title'
                link = item.select_one('a')['href'] if item.select_one('a') else '#'
                products.append({'name': name, 'link': link})

            return products

        except requests.exceptions.RequestException as e:
            print(f"Error while fetching the data: {e}")
            return []

# Usage
scraper = MedicineScraper()
products = scraper.scrape_products('ayurvedic+medicine')
print(products)
