from .pages.catalogue_page import CataloguePage


def test_guest_can_add_product_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = CataloguePage(browser, link)
    page.open()
    page.should_be_catalogue_page()
