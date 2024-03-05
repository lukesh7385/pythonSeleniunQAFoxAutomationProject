from selenium.webdriver.common.by import By


class LogoutPage:
    btnContinue_xpath = (By.XPATH, "//a[normalize-space()='Continue']")
    btnLogout_xpath = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def click_on_logout_button(self):
        self.driver.find_element(*LogoutPage.btnLogout_xpath).click()

    def click_on_continue_button(self):
        self.driver.find_element(*LogoutPage.btnContinue_xpath).click()
