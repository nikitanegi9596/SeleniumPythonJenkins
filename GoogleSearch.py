import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class MyTestCase(unittest.TestCase):
    def test01(self):
        filePath = "C:\\JenkinsStuff\\Selenium\\drivers\\chromedriver.exe"
        url = "https://www.google.com/"
        driver = webdriver.Chrome(filePath)
        time.sleep(1)
        driver.get(url)
        time.sleep(1)

        searchBox = driver.find_element(By.NAME, "q")
        searchBox.send_keys("automation")
        time.sleep(2)
        searchBox.send_keys(Keys.ARROW_DOWN)
        searchBox.send_keys(Keys.ARROW_DOWN)
        searchBox.send_keys(Keys.ENTER)
        time.sleep(2)
        print(driver.title)
        time.sleep(2)
        driver.quit()
if __name__ == '__main__':
    unittest.main()