import conftest
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self):
        self.driver = conftest.browser;
        self.username_field = (By.ID, "user-name");
        self.password_field = (By.XPATH, "//*[@id= 'password']");
        self.login_btn = (By.XPATH, "//*[@id= 'login-button']");

    def fazer_login(self, usuario, senha):
        self.driver.find_element(*self.username_field).send_keys(usuario);
        self.driver.find_element(*self.password_field).send_keys(senha);
        self.driver.find_element(*self.login_btn).click();