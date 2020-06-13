import time
import unittest

import HtmlTestRunner
from selenium import webdriver


class TestCase01(unittest.TestCase):
    global driver
    driver = webdriver.Chrome("/Users/pretty.sanwale/PycharmProjects/SeleniumPrograms/driverfile/chromedriver")

    @classmethod
    def setUpClass(cls):
        print('this is setup method' + '\n')

    @classmethod
    def tearDownClass(cls):
        driver.close()

    def test01_launch_browser_login(self):
        driver.get("https://freecrm.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//span[text()='Log In']").click()
        driver.find_element_by_xpath("//input[@name='email']").send_keys("bewarepretty@gmail.com")
        driver.find_element_by_xpath("//input[@name='password']").send_keys("Active@2020")
        driver.find_element_by_xpath("//div[text()='Login']").click()
        try:
            driver.switch_to.alert().dismiss()
        except Exception as e:
            print(format(e))
        try:
            assert "Cogmento CRM" in driver.title
            print("test is passed")
        except Exception as e:
            print(format(e))
        finally:
            print("done")

    def test02_create_contact(self):
        driver.implicitly_wait(10)
        time.sleep(5)
        driver.find_element_by_xpath("//span[text()='Contacts']").click()
        time.sleep(5)
        flag = False
        try:
            flag = driver.find_element_by_xpath("//p[text()='No records found']").is_displayed()
        except Exception as e:
            print(format(e))
        if flag is True:
            print("no records present please create new record")
            time.sleep(5)
            driver.find_element_by_xpath("//i[@class='edit icon']").click()
            driver.find_element_by_xpath("//input[@name='first_name']").send_keys("Pretty")
            driver.find_element_by_xpath("//input[@name='last_name']").send_keys("Sanwale")
            driver.find_element_by_xpath("(//input[@aria-autocomplete='list'])[1]").send_keys("Harman1")
            time.sleep(10)
            driver.find_element_by_xpath("//input[@placeholder='Email address']").send_keys("bewarepretty@gmail.com")
            driver.find_element_by_xpath("(//label)[23]").click()
            driver.find_element_by_xpath("//i[@class='save icon']").click()
            print('test is passed')
            driver.close()
        else:
            print("delete the existing record")
            driver.find_element_by_xpath("//button[@class='ui icon inverted button']").click()
            time.sleep(5)
            driver.find_element_by_xpath("//button[text()='Delete']").click()
            time.sleep(5)
            if driver.find_element_by_xpath("//p[text()='No records found']").is_displayed():
                print("record is deleted successfully")
                print('test is passed')
                driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output='/Users/pretty.sanwale/PycharmProjects/SeleniumPrograms/reports'))
