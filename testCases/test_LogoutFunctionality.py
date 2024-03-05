from pageObject.LoginPage import LoginPage
from pageObject.LogoutPage import LogoutPage
from pageObject.RegistrationPage import RegistrationPage
from utilities.readProperties import ReadConfig


class Test_003_LogoutFunctionality:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    def test_logout_functionality_001(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.rp = RegistrationPage(self.driver)
        self.rp.clicking_on_my_account_drop_down_menu()
        self.lp = LoginPage(self.driver)
        self.lp.click_on_login_link()
        self.lp.enter_email_address(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_on_login_button()
        self.lo = LogoutPage(self.driver)
        self.lo.click_on_logout_button()
        self.rp.clicking_on_my_account_drop_down_menu()

        if self.driver.find_element(*LoginPage.linkLogin_xpath).is_displayed():
            assert True
        else:
            assert False

        self.lo.click_on_continue_button()

        exp_title = "Your Store"
        act_title = self.driver.title

        if act_title == exp_title:
            assert True
        else:
            assert False
        self.rp.teardown()
