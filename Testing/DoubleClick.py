from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



# set the path of the browser or chrome driver
driver =webdriver.Chrome(executable_path="C:/Users/ROBERT/Downloads/chromedriver_win32/chromedriver.exe")

# open the  url
driver.get("https://testautomationpractice.blogspot.com/")

# window maximize
driver.maximize_window()

# identify the double click element and store as a variable
element = driver.find_element(by=By.XPATH,value="//button[contains(text(),'Copy Text')]")

# create an action class interface
actions = ActionChains(driver)

# perform Double click
actions.double_click(element).perform()

