from selenium import webdriver
import time
#http://automationpractice.com is the site for selenium automation
browser=webdriver.Chrome("C:/Users/DELL/Desktop/chromedriver.exe")
browser.get("http://automationpractice.com")
browser.maximize_window()
browser.find_element_by_class_name("login").click()
time.sleep(1000)