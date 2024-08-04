import pytest
from selenium import webdriver

browser: webdriver.Remote;

@pytest.fixture
def setup_teardown(scope="session"):
    # setup
    global browser
    browser = webdriver.Chrome();
    browser.implicitly_wait(5)
    browser.get("https://www.saucedemo.com/");
    browser.maximize_window();

    #run test
    yield browser

    #teardown
    browser.quit()


