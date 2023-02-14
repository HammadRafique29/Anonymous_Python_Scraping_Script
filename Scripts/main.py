import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from proxies import *
import random
from anonymous_techniques import *


urls = ["https://www.google.com", "https://www.bing.com"]
driver = webdriver.Firefox()
driver.get(urls[0])

driver.execute_script(f"window.open('{urls[1]}', '_blank');")
driver.switch_to.window(driver.window_handles[-1])









# get_proxies = FreeProxies()
# print(get_proxies.verify_proxies())


# # Initialize the Selenium webdriver
# driver = webdriver.Firefox()
#
# # Use the webdriver to open a website
# driver.get("https://www.google.com")
#
# # Get the HTML content of the page
# html_content = driver.page_source
#
# # Use Beautiful Soup to parse the HTML content
# soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
#
#
#
# # Find elements in the HTML content
# elements = soup.find_all('div', class_='example-class')
#
# # Extract data from the elements
# data = []
# for element in elements:
#     data.append(element.text)
#
# # Close the webdriver
# driver.quit()
#
# # Print the extracted data
# print(data)
