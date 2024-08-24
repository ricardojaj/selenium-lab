import time
from selenium.webdriver.common.by import By
import pytest
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")

class Test_Login:
    def test_login_valido(self, setup_teardown):
        browser = conftest.browser
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()
