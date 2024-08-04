import time
from selenium.webdriver.common.by import By
import pytest
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")

class Test_Login:
    def test_login_valido(self, setup_teardown):
        browser = conftest.browser;
        login_page = LoginPage();

        login_page.fazer_login("standard_user", "secret_sauce");

        products_title = browser.find_element(By.XPATH, "//span[@class='title']");
        assert products_title.is_displayed();

        time.sleep(5);