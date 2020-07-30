import unittest
from selenium import webdriver


class TestCase04(unittest.TestCase):
    global driver
    driver = webdriver.Chrome('/Users/pretty.sanwale/PycharmProjects/SeleniumPrograms/driverfile/chromedriver')

    @classmethod
    def setUpClass(cls):
        print('this is setup method' + '\n')

    def test01_launch_flipkart(self):
        driver.get("https://www.flipkart.com/")
        driver.find_element_by_xpath("//input[@title = 'Search for products, brands and more']").send_keys('lapetop')
        driver.refresh()
        driver.find_element_by_xpath('(//img[@class="1Nyybr _30XEf0"])[1]').click()
        driver.switch_to.window()
        laptop_name = driver.find_element_by_xpath('//span[@class = "_35KyD6"]').text
        price = driver.find_element_by_xpath('//div[@class = "_1vC4OE _3qQ9m1"]').text
        dict1 = {laptop_name: price}
        print(dict1)

if __name__ == '__main__':
    unittest.main()








