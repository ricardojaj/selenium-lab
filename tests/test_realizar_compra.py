import time
from selenium.webdriver.common.by import By
import conftest
import pytest
@pytest.mark.usefixtures("setup_teardown")
class Test_realizar_compra:
    def test_finalizando_compra(self):
        browser = conftest.browser;
        username = browser.find_element(By.XPATH, "//*[@id='user-name']");
        username.send_keys("standard_user");

        password = browser.find_element(By.XPATH, "//*[@id= 'password']");
        password.send_keys("secret_sauce");

        btn_login = browser.find_element(By.XPATH, "//*[@id= 'login-button']");
        btn_login.click();

        #adc produto
        browser.find_element(By.XPATH, "//*[@id= 'add-to-cart-sauce-labs-onesie']").click();

        #Acessando Carrinho
        browser.find_element(By.XPATH, "//*[@class = 'shopping_cart_link']").click();

        #Click checkout button
        browser.find_element(By.ID, "checkout").click();

        #Preenchendo informaçoes
        firstName = browser.find_element(By.XPATH, "//*[@id = 'first-name']");
        firstName.send_keys("Mariana");

        lastName = browser.find_element(By.XPATH, "//*[@id = 'last-name']");
        lastName.send_keys("Santos");

        postalCode = browser.find_element(By.XPATH, "//*[@id = 'postal-code']");
        postalCode.send_keys("13478580");
        time.sleep(3)
        browser.find_element(By.XPATH, "//*[@id = 'continue']").click();

        #finalizando compra
        browser.find_element(By.XPATH, "//*[@id = 'finish']").click();
        time.sleep(3)
