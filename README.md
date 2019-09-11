## Shopify API/Selenium Bot

The purpose of this project is to automate the human element of ordering 
things on Shopify to either automate purchases or do things quickly and 
without error for a time sensitive or limited item.

This project requests the product JSON from a Shopify store. The project 
filters the JSON for the product you are looking for and creates a 
prefilled cart URL which is opened in Selenium.

To use this edit the `shipping.py` file with your correct information. 
You will also need to get the handle, size, (and json_url, and base_cart_url if not using Yeezy Supply) of your product in 
`shopifyboy.py`. For 
`https://yeezysupply.com/products/yeezy-boost-350-v2-lundmark`, the 
handle would be `yeezy-boost-350-v2-lundmark`. You would also need to 
enter the size you are wanting as well as the `size` variable.

If the requested item is not in stock, it will still show a cart with your item in it, but the shipping information will not populate, but that is to be expected.

This is technically working if the product is there, but I am wanting to 
add some changes in the future.

##### To do:
- Add Mac and Linux support (WebDrivers, if statement based on os 
library)
- Add more logic to actively request the API for a list and retry if not 
found.
- Move Selenium into a separate function to make it more modular and add to main(). It is currently closing after function completes. Leaving out of main() for now.

