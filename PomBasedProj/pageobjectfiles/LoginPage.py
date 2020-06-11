

class LoginPage:
    page_login_xpath = "//span[text()='Log In']"
    userName_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    login_xpath = "//div[text()='Login']"

    def __init__(self, driver):
        self.driver = driver

