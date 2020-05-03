from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user="adityadawadikar2000@gmail.com"
pwd="adipraneet"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
assert "facebook" in driver.title
elem= driver.find_element_by_id("email")
elem.send_keys(user)
elem=driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()