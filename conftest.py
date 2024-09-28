import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language what you want to open the site")


@pytest.fixture(scope="session")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()
    