import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://www.youtube.com/watch?v=XHD3h4-VVpo")
time.sleep(3)
driver.find_element_by_class_name("ytp-play-button ytp-button").send_keys(Keys.ENTER)
# driver.find_element("aria-label").send_keys(Keys.ENTER)
time.sleep(3)

driver.close()