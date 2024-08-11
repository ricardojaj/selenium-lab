import time
from selenium.webdriver.common.by import By
import conftest
import pytest

from pages.carrinho_page import CarrinhoPage
from pages.fechar_pedido_page import FecharPedido
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class Test_realizar_compra:
    def test_finalizando_compra(self, setup_teardown):
        browser = conftest.browser;
        login_page = LoginPage();
        fechar_pedido = FecharPedido();

        login_page.fazer_login("standard_user", "secret_sauce");

        carrinho_page = CarrinhoPage();
        carrinho_page.adcProdutosCarrinho();

        carrinho_page.acessoCarrinho()
        carrinho_page.adcNovoProduto()

        #Click checkout button
        fechar_pedido.acessarTelaChecout();

        #Preenchendo informaçoes
        fechar_pedido.formularioDeCompra("Mariana", "Santos", "11111111")


        #finalizando compra
        fechar_pedido.finalizarCompra()
        time.sleep(3)
