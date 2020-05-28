from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_name = "jk@gmail.com"
password = "Password"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.facebook.com/")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()
