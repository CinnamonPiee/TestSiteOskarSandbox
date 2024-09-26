from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_description = ''

    def should_be_add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    def should_be_success(self):
        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGES))
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                               "basket not found "

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'Add to basket' is not " \
                                                                                "presented "

    def check_success_message(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        # assert self.product_price == msg_lst[-1].text, "Wrong price product added to basket"

    def should_be_dont_see_success_after_add(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                                   "basket not found "

    def should_be_message_disappeared_after_adding_product_in_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                                   "basket not found "
