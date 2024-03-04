from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from pageObject.RegistrationPage import RegistrationPage
from utilities.customeLogger import LogGen


class Test_001_RegistrationFunctionality:
    baseURL = ReadConfig.get_application_url()
    log = LogGen.loggen()

    def test_registration_functionality_001(self, setup):
        self.log.info("****************** Starting Test Case the Registration Functionality TC_RF_001 ****************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.log.info("Navigate to the url")
        self.driver.maximize_window()
        self.log.info("maximizing the browser window")

        self.rp = RegistrationPage(self.driver)
        self.rp.clicking_on_my_account()
        self.log.info("clicking on the my account drop menu")
        self.rp.clicking_on_register()
        self.log.info("clicking on registration link")
        self.rp.set_first_name('Lukesh')
        self.log.info("entering firstname")
        self.rp.set_last_name('Ade')
        self.log.info("entering lastname")
        self.rp.set_email(self.rp.generate_random_username() + '@gmail.com')
        self.log.info("entering email")
        self.rp.set_phone_no('1234567890')
        self.log.info("entering phone number")
        self.rp.set_password("admin")
        self.log.info("Entering password")
        self.rp.confirm_password('admin')
        self.log.info("confirm password")
        self.rp.clicking_on_check_box_agree()
        self.log.info("clicking on check box")
        self.rp.clicking_on_continue()
        self.log.info("clicking on continue button")
        exp_title1 = "Your Account Has Been Created!"
        act_title1 = self.driver.title
        self.log.info("************** Starting the Validation **********************")
        if act_title1 == exp_title1:
            assert True
        else:
            assert False
        self.rp.clicking_on_second_continue()
        self.log.info("clicking on second continue button")
        exp_title = "My Account"
        act_title = self.driver.title
        self.log.info("************** Starting the second Validation **********************")
        if act_title == exp_title:
            assert True
            self.log.info("Registration Test Passed")
        else:
            assert False
        self.log.info("*************** Ending the Test Case the Registration Functionality TC_RF_001 ****************")
        self.rp.teardown()
        self.log.info("closing the browser")

    def test_registration_functionality_003(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.rp = RegistrationPage(self.driver)
        self.rp.clicking_on_my_account()
        self.rp.clicking_on_register()
        self.rp.set_first_name('Lukesh')
        self.rp.set_last_name('Ade')
        self.rp.set_email(self.rp.generate_random_username() + '@gmail.com')
        self.rp.set_phone_no('1234567890')
        self.rp.set_password("admin")
        self.rp.confirm_password('admin')
        self.rp.clicking_on_radio_button_newsletter_subscribe_yse()
        self.rp.clicking_on_check_box_agree()
        self.rp.clicking_on_continue()
        exp_title1 = "Your Account Has Been Created!"
        act_title1 = self.driver.title
        if act_title1 == exp_title1:
            assert True
        else:
            assert False
        self.rp.clicking_on_second_continue()
        exp_title = "My Account"
        act_title = self.driver.title
        if act_title == exp_title:
            assert True
        else:
            assert False
        self.rp.teardown()

    def test_registration_functionality_004(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.rp = RegistrationPage(self.driver)
        self.rp.clicking_on_my_account()
        self.rp.clicking_on_register()
        self.rp.clicking_on_continue()

        act_firstname_text_message = self.driver.find_element(By.XPATH,
                                                              "//div[contains(text(),'First Name must be between 1 and "
                                                              "32 characters!')]")
        exp_firstname_text_message = "First Name must be between 1 and 32 characters!"
        assert act_firstname_text_message.text.__eq__(exp_firstname_text_message)

        act_lastname_text_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'Last Name must be "
                                                                       "between 1 and 32 characters!')]")
        exp_lastname_text_message = "Last Name must be between 1 and 32 characters!"
        assert act_lastname_text_message.text.__eq__(exp_lastname_text_message)

        act_email_text_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'E-Mail Address does not "
                                                                    "appear to be valid!')]")
        exp__email_text_message = "E-Mail Address does not appear to be valid!"
        assert act_email_text_message.text.__eq__(exp__email_text_message)

        act_telephone_text_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'Telephone must be "
                                                                        "between 3 and 32 characters!')]")
        exp_telephone_text_message = "Telephone must be between 3 and 32 characters!"
        assert act_telephone_text_message.text.__eq__(exp_telephone_text_message)

        act_password_text_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'Password must be "
                                                                       "between 4 and 20 characters!')]")
        exp_password_text_message = "Password must be between 4 and 20 characters!"
        assert act_password_text_message.text.__eq__(exp_password_text_message)

        act_privacy_policy_text_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger "
                                                                             "alert-dismissible']")
        exp_privacy_policy_text_message = "Warning: You must agree to the Privacy Policy!"
        assert act_privacy_policy_text_message.text.__contains__(exp_privacy_policy_text_message)
        self.rp.teardown()
