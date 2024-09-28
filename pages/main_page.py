from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_catalogue(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR_DROPDOWN_MENU_CATALOGUE), \
        "Catalogue link is not visible on page!"

    def should_be_clothing(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR_DROPDOWN_MENU_CLOTHING), \
        "Clothing link is not visible on page!"

    def should_be_books(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR_DROPDOWN_MENU_BOOKS), \
        "Books link is not visible on page!"

    def should_be_offers(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR_DROPDOWN_MENU_OFFERS), \
        "Offers link is not visible on page!"

    def should_be_success_auth_message(self):
        assert self.is_element_present(*MainPageLocators.SUCCESS_AUTH_MESSAGE), \
        "Success message is not visible on page"
