import unittest
import ExcelUtil
from selenium import webdriver
from selenium.webdriver.common.by import By

# set the path of the web driver
driver = webdriver.Chrome(executable_path="C:/Users/ROBERT/Downloads/chromedriver_win32/chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/")

# set the path of the Excel File
path = ("C:\\Users\\ROBERT\\Desktop\\TestData.xlsx")

# access the Row count Method
rows = ExcelUtil.getRowCount(path,"Sheet1")
print(rows)

# access ReadData method to get the inputs from Excel file and pass in to the application using for loop

for r in range(2,rows+1):
    username = ExcelUtil.ReadData(path,"Sheet1",r,1)
    password = ExcelUtil.ReadData(path,"Sheet1",r,2)

    driver.find_element(by=By.NAME,value="userName").send_keys(username)
    driver.find_element(by=By.NAME,value="password").send_keys(password)
    driver.find_element(by=By.NAME,value="submit").click()

    if driver.title=="Welcome":
        print("Pass")
        ExcelUtil.WriteData(path,"Sheet1",r,3,"Pass")

    else:
        print("Fail")
        ExcelUtil.WriteData(path,"Sheet1",r,3,"Fail")







    driver.get("https://demo.guru99.com/test/newtours/")















