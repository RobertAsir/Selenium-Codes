from selenium import webdriver
from selenium.webdriver.common.by import By

# set the path of the browser or chrome driver
driver =webdriver.Chrome(executable_path="C:/Users/ROBERT/Downloads/chromedriver_win32/chromedriver.exe")

# open the url
driver.get("http://www.google.com")

# close the url or browser
driver.close()
