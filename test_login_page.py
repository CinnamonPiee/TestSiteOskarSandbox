from .pages.login_page import LoginPage


def test_quest_can_see_login_or_registration(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
