#Trendyol Web Scraper for Price Monitoring

from bs4 import BeautifulSoup
import requests
import re
from customtkinter import *
from win10toast import ToastNotifier

class Product:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

class PriceMonitor:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        return self.products
    
class WebScraper:
    def __init__(self, url):
        self.url = url
        self.source = self.fetch_page()
        self.soup = self.parse_page()
        
    def fetch_page(self):
        response = requests.get(self.url)
        return response.text

    def parse_page(self):
        return BeautifulSoup(self.source, 'html.parser')

    def scrape_product(self):
        self.product_name = self.soup.find('h1', {'class': 'product-title'}).text
        price_tag = self.soup.find('span', {'class': 'discounted'})
        
        self.product_price = float("".join(filter(str.isdigit, price_tag.text.strip())))
        return Product(self.product_name, self.product_price, self.url)

def main():
    products = []
    monitor = PriceMonitor()
    urls = ["https://www.trendyol.com/hp/victus-amd-ryzen-7-8845hs-16gb-1tb-ssd-rtx4060-8gb-15-6-freedos-fhd-144hz-gaming-laptop-b82n5ea-p-959953848"]
    for url in urls:
        scraper = WebScraper(url)
        product = scraper.scrape_product()
        monitor.add_product(product)
        
    for product in monitor.get_all_products():
        print(f"Product: {product.name},\nPrice: {product.price},\nURL: {product.url}")

if __name__ == "__main__":
    main()