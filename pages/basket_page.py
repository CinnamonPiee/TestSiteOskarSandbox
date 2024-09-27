from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_dont_see_basket_link(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_LINK), "Basket link is on page!"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket is not empty"

    def should_be_text_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No text about empty basket"
