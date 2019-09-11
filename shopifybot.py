import requests
from selenium import webdriver
import shipping
import os

# Set the handle and size you want (should be predictable)
handle = 'womens-sweatpants-gravel'
size = 'S'
json_url = 'https://yeezysupply.com/products.json'
base_cart_url = 'https://yeezysupply.com/cart/'


# Function to request the JSON and find variants for matching handle
def get_product_variants (url, handle):
        resp = requests.get(url).json()['products']
        for r in resp:
            if r['handle'] == handle:
                variants = r['variants']
                return variants


# Get correct ID for corresponding variant.
def find_id(variants, size):
    for var in variants:
        if var['option1'] == size:
            return var['id']


# Generate Permalink
def generate_cart_url (base_url, id):
    product_url = base_url + str(id) + ':1' + shipping.email
    permalink = '&checkout'.join([product_url,
                            shipping.first_name,
                            shipping.last_name,
                            shipping.address1,
                            shipping.address2,
                            shipping.city,
                            shipping.zip,
                            shipping.phone])
    return permalink


# Main Function
def main():
    product = get_product_variants (json_url, handle)
    get_id = find_id (product, size)
    return generate_cart_url(base_cart_url, get_id)


# Selenium to open Permalink URL
driver_path = os.path.join(os.getcwd(), 'chromedriver76.exe')
driver = webdriver.Chrome(driver_path)
driver.get(main())