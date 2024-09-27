from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def should_be_register_email_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL)

    def should_be_register_password_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD)

    def should_be_register_password_repeat_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD)

    def should_be_btn_to_register(self):
        assert self.is_element_present(*LoginPageLocators.BTN_REGISTER)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_REGISTER).click()

