from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.browser;
        self.titulo_pagina = (By.XPATH, "//span[@class='title']");
        self.mensagem_login_invalido = (By.XPATH, "//h3[@data-test='error']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina);

    def verificar_login_invalido(self):
        self.verificar_se_elemento_existe(self.mensagem_login_invalido);


