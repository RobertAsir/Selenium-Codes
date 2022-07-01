import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/ROBERT/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver.get("http://www.google.com")
        # capture the expected and actual title of the page and compare it
        expectedtitle ="welcome"

        actualtitle = self.driver.title

        # add assertEquals to compare the expected and actual
        self.assertEqual(expectedtitle,actualtitle)

        # add assertNotEquals to compare the expected and actual
        self.assertNotEqual(expectedtitle,actualtitle)

        # add assertTrue check the google search box
        self.assertTrue(self.driver.find_element(by=By.NAME,value="q").is_displayed())







if __name__=="__main__":
    unittest.main()
