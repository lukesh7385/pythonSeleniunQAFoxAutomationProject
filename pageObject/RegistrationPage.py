import random
import string
from selenium.webdriver.common.by import By


class RegistrationPage:
    linkMyAccountDropDownMenu_xpath = (By.XPATH, "//span[normalize-space()='My Account']")
    linkRegister_xpath = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space("
                                    ")='Register']")
    textFirstName_id = (By.ID, "input-firstname")
    textLastName_id = (By.ID, "input-lastname")
    textEmail_id = (By.ID, "input-email")
    textPhoneNo_id = (By.ID, "input-telephone")
    textPassword_id = (By.ID, "input-password")
    textConfirmPassword_id = (By.ID, "input-confirm")
    rdSubscribe_name = (By.NAME, "newsletter")
    checkBoxPrivacyPolicy_name = (By.NAME, "agree")
    btnContinue_xpath = (By.XPATH, "//input[@value='Continue']")
    btn2Continue_linkText = (By.LINK_TEXT, "Continue")
    linkNewsLetter_xpath = (By.XPATH, "//a[normalize-space()='Subscribe / unsubscribe to newsletter']")

    def __init__(self, driver):
        self.driver = driver

    def clicking_on_my_account_drop_down_menu(self):
        self.driver.find_element(*RegistrationPage.linkMyAccountDropDownMenu_xpath).click()

    def clicking_on_register(self):
        self.driver.find_element(*RegistrationPage.linkRegister_xpath).click()

    def set_first_name(self, first_name):
        self.driver.find_element(*RegistrationPage.textFirstName_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*RegistrationPage.textLastName_id).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element(*RegistrationPage.textEmail_id).send_keys(email)

    def set_phone_no(self, phone_number):
        self.driver.find_element(*RegistrationPage.textPhoneNo_id).send_keys(phone_number)

    def set_password(self, password):
        self.driver.find_element(*RegistrationPage.textPassword_id).send_keys(password)

    def confirm_password(self, confirm_password):
        self.driver.find_element(*RegistrationPage.textConfirmPassword_id).send_keys(confirm_password)

    def clicking_on_check_box_agree(self):
        self.driver.find_element(*RegistrationPage.checkBoxPrivacyPolicy_name).click()

    def clicking_on_radio_button_newsletter_subscribe_yse(self):
        self.driver.find_element(*RegistrationPage.rdSubscribe_name).click()

    def clicking_on_continue(self):
        self.driver.find_element(*RegistrationPage.btnContinue_xpath).click()

    def clicking_on_second_continue(self):
        self.driver.find_element(*RegistrationPage.btn2Continue_linkText).click()

    def clicking_on_news_letter_link(self):
        self.driver.find_element(*RegistrationPage.linkNewsLetter_xpath).click()

    def teardown(self):
        self.driver.quit()

    @staticmethod
    def generate_random_username():
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        return username
