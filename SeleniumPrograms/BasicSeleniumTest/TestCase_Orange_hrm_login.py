import time

from selenium import webdriver
import unittest
import HtmlTestRunner


class OrangeHTMLTestRunner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/Users/pretty.sanwale/PycharmProjects/SeleniumPrograms/driverfile/chromedriver')
        cls.driver.maximize_window()

    def test001_launch_page(self):
        self.driver.get('https://freecrm.com/')
        time.sleep(3)
        self.assertEqual('Free CRM #1 cloud software for any business large or small', self.driver.title, 'title is not matching')

    def test002_login_page(self):
        self.driver.get('https://freecrm.com/')
        time.sleep(3)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//span[text()='Log In']").click()
        self.driver.find_element_by_xpath("//input[@name='email']").send_keys("bewarepretty@gmail.com")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("Active@2020")
        self.driver.find_element_by_xpath("//div[text()='Login']").click()
        self.assertEqual('Cogmento CRM', self.driver.title, 'title is not matching')

    @classmethod
    def test003_tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output='/Users/pretty.sanwale/PycharmProjects/SeleniumPrograms/reports'))






