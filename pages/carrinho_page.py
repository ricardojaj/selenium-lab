import conftest
from selenium.webdriver.common.by import By

class CarrinhoPage:
    def __init__(self):
        self.driver = conftest.browser
        self.btn_add_product = (By.XPATH, "//*[@id= 'add-to-cart-sauce-labs-bike-light']")
        self.carrinho = (By.XPATH, "//*[@class = 'shopping_cart_link']")
        self.btnVoltar = (By.ID, "continue-shopping")
        self.btn_adc_novoProduto = (By.XPATH, "//*[@id= 'add-to-cart-sauce-labs-onesie']")


    def adcProdutosCarrinho(self):
        self.driver.find_element(*self.btn_add_product).click()

    def acessoCarrinho(self):
        self.driver.find_element(*self.carrinho).click()
        self.driver.find_element(*self.btnVoltar).click()

    def adcNovoProduto(self):
       self.driver.find_element(*self.btn_adc_novoProduto).click()
       self.driver.find_element(*self.carrinho).click()
