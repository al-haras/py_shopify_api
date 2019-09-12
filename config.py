# Assign the variables for the specific item you are wanting/size:
handle = 'womens-sweatpants-gravel'
size = 'S'

# Update URL to desired Shopify store as base_url
store_url = 'https://yeezysupply.com/'
json = store_url + 'products.json'
cart = store_url + 'cart/'

# Update placeholder information with correct shipping information
email = "?checkout[email]=email@email.com"
first_name = "[shipping_address][first_name]=First"
last_name = "[shipping_address][last_name]=Last"
address1 = "[shipping_address][address1]=123 Fake Street"
address2 = "[shipping_address][address2]=Apt 1234"
city = "[shipping_address][city]=Anywhere"
zipcode = "[shipping_address][zip]=90210"
phone = "[shipping_address][phone]=5555555555"
