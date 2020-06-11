import time
import unittest
from selenium import webdriver


class TestingSetupClass(unittest.TestCase):
    global driver
    driver = webdriver.Chrome('/Users/pretty.sanwale/PycharmProjects/SeleniumPrograms/driverfile/chromedriver2')

    @classmethod
    def setUpClass(cls):
        print('this is setup method' + '\n')

    @classmethod
    def tearDownClass(cls):
        driver.close()

    def test001(self):
        driver.get('http://newtours.demoaut.com/')
        driver.maximize_window()
        print(driver.title)
        time.sleep(3)
        driver.get('http://pavantestingtools.blogspot.in/')
        driver.maximize_window()
        print(driver.title)
        time.sleep(3)
        driver.back()
        time.sleep(3)
        print(driver.title)
        time.sleep(3)
        driver.forward()
        print(driver.title)

    def test002_explicitly_wait(self):
        driver.get('http://pavantestingtools.blogspot.in/')
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@id='close']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()='Web Automation Testing']").click()
        driver.find_element_by_xpath("//a[text()='JMeter']").click()
        driver.save_screenshot('/Users/pretty.sanwale/PycharmProjects/SeleniumPrograms/screenshot/screen1.jpg')


if __name__ == '__main__':
    unittest.main