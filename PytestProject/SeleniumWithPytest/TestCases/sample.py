from selenium import webdriver

driver = webdriver.Chrome('/Users/pretty.sanwale/PytestProject/SeleniumWithPytest/driverfile/chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element_by_id('txtUsername').send_keys("Admin")
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()
driver.close()
driver.quit()
print('Test Passed')

