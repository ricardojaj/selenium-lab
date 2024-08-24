import time
from selenium.webdriver.common.by import By
import conftest
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class Test_login_invalido:
    def test_login_senha_invalida(self, setup_teardown):
        browser = conftest.browser
        login_page = LoginPage()
        home_page = HomePage()

        #user e senha invalida
        login_page.fazer_login("standard_use", "secret_sau")

        home_page.verificar_login_invalido()

        time.sleep(5)
