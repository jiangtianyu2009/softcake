from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(webdriver.FirefoxProfile("C:\\Users\\jiang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\5xd6vmv0.default-1480350130384"))
browser.get("http://www.baidu.com")
browser.get("http://pan.baidu.com/s/1i5DLdit")
browser.find_element_by_id("accessCode").clear()
browser.find_element_by_id("accessCode").send_keys("ts63")
browser.find_element_by_class_name("g-button-right").click()
time.sleep(5)
browser.find_element_by_class_name("g-button-right").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id=\"fileTreeDialog\"]/div[3]/a[2]/span/span").click()

