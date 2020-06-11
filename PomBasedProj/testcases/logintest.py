import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
sys.path.append('/Users/pretty.sanwale/PycharmProjects/PomBasedProj')
from pageobjectfiles.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    url = "https://freecrm.com/"
    driver = webdriver.Chrome('/Users/pretty.sanwale/PycharmProjects/PomBasedProj/driverfile/chromedriver2')
    username = "bewarepretty@gmail.com"
    password = "Active@2020"
    wait = WebDriverWait(driver, 10)

    @classmethod
    def setUpClass(cls):
        time.sleep(3)
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath(lp.page_login_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(lp.userName_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(lp.password_xpath).send_keys(self.password)
        time.sleep(3)
        elem = self.driver.find_element_by_xpath(lp.login_xpath)
        self.wait.until(EC.visibility_of_element_located(self.driver, elem))
        elem.click()
        self.assertEqual("Cogmento CRM", self.driver.title, "title match is not found")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

