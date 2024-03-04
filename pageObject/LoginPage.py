from selenium.webdriver.common.by import By


class LoginPage:
    linkLogin_xpath = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']")
    textEmailAddress_xpath = (By.XPATH, "//input[@id='input-email']")
    textPassword_xpath = (By.XPATH, "//input[@id='input-password']")
    btnLogin_xpath = (By.XPATH, "//input[@value='Login']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_login_link(self):
        self.driver.find_element(*LoginPage.linkLogin_xpath).click()

    def enter_email_address(self, email):
        self.driver.find_element(*LoginPage.textEmailAddress_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.textPassword_xpath).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*LoginPage.btnLogin_xpath).click()
