## Shopify API/Selenium Bot

The purpose of this project is to automate the human element of ordering 
things on Shopify to either automate purchases or do things quickly and 
without error for a time sensitive or limited item.

This project requests the product JSON from a Shopify store. The project 
filters the JSON for the product you are looking for and creates a Permalink
(pre-filled cart URL) which is opened in Selenium.

Edit the `config.py` file with your correct information.
You will need to get the handle, size, (and store_url if not using Yeezy Supply) of your product in `config.py`. For
`https://yeezysupply.com/products/yeezy-boost-350-v2-lundmark`, the 
handle would be `yeezy-boost-350-v2-lundmark`. the `store_url` would be `https://yeezysupply.com/`

If the requested item is not in stock, it will still show a cart with your item in it, but the shipping information will not populate, but that is to be expected.

This is working if the product is in the store, but I am wanting to
add some changes in the future.

Windows, Linux and Mac support has been added and tested on the following:
- Windows: Chrome Version 76
- Windows: Chrome Version 77
- Linux: Chrome Version 77

##### To do:
- Add more logic to actively request the API for a list and retry if handle not
found.
- Move Selenium into a separate function to make it more modular and add to main(). It is currently closing after function completes. Leaving out of main() for now.
- Add a proper requirements.txt for pip
