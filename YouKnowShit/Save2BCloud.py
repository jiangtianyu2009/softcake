from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

distDir = 'F:\\utorrent\\dllink'
filenames = os.listdir(distDir)
print(filenames)

for filename in filenames:
    dlurl = "http://pan.baidu.com/s/" + \
        open(distDir + os.sep + filename, "r").readline().split('/')[4].split(' ')[0]
    flpwd = open(distDir + os.sep + filename, "r").readline()[-4:]
    print(dlurl + '  ' + flpwd)
    browser = webdriver.Firefox(webdriver.FirefoxProfile(\
        "C:\\Users\\jiang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\5xd6vmv0.default-1480350130384"))
    browser.get("http://www.baidu.com")
    browser.get(dlurl)
    browser.find_element_by_id("accessCode").clear()
    browser.find_element_by_id("accessCode").send_keys(flpwd)
    browser.find_element_by_class_name("g-button-right").click()
    time.sleep(3)
    browser.find_element_by_class_name("g-button-right").click()
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id=\"fileTreeDialog\"]/div[3]/a[2]/span/span").click()
    time.sleep(3)
    browser.quit()
    time.sleep(3)
    os.remove(distDir + os.sep + filename)

