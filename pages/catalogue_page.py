from .base_page import BasePage
from .locators import CataloguePageLocators


class CataloguePage(BasePage):

    def should_be_catalogue_page(self):
        self.should_be_catalogue_url()
        self.should_be_button_to_add()
        self.add_product_in_basket()

    def should_be_catalogue_url(self):
        assert "?promo=newYear" in self.browser.current_url

    def should_be_button_to_add(self):
        assert self.is_element_present(*CataloguePageLocators.BUTTON_ADD_TO_BASKET)

    def add_product_in_basket(self):
        link = self.browser.find_element(*CataloguePageLocators.BUTTON_ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()
