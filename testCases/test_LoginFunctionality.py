from utilities.readProperties import ReadConfig
from pageObject.LoginPage import LoginPage
from pageObject.RegistrationPage import RegistrationPage


class Test_002_LoginFunctionality:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    def test_login_functionality_001(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.rp = RegistrationPage(self.driver)
        self.rp.clicking_on_my_account()
        self.lp = LoginPage(self.driver)
        self.lp.click_on_login_link()
        self.lp.enter_email_address(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_on_login_button()

        exp_title = "My Account"
        act_title = self.driver.title

        if act_title == exp_title:
            assert True
        else:
            assert False
        self.rp.teardown()
