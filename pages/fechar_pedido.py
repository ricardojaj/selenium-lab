import conftest;
from selenium.webdriver.common.by import By;

class FecharPedido:
    def __init__(self):
        self.driver = conftest.browser;
        self.checkoutBtn = (By.ID, "checkout");
        self.firstName = (By.XPATH, "//*[@id = 'first-name']");
        self.lastName = (By.XPATH, "//*[@id = 'last-name']");
        self.postalCode = (By.XPATH, "//*[@id = 'postal-code']");
        self.continueBtn = (By.XPATH, "//*[@id = 'continue']");
        self.finalizarPedidoBtn = (By.XPATH, "//*[@id = 'finish']");

    def acessarTelaChecout(self):
        self.driver.find_element(*self.checkoutBtn).click();

    def formularioDeCompra(self, firstName, lastName, postalCode):
        self.driver.find_element(*self.firstName).send_keys(firstName);
        self.driver.find_element(*self.lastName).send_keys(lastName);
        self.driver.find_element(*self.postalCode).send_keys(postalCode);
        self.driver.find_element(*self.continueBtn).click();

    def finalizarCompra(self):
        self.driver.find_element(*self.finalizarPedidoBtn).click();


