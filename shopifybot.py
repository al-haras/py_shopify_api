import requests
import json
from selenium import webdriver
import shipping
import os

## Shopify API Call and Parsing Json
# Set the handle and size you want (should be predictable)
handle = 'womens-sweatpants-gravel'
size = 'S'
r = requests.get('https://yeezysupply.com/products.json')
products = json.loads((r.text))['products']

# Function to parse and find the correct ID to add to cart.
def getProduct():
    for product in products:
        productParse = product
        productHandle = product['handle']
        if productHandle == handle:
            variants = product['variants']
            for variant in variants:
                id = variant['id']
                option = variant['option1']
                if size == option:
                    return (id)

# Call Function to get correct ID.
correctProduct = getProduct()

# Generate Cart URL.
productURL = "http://yeezysupply.com/cart/{}:1?checkout[email]={}&checkout[shipping_address][first_name]={}&checkout[shipping_address][last_name]={}&checkout[shipping_address][address1]={}&checkout[shipping_address][address2]={}&checkout[shipping_address][city]={}&checkout[shipping_address][zip]={}&checkout[shipping_address][phone]={}".format(correctProduct, shipping.email,shipping.firstName,shipping.lastName,shipping.address1,shipping.address2,shipping.city,shipping.zip,shipping.phone)

## Selenium
# Set Driver Path
driverPath = os.path.join(os.getcwd(), 'chromedriver76.exe')
driver = webdriver.Chrome(driverPath)

# Open Page
driver.get(productURL)
driver.find_element_by_xpath("//*[@id="salesFinal"]").click()