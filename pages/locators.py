from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    LANGUAGE_FORM = (By.CSS_SELECTOR, "#language_selector .form-control")
    LANGUAGE_LINK = (By.CSS_SELECTOR, "#language_selector .btn")
    NAVBAR_FORM = (By.CSS_SELECTOR, ".navbar-right #id_q")
    NAVBAR_LINK = (By.CSS_SELECTOR, ".navbar-right .btn")
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, ".container-fluid a")
    NAVBAR_BROWSE = (By.CSS_SELECTOR, "#browse .dropdown-toggle")


class MainPageLocators():
    NAVBAR_DROPDOWN_MENU_CATALOGUE = (By.CSS_SELECTOR, ".dropdown-menu [href='/ru/catalogue/']")
    NAVBAR_DROPDOWN_MENU_CLOTHING = (By.CSS_SELECTOR, ".dropdown-menu [href='/ru/catalogue/category/clothing_1/']")
    NAVBAR_DROPDOWN_MENU_BOOKS = (By.CSS_SELECTOR, ".dropdown-menu [href='/ru/catalogue/category/books_2/']")
    NAVBAR_DROPDOWN_MENU_OFFERS = (By.CSS_SELECTOR, ".dropdown-menu [href='/ru/offers/']")
    SUCCESS_AUTH_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class UserProfilePage():
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, ".container-fluid a")
    USER_ACCOUNT_LINK = (By.CSS_SELECTOR, "[href='/ru/accounts/']")
    NAV_PILLS = (By.CSS_SELECTOR, ".nav-pills")
    PROFILE = (By.CSS_SELECTOR, "[href='/ru/accounts/profile/']")
    ORDERS = (By.CSS_SELECTOR, "[href='/ru/accounts/orders/']")
    ADDRESSES = (By.CSS_SELECTOR, "[href='/ru/accounts/addresses/']")
    EMAILS = (By.CSS_SELECTOR, "[href='/ru/accounts/emails/']")
    ALERTS = (By.CSS_SELECTOR, "[href='/ru/accounts/alerts/']")
    NOTIFICATIONS_INBOX = (By.CSS_SELECTOR, "[href='/ru/accounts/notifications/inbox/']")
    WISHLISTS = (By.CSS_SELECTOR, "[href='/ru/accounts/wishlists/']")
    PILLS_INFO = (By.CSS_SELECTOR, ".col-md-9")
# TODO Тут продолжить


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BTN_LOGIN = (By.CSS_SELECTOR, "[name='login_submit']")
    MAIN_PAGE_BREADCRUMBS_LINK = (By.CSS_SELECTOR, ".breadcrumb a")
    DONT_REMEMBER_PASSWORD_LIND = (By.CSS_SELECTOR, "[href='/ru/password-reset/']")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".product_main form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner #basket_formset")
    MAIN_PAGE_BREADCRUMBS_LINK = (By.CSS_SELECTOR, ".breadcrumb a")
