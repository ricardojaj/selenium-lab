import time
import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage
from pages.carrinho_page import CarrinhoPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.smoke
class Test_adc_produtos:

    def test_adc_produtos_carrinho(self):
        browser = conftest.browser
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce")

        carrinho_page = CarrinhoPage()
        carrinho_page.adcProdutosCarrinho()
        carrinho_page.acessoCarrinho()
        carrinho_page.adcNovoProduto()

        time.sleep(5)
