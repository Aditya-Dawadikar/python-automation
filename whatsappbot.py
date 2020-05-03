from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
#str=input("Enter the msg:")
str="hey"
date=datetime.datetime.now()

driver= webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

elem=driver.find_element_by_class_name("Ameya Pawar")
elem.click()
elem=driver.find_element_by_class_name("_3u328 copyable-text selectable-text")

def sendmsg():

    elem.send_keys(str)
    elem.send_keys(Keys.RETURN)

while(date!="2019-08-31 20:43:00.0000000"):
    date = datetime.datetime.now()
    time.sleep(1)


if(date== "2019-08-31 20:43:00.0000000"):
    sendmsg()