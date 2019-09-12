import requests
import platform
import os
from selenium import webdriver
import config

item_handle = config.handle
item_size = config.size
base_url = config.store_url
json_url = config.json
base_cart_url = config.cart


# Function to request the JSON and find variants for matching handle
def get_product_variants(url, handle):
    resp = requests.get(url).json()['products']
    for prods in resp:
        if prods['handle'] == handle:
            return prods['variants']


# Get correct ID for corresponding variant.
def find_id(variants, size):
    for var in variants:
        if var['option1'] == size:
            return var['id']


# Generate Permalink
def generate_cart_url(plain_url, specific_item):
    product_url = plain_url + str(specific_item) + ':1' + config.email
    permalink = '&checkout'.join([product_url,
                                  config.first_name,
                                  config.last_name,
                                  config.address1,
                                  config.address2,
                                  config.city,
                                  config.zipcode,
                                  config.phone])
    return permalink


# Determine the OS and set corresponding path for WebDriver
def get_correct_driver():
    if platform.system() == 'Linux':
        return os.path.join(os.getcwd(), 'chromedriver')
    elif platform.system() == 'Windows':
        return os.path.join(os.getcwd(), 'chromedriver76.exe')
    elif platform.system() == 'Darwin':
        return os.path.join(os.getcwd(), 'chromedriver_mac')
    else:
        print("You do not appear to be running Linux, Windows, or Mac")
        input("Press any key to Exit")
        exit()


# Main Function
def main():
    product = get_product_variants(json_url, item_handle)
    get_id = find_id(product, item_size)
    return generate_cart_url(base_cart_url, get_id)


# Selenium to open Permalink URL
driver_path = get_correct_driver()
driver = webdriver.Chrome(driver_path)
driver.get(main())
