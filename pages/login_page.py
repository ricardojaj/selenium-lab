import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.browser;
        self.username_field = (By.ID, "user-name");
        self.password_field = (By.XPATH, "//*[@id= 'password']");
        self.login_btn = (By.XPATH, "//*[@id= 'login-button']");

    def fazer_login(self, usuario, senha):
       # self.driver.find_element(*self.username_field).send_keys(usuario);
       # self.driver.find_element(*self.password_field).send_keys(senha);
       # self.driver.find_element(*self.login_btn).click();
        self.escrever(self.username_field, usuario);
        self.escrever(self.password_field, senha);
        self.clicar(self.login_btn)