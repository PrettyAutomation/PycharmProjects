from selenium import webdriver


def test_org_login1():
    global driver
    driver = webdriver.Chrome('/Users/pretty.sanwale/PycharmProjects/PytestProject'
                              '/SeleniumWithPytest/driverfile/chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(10)


def test_org_login2():
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()


def test_org_login3():
    driver.close()
    driver.quit()
    print('Test Passed')


