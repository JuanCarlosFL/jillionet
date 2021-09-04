from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome()
driver.get("https://pancakeswap.finance/farms")

elem = driver.find_element_by_css_selector("div.dalabt")
print(elem)
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()